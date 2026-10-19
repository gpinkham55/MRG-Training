# MRG-Training: context for Claude Code

New hire training site for Montgomery Rubber & Gasket (MR&G), P21 location 110, part of TRG. Owner: the General Manager. Live site: https://gpinkham55.github.io/MRG-Training/ (GitHub Pages from `main`, root).

## Audience and scope
- All newcomers (inside sales, counter, customer service, warehouse, shop). Not just phone staff: every scenario can come by phone or at the counter.
- Focus: P21 navigation, customer and item inquiry, ship-to and contact maintenance, order entry, quoting, order follow-up, our products and capabilities, industry reference (sizing charts, connection types).
- 3-week plan. First half of each day is self-taught in P21PLAY (our P21 test system); second half with a mentor.

## Content rules
- No employee names. Use roles: Sales Mentor, Shop Mentor, Manager.
- Use real customer names and P21 contacts where possible. Mark made-up callers as practice callers.
- Never publish costs, margins, or credit status (repo is public). Customer prices, order numbers, POs, and item IDs are OK.
- No version numbers or dates on the site.
- Answer keys stay off the site and out of this repo.
- Safety: the only shop rule is safety glasses when cutting or operating equipment. No safety orientation sign-off.
- Each section is its own page.
- Writing style: plain conversational English. Never use the em dash. Avoid: "because", "matters", "while" as a contrast, "exists/existing", times of day and days of the week, "naming/named".

## Structure
| Page | Source |
|---|---|
| Home | `build.py` (home() text and PAGES list) |
| 1 Getting Started | `src/start.md` |
| 2 Schedule | `src/schedule.md` |
| 3 P21 Guides | `src/guides.md` (Guides 3.1 to 3.8) |
| 4 Products & Capabilities | `src/products.md` |
| 5 Product Samples | `src/samples.md`, drawings from `tools/make_sample_art.py` into `img/samples/` |
| 6 Reference | `src/reference.md` (Abbreviations, then Sheets A to O) |
| 7 Exercises | `src/exercises.md` |
| 8 Assessments | `src/assessments.md` |
| Call & Counter Trainer | `trainer.html` (hand-built; requests in the `S` array) |

## Build
- `python3 build.py` (needs pandoc) turns `src/*.md` into the root `*.html` pages. Commit the regenerated HTML.
- A GitHub Action (`.github/workflows/build.yml`) also rebuilds on pushes that touch `src/` or `build.py`. Pull before pushing.
- Palette: olive gray #3D4240, dim gray #6A6E6B, ash gray #AAB0AA, light green #8DD783, pigment green #399A4B. Logo: `img/mrg-logo.png`.

## Trainer data
Each request in `trainer.html` has `ch` (Phone/Counter), `fields`, `good` questions (`a` answer, optional `sys` P21PLAY result, `g` fills fields, `r` prerequisites, `c` coach note), `weak` questions, and `action`. After editing, check every request can fill all its fields and that the script parses.

## P21 data
Real data came from Prophet 21 via the `p21_query_sql` connector (read-only). Key accounts used: IP Prattville 10549, IP Selma 10552, GP Pennington 10510, WestRock 10753 (deliverable ship-to 10756 Demopolis), Boise Cascade 10399 (Chapman) and 10400, Cowin Equipment 10462, Rheem 10662, City of Montgomery Garage 10440, Montgomery Water Works 10606, A-1 Industrial 10350, counter cash account 910.
