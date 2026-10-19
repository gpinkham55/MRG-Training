# MR&G Training

New hire training site for Montgomery Rubber & Gasket: P21 navigation, customer and item inquiry, ship-to and contact maintenance, order entry, quoting, our products and capabilities, and industry reference charts.

**Live site:** https://gpinkham55.github.io/MRG-Training/

## Pages

| Page | Source |
|---|---|
| Home | `build.py` |
| Getting Started | `src/start.md` |
| Schedule | `src/schedule.md` |
| P21 Guides | `src/guides.md` |
| Products | `src/products.md` |
| Reference | `src/reference.md` |
| Exercises | `src/exercises.md` |
| Assessments | `src/assessments.md` |
| Call & Counter Trainer | `trainer.html` (hand-built) |

Exercises and trainer scenarios use real customer, order, and item data from P21. Costs, margins, and credit status are left out; trainees look those up in P21PLAY. Answer keys are kept off this site.

## Updating the site

Edit the Markdown file for the page in `src/` (on github.com: open the file, tap the pencil icon, edit, then Commit changes). A GitHub Action rebuilds the pages automatically within a minute or two. Check progress on the Actions tab.

Markdown basics: `## Heading`, `**bold**`, `- bullet`, `1. numbered step`, and tables written with `|` between columns.

## Call & Counter Trainer

A customer calls or walks up to the counter. The trainee picks the best next question from several options, gets the customer's answer or a P21PLAY lookup result, and builds a ticket. When the ticket is complete, the trainee picks the right P21PLAY action and gets the entry steps.

Scoring: +10 good question, -5 off-track question, +20 correct P21 action, -10 wrong action.

All requests live in the `S` array in `trainer.html`. Each request has:
- `ch`: "Phone" or "Counter"
- `fields`: the ticket lines
- `good`: legitimate questions. `a` is the customer's answer, `sys` is an optional P21PLAY lookup result, `g` fills ticket fields, `r` lists fields that must be filled before the question appears, `c` is the coach note.
- `weak`: off-track questions with a coach note
- `action`: the final P21PLAY decision and the entry steps

Practice entries go in P21PLAY, never live P21.
