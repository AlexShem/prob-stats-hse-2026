// Print a reveal.js deck to PDF with headless Chrome, waiting until reveal and MathJax are done.
// Usage: node scripts/slides_to_pdf.mjs <chrome> <url ending in ?print-pdf> <out.pdf>
// (A plain `chrome --print-to-pdf` prints after a fixed time and gives a blank page when the
// deck is slow to lay out.)
import { spawn } from "node:child_process";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const [chrome, url, out] = process.argv.slice(2);
const port = 9300 + Math.floor(Math.random() * 500);
const profile = mkdtempSync(join(tmpdir(), "slides-pdf-"));
const proc = spawn(chrome, [
  "--headless", "--disable-gpu", "--no-sandbox", `--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`, "--window-size=1280,720",
  "--host-resolver-rules=MAP cdn.jsdelivr.net 127.0.0.1",
  "about:blank",
], { stdio: "ignore" });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const fail = (m) => { console.error(m); proc.kill(); process.exit(1); };

let target;
for (let i = 0; i < 50 && !target; i++) {
  try { target = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find((t) => t.type === "page"); }
  catch { await sleep(200); }
}
if (!target) fail("Chrome did not start");

const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0; const pending = new Map();
ws.onmessage = (e) => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise((r) => { const n = ++id; pending.set(n, r); ws.send(JSON.stringify({ id: n, method, params })); });
const ev = async (expression) => (await send("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true })).result?.result?.value;

await send("Page.enable");
await send("Page.navigate", { url });
let ready = false;
for (let i = 0; i < 300 && !ready; i++) {          // up to 60 s
  await sleep(200);
  ready = await ev(`!!(window.Reveal && Reveal.isReady && Reveal.isReady() && document.querySelector('.pdf-page'))`);
}
if (!ready) fail("reveal never finished the print layout");
const bounded = (p) => `Promise.race([${p}, new Promise((r) => setTimeout(() => r("timeout"), 15000))])`;
const mj = await ev(bounded(`((window.MathJax && MathJax.startup && MathJax.startup.promise) ? MathJax.startup.promise.then(() => "done") : Promise.resolve("no MathJax"))`));
console.error("MathJax:", mj);
await ev(bounded(`document.fonts.ready.then(() => "ok")`));
await sleep(1500);
const r = await send("Page.printToPDF", { printBackground: true, preferCSSPageSize: true });
if (!r.result) fail("printToPDF failed: " + JSON.stringify(r.error));
writeFileSync(out, Buffer.from(r.result.data, "base64"));
proc.kill();
process.exit(0);
