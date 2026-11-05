-- Slides filter: the macro/setup includes at the top of a deck produce invisible blocks that
-- reveal.js would put on an empty slide of their own. Move them under the first heading.
function Pandoc(doc)
  local pre, i = pandoc.List(), 1
  while i <= #doc.blocks and doc.blocks[i].t ~= "Header" do
    pre:insert(doc.blocks[i]); i = i + 1
  end
  if #pre == 0 or i > #doc.blocks then return nil end
  local out = pandoc.List({ doc.blocks[i] })
  out:extend(pre)
  for j = i + 1, #doc.blocks do out:insert(doc.blocks[j]) end
  doc.blocks = out
  return doc
end
