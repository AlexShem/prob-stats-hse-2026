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
-- Line for a lecture: "PDF · Slides (PDF)"; for a seminar: "PDF".

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

-- `chapter` is the SNN prefix a sol block was tagged with (see tag_chapters); without a tag,
-- fall back to the file being rendered (HTML renders one chapter per file).
local function is_released(chapter)
  if chapter then return lecturer_copy or released[chapter] end
  return lecturer_copy or released[stem] or released[stem:sub(1, 3)]
end

-- The book PDF is one combined document, so the file name says nothing about which seminar
-- a sol block is in. Walk the blocks in order and tag each sol with the SNN of the last
-- level-1 heading `{#sec-SNN}` before it.
local function tag_chapters(doc)
  local current = nil
  return doc:walk({
    traverse = "topdown",
    Header = function(h)
      if h.level == 1 then current = h.identifier:match("^sec%-([LS]%d%d)$") end
    end,
    Div = function(div)
      if current and div.classes:includes("sol") then
        div.attributes["data-chapter"] = current
        return div
      end
    end,
  })
end

local function box(div, ctype, default_title)
  local title = div.attributes["title"] or default_title
  return quarto.Callout({ type = ctype, title = title, content = div.content, appearance = "simple" })
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
  if fold and (quarto.doc.is_format("pdf") or quarto.doc.is_format("latex")) then
    -- Quarto's own .proof blocks become amsthm proof environments, which draw the end square.
    -- A folded proof is printed in full, so give it the same environment.
    local out = pandoc.List({ pandoc.RawBlock("latex", "\\begin{proof}") })
    out:extend(div.content)
    out:insert(pandoc.RawBlock("latex", "\\end{proof}"))
    return out
  end
  return nil
end

local function handle_div(div)
  if div.classes:includes("proof") or div.classes:includes("proof-fold") then
    return handle_proof(div)
  end
  if div.classes:includes("sol") then
    if is_released(div.attributes["data-chapter"]) then return box(div, "note", "Solution") end
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
    links:insert(pandoc.Str(" ("))
    links:insert(pandoc.Link("PDF", "../slides/" .. stem .. ".pdf"))
    links:insert(pandoc.Str(")"))
  end
  if kind == "S" and not is_released() then
    links:insert(pandoc.Str(" · Solutions appear here after the seminar."))
  end
  doc.blocks:insert(1, pandoc.Div(pandoc.Para(links), pandoc.Attr("", { "chapter-downloads" })))
  return doc
end

return {
  { Meta = read_meta },
  { Pandoc = tag_chapters },
  { Div = handle_div },
  { Pandoc = add_downloads },
}
