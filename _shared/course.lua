-- Course filter for the book (see CLAUDE.md, "Book mechanics").
--   ::: sol ... :::        seminar solution. Shown if the seminar is listed in
--                          `solutions-released` (book/_quarto.yml) or in the lecturer copy,
--                          removed otherwise. Not "solution": Quarto reserves that class.
--   ::: lecturer ... :::   board/timing cue, only in the lecturer copy.
--   ::: proof ... :::      proof of an important result: always inline, closed with an end mark.
--   ::: proof-fold ... ::: proof of a lesser result: a closed dropdown in HTML, printed in full
--                          in PDF (book and lecturer copy). Same end mark either way.
--   HTML only: a download line (PDF, slides) under each lecture/seminar title.
-- Only files named LNN-*.qmd / SNN-*.qmd get the download line.

local lecturer_copy = false
local released = {}
local stem = ""
local kind = nil  -- "L" or "S"
local root = nil  -- repo root (parent of book/)

local function file_exists(path)
  local f = io.open(path, "r")
  if f then f:close() return true end
  return false
end

local function read_meta(meta)
  lecturer_copy = meta["lecturer-copy"] == true
  if meta["solutions-released"] then
    for _, v in ipairs(meta["solutions-released"]) do
      released[pandoc.utils.stringify(v)] = true
    end
  end
  local input = quarto.doc.input_file or ""
  stem = input:match("([^/\\]+)%.qmd$") or ""
  kind = stem:match("^([LS])%d%d")
  root = input:match("^(.*)[/\\]book[/\\]")
end

local function is_released()
  return lecturer_copy or released[stem] or released[stem:sub(1, 3)]
end

local function box(div, ctype, default_title)
  local title = div.attributes["title"] or default_title
  return quarto.Callout({ type = ctype, title = title, content = div.content, appearance = "simple" })
end

-- End-of-proof square for PDF (HTML gets it from book.css). Appended to the last paragraph so
-- it sits at the right edge of the last line, or on its own line after display math.
local function add_qed(blocks)
  local mark = pandoc.RawInline("latex", "\\hfill\\ensuremath{\\square}")
  local last = blocks[#blocks]
  if last and (last.t == "Para" or last.t == "Plain") then
    last.content:insert(mark)
  else
    blocks:insert(pandoc.Plain({ mark }))
  end
  return blocks
end

local function handle_proof(div)
  local fold = div.classes:includes("proof-fold")
  if quarto.doc.is_format("html") then
    if not fold then return nil end  -- Quarto's own .proof block; the end mark comes from CSS
    local out = pandoc.List({
      pandoc.RawBlock("html", '<details class="proof-fold"><summary>Proof</summary><div class="proof-body">'),
    })
    out:extend(div.content)
    out:insert(pandoc.RawBlock("html", "</div></details>"))
    return out
  end
  if quarto.doc.is_format("pdf") or quarto.doc.is_format("latex") then
    local blocks = add_qed(pandoc.List(div.content))
    if fold then
      return pandoc.Div(blocks, pandoc.Attr(div.identifier, { "proof" }, div.attributes))
    end
    div.content = blocks
    return div
  end
  return nil
end

local function handle_div(div)
  if div.classes:includes("proof") or div.classes:includes("proof-fold") then
    return handle_proof(div)
  end
  if div.classes:includes("sol") then
    if is_released() then return box(div, "note", "Solution") end
    return {}
  end
  if div.classes:includes("lecturer") then
    if lecturer_copy then return box(div, "tip", "Board") end
    return {}
  end
end

-- Quarto lifts the chapter title out of the body in book HTML, so the download line
-- goes at the top of the body, right under the rendered title.
local function add_downloads(doc)
  if kind == nil or lecturer_copy or not quarto.doc.is_format("html") then return nil end
  local links = pandoc.List({ pandoc.Link("PDF", "../pdf/" .. stem .. ".pdf") })
  if kind == "L" and root and file_exists(root .. "/slides/" .. stem .. ".qmd") then
    links:insert(pandoc.Str(" · "))
    links:insert(pandoc.Link("Slides", "../slides/" .. stem .. ".html"))
  end
  if kind == "S" and not is_released() then
    links:insert(pandoc.Str(" · Solutions appear here after the seminar."))
  end
  doc.blocks:insert(1, pandoc.Div(pandoc.Para(links), pandoc.Attr("", { "chapter-downloads" })))
  return doc
end

return {
  { Meta = read_meta },
  { Div = handle_div },
  { Pandoc = add_downloads },
}
