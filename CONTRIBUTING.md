# Contributing

Thanks for helping. The guides are used by students revising for real exams, so accuracy and brevity matter more than completeness.

## What is welcome

- A wrong page number, section number or equation.
- A clearer explanation of a topic that is already in a guide.
- A missing topic that is in the BMAS synopsis.
- A verified free link that replaces a dead one.
- A new guide for a course on the current 500-level Harmattan list.

## Ground rules

1. **Do not paste copyrighted material.** No textbook pages, no scanned notes, no past-paper text, no PDFs, no DOCX files. Cite the question number or the chapter instead.
2. **Cite specifically.** "Rao Ch. 4 §4.4.2, p. 222" is useful; "Rao" is not.
3. **Mark inference.** If a claim is not in the notes, the textbook or a past paper, write "inference" or "confirm with the lecturer".
4. **Keep it compact.** One guide is 10–16k characters. If a topic needs more, link to a source rather than expanding the guide.
5. **Use SI units and the course's notation.** If the lecturer uses a different symbol, use the lecturer's and note the alternative once.

## Guide structure

Every guide must contain, in this order:

```
# MCE 5xx — Course title

*N Units · 500 Level, Harmattan · BMAS: MCT 5xx · FUTO Mechatronics*

## Overview
## Synopsis (BMAS, verbatim)
## Sources
## Course Content Summary      <- 3-column table
## Course Content Details      <- one ### per topic
## How to use this
```

Each topic must have a short explanation, then:

```
**Study:** exact chapter/section/pages, plus an optional link.
**Exam:** the past-paper questions this topic unlocks, or "No direct question".
```

followed by `- [ ]` checklist items.

End the guide with:

```
**Refresh before starting (no new textbook):** ...
**Priority:** ...
```

## Maths

Use LaTeX, not Unicode symbols:

- Inline: `$\omega_n=\sqrt{k/m}$`
- Display: `$$\omega_n=\sqrt{\frac{k}{m}}$$`
- Inside a list item, indent the display block by two spaces so it stays in the list.
- Units and chemical formulae in upright text: `$\mathrm{SiO_2}$`, `$5\ \text{mm}$`.
- Do not use `ω`, `√`, `²`, `¨x` or similar characters in formulas. Use `\omega`, `\sqrt{}`, `^2`, `\ddot{x}`.
- Keep display equations for the equation a student must reproduce; keep one-line substitutions inline.

## Adding a course

1. Copy the closest existing guide and change the front matter, synopsis and sources.
2. Build the topic list from the BMAS synopsis first, then the notes, then the papers.
3. Fill the summary table with importance and a frequency label from the papers you actually have.
4. Add the file to the table in `guides/README.md` and to the root `README.md`.
5. Run the checker.

## Checker

```bash
python scripts/check_guides.py
```

It verifies the required headings, that every topic has a Study and Exam line before its first checkbox, the three-column summary table, and the character budget. It does not check factual accuracy; that is the reviewer's job.

## Commits and pull requests

- One logical change per commit. Good messages: `fix(mce-507): correct Rao log-decrement page`, `feat(mce-501): add DH worked example`.
- In a pull request, say which course and topic changed, and give the source you checked.
- If you are correcting a page number, say which edition you used.

## Licence

By contributing you agree that your text is released under the same licence as the repository: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
