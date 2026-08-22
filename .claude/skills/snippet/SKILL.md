---
name: snippet
description: Create a new snippet card (_snippets/**/snip_*.md) for this site — a single-idea extract of mūlam plus bhāvārtha, rendered to a fixed-size image. Use when asked to make a snip_vs_NNNN (or other snip_* series) based on an existing snippet and a theme, e.g. "create snip_vs_0004 from snip_vs_0003, on the pair व्यापकम् + नामरूपयोरधिष्ठानम्".
---

# Making a snippet card

The user gives three things: the **output stem** (`snip_vs_0004`), a **base file** to
imitate, and the **theme** (usually a pair of viśeṣaṇas, a sūtra, or one idea).

## 1. Read the base, and the neighbour before it

`cat` the named base file *and* the snippet before it. Two samples show which parts
are fixed template and which vary. Everything in the front matter except `permalink`
and `title` is carried over verbatim — `layout`, `source`, `source_url`, `image`,
`image_alt` all stay the same within a series.

## 2. Go to the mūlam — never compose Sanskrit from scratch

The base's `source_url` (e.g. `/sagara/1/002`) names the grantha page. Find it by
permalink and read it:

```
grep -rln "permalink: /sagara/1/002" --include="*.md" . | grep -v _site
```

The theme the user names is almost always a clause already in that page. Copy the
mūlam for it and **condense** — that is the whole editorial act. Compare the base
snippet against its own clause in the source to see the house style. In the
विचारसागरः series the condensation rule is:

- drop school attributions (`न्यायमतसिद्ध-`, `बौद्धानाम्`, `साङ्ख्याभिमते`)
- drop the `तद्वारणाय '...' इति` framing; end the first sentence at `अतिव्याप्तिः।`
- keep the second sentence's skeleton parallel to the neighbouring snippets —
  `X-त्वेऽपि तेषां Y-त्वेन Z-त्वाभावान्नातिव्याप्तिः।`
- open with `स्वस्वरूपं **A + B** —` using the theme pair in bold

If the theme is genuinely not in the source, say so and ask before inventing Sanskrit.

## 3. The translation is short by design

Three or four lines of plain English in `<div class="translation-inline" markdown="1">`,
IAST for Sanskrit terms, no devanāgarī. It restates the pair and says what the added
clause excludes. It is not a gloss of every word of the mūlam.

## 4. Render and look at it — the card does not scroll

The card is a fixed 1440x960 box; overflow silently collides with the footer rule.
Always build and export, then **Read the PNG and look at it**:

```
source /opt/homebrew/opt/chruby/share/chruby/chruby.sh && chruby ruby-3.4.1 && bundle exec jekyll build
path/to/venv/bin/python scripts/snippet_export.py snip_vs_0004
```

Read `exports/snippets/snip_vs_0004.png`. The last line of the translation must clear
the footer rule with visible slack — compare against the base snippet's PNG. If it is
tight or overrunning, tighten the English (the Sanskrit is fixed by the mūlam) and
re-export. Expect one or two passes.

`make snippets snip_vs_0004` does the same thing and then opens the image; prefer the
two commands above so nothing pops open in the user's face mid-task.

## 5. Nothing else to wire up

`index_snippets.md` lists `site.snippets` automatically. Do not edit it.

## Report

Show the rendered PNG, name the file created, and mention that
`exports/snippets/<stem>.png` and `_site/` were touched by the verification build.
