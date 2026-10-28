# Methodology

How the guides were built, how the "exam likelihood" column was estimated, and where the method is weak.

## 1. Scope

The course list is the 500-level Harmattan semester for Mechatronics Engineering at FUTO. Each guide follows the official BMAS synopsis for the course, expanded into topics that match what was actually taught and examined.

Three courses with resources in the Drive folder are excluded because they are not on the offered list: MCE 505 (Microcomputers), MCE 509 (Control Engineering II) and MCE 527 (Cyber Security).

Two courses have no BMAS entry: MCE 515 (Project I) and MCE 529 (Seminar and Industrial Exchange Programme). Their guides follow the closest BMAS analogues (MCT 599 and MCT 413) and standard departmental practice, and say so explicitly. MCE 521 has no lecture notes or past paper; it is reconstructed from BMAS MCT 519 and standard microfabrication texts.

## 2. Evidence hierarchy

When sources disagreed, this order decided:

1. **BMAS synopsis** — the official scope. If a topic is in the synopsis, it is in the guide even when no paper has asked it.
2. **Taught material** — lecturer notes, handouts and the textbook edition used in class. This decides notation and emphasis.
3. **Past papers** — what was actually asked, and how often.
4. **Standard textbooks and open courseware** — used to fill gaps, with the specific chapter cited.

A topic that is in the synopsis but never examined is marked low priority, not deleted. A topic that is examined but thinly taught is marked as inference.

## 3. How the topic list was made

For each course:

1. Read the BMAS synopsis and split it into examinable concepts.
2. Read the lecturer notes and the table of contents of the set text; map each concept to a chapter and section.
3. Read every available past paper and tag each question with the concepts it tests.
4. Merge the two lists. Concepts that appear in both are core; concepts that appear only in the synopsis are "BMAS-mandated"; concepts that appear only in papers are flagged as inference.
5. Write one checklist item per thing you must be able to *do*, not per paragraph of the book.

## 4. How "exam likelihood" was estimated

The label is a count across the papers available for that course, not a prediction:

- **Very high** — appears in every available paper, usually more than once.
- **High** — appears in two of three, or once with heavy marks.
- **Medium** — appears once, or only as part of a larger question.
- **Low** — in the synopsis but not asked in the available papers.
- **Unknown** — no paper available, or the topic is new.

The sample is small: two or three papers per course, and one for MCE 507. Treat the labels as a study order, not a guarantee. A new lecturer can change the balance.

## 5. Known limitations

- **Small paper sample.** Three sessions at most. A topic marked "Low (0/3)" can still appear.
- **OCR and handwriting.** Some papers and notes are scans. Question numbers and part labels may be incomplete; where a paper was unreadable, the guide says so rather than guessing.
- **Syllabus drift.** Course codes and content change between sessions. MCE 511 is a known ambiguity between 505 and 511.
- **Edition drift.** Page numbers follow the PDFs in the Drive folder. A different edition shifts them.
- **Inference.** MCE 515, 521 and 529 contain material that is reconstructed rather than taught. It is labelled in the guide and should be checked with the coordinator.
- **No mark schemes.** The "Exam" lines say which question a topic unlocks, not how many marks each part carries.

## 6. Maintaining a guide

When you correct or extend a guide:

1. Change one topic at a time and keep the Study → Exam → checklist order.
2. Cite a chapter and page, not a whole book.
3. If you add a past-paper reference, use the paper's own numbering and say which paper.
4. If a claim is inference, write "inference" or "confirm with the lecturer".
5. Run `python scripts/check_guides.py` before committing.
6. Update the character and checkbox counts in `guides/README.md` if they moved.

## 7. What this is not

These are student notes. They are not a substitute for the lecturer, the textbook or the lab. They do not contain past-paper text, and they do not claim to predict the next paper.
