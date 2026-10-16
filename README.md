# MR&G Training

Onboarding site for new Montgomery Rubber & Gasket inside sales, counter, and customer service hires.

Exercises use real customer, order, item, and price data from P21 (pulled 10/16/2026). Costs, margins, and credit status are left out; trainees look those up in P21PLAY.

**Live site:** https://gpinkham55.github.io/MRG-Training/

## Pages
- `index.html`: home
- `schedule.html`: 3-week schedule, daily blocks, mentor hours
- `guides.html`: P21 workflow guides
- `reference.html`: product and standards reference sheets
- `exercises.html`: daily exercises and simulations
- `assessments.html`: quizzes, final exam, sign-off record (answer keys are kept off the public site)
- `trainer.html`: Call Desk Trainer

## Updating the plan
Edit the Markdown in `src/`, then run `python3 build.py` (needs pandoc) and commit the regenerated pages.

# Call Desk Trainer

Branching customer-call simulator for new Montgomery Rubber & Gasket inside sales, counter, and customer service hires.

A customer calls with a request. The trainee picks the best next question from several options, gets the customer's answer (or a P21PLAY lookup result), and builds a call ticket. Once the ticket is complete, the trainee chooses the right P21PLAY action and gets the step-by-step entry list.

## Calls
1. Suction Hose Assembly (new ship-to, quote)
2. Hydraulic Press Hose (assembly order)
3. Steam Header Gaskets (quote, extended validity)
4. Steam Hose Special Order
5. Missing Invoices (contact maintenance)
6. April Hose Reorder (sales history search)
7. Counter Walk-In Adapter (thread ID)
8. Where's My Order? (backorder, TRG transfer)
9. Price Match Request (margin and approval)
10. Wrong Gaskets Shipped (RMA and replacement)

## Scoring
+10 good question, -5 off-track question, +20 correct P21 action, -10 wrong action.

## Editing calls
All calls live in the `S` array inside `trainer.html`. Each call has:
- `fields`: the call ticket lines
- `good`: legitimate questions. `a` is the customer's answer, `sys` is an optional P21PLAY lookup result, `g` fills ticket fields, `r` lists fields that must be filled before the question appears, `c` is the coach note.
- `weak`: off-track questions with a coach note
- `action`: the final P21PLAY decision and the entry steps

All customers, orders, and prices are made up. Practice entries go in P21PLAY, never live P21.
