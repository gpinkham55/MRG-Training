# SECTION 3: Daily Practical Exercises & Simulations

Every exercise below uses real MR&G customers, orders, items, and prices pulled from P21 on 10/16/2026. Work them in **P21PLAY**. P21PLAY is a copy of live data, so stock and order status there may differ a little from what's printed here. When they differ, P21PLAY is right; write down what you found.

Mentor check notes after each exercise are for the mentor reviewing your work in Block D.

### Exercise 1.1 (Day 1): Navigation Scavenger Hunt

Find and record:

1. Search customers by city "Prattville." Record the Customer ID for International Paper Prattville.
2. That customer's terms and credit status.
3. Its last three orders: dates, PO numbers, and order totals.
4. How many ship-tos it has.
5. Search customers for "Boise Cascade." You'll find two accounts. Record both IDs and bill-to cities, and write one sentence on how you'd tell which one a caller means.
6. Look up these items and record on-hand at location 110:
   - `HB5K-8` (hydraulic hose, -8, 2-wire)
   - `150016595` (gasket sheet, 60" x 63" x 1/16", green)
   - `HSE WTR 300 RBR SUC` (3" rubber water suction hose)

**Mentor check:** IP Prattville is 10549, Net 60, 1 ship-to. Confirm the credit status the trainee read in P21PLAY. Boise Cascade 10399 bills to Chapman, AL; 10400 bills to Boise, ID. Ask the caller which mill and match the ship-to. Sheet 150016595 is stocked and sold in square inches (SI).

### Exercise 1.2 (Day 2): Read the Customer

Account: **WestRock Company (10753)**.

Write a one-paragraph account brief covering: credit limit, terms, credit status, salesrep, number of ship-tos and contacts, how many orders in the last 12 months, typical items bought, and any notepads.

Then answer:

1. Four of the five ship-tos show a PO Box in Duluth, GA. Which ship-to is a real delivery address a truck can go to?
2. WestRock's open order 1040323 (PO 29846666) has a backordered line. What is the item, and what is its disposition?

**Mentor check:** Net 120, salesrep 1005, 5 ship-tos, 4 contacts, about 111 orders in 12 months. The deliverable ship-to is 10756, WestRock Mill Company, Demopolis (28270 Hwy 80 West). Order 1040323 line 1 is 150019658, 3" SS braid hose x 8' with 150# flanges, disposition B.

### Exercise 1.3 (Day 3): The Account With No Contacts

Account: **City of Montgomery Garage (10440)**.

P21 shows **zero** contacts on this account. Its second ship-to (10439, City of Montgomery Landfill) has a person's attention line typed into the address.

*Practice scenario (made-up caller):* "This is Dana Reese, fleet parts buyer for the City garage. I'll be placing your orders now. Invoices still go to the Finance Department, Accounts Division."

Tasks in P21PLAY:

1. Search for duplicates on the caller's name and email before adding.
2. Add Dana Reese as a Purchasing contact linked to 10440, with phone and email (make up practice values).
3. Set quote and acknowledgment delivery to Dana.
4. Look at ship-to 10439. Write down what's in Address 1 and why a contact belongs in Contact Maintenance, not on an address line.
5. Add a dated note on the customer record.

Role play: run a STAMPED interview with your mentor playing Dana asking for "a hose for the shop air reel."

**Mentor check:** contact linked to 10440 with Purchasing role; trainee spots "Attn: Noah Johnson" in ship-to 10439's address line and recommends it move to a contact (with a mentor's OK; don't change live data).

### Exercise 1.4 (Day 4): New Site Ship-To

Account: **Montgomery Water Works (10606)**, Net 30, 1 ship-to.

*Practice scenario:* "We're commissioning a new pump station. Use 1500 Practice Rd, Montgomery, Gate 2. Call Marcus at the station before delivering."

1. Confirm the site isn't already a ship-to.
2. Create the ship-to in P21PLAY with Gate 2 in Address 2.
3. Put the call-ahead in delivery instructions, not the address lines.
4. Check the customer record for tax exemption status before setting the ship-to's tax fields. Write down what you found and confirm with your mentor.
5. Set carrier and preferred location 110.

Product question: they want 20 ft of 3" suction hose. Look up `HSE WTR 300 RBR SUC`. How many feet are available (on hand minus allocated)?

**Mentor check:** as of 10/16, 254 ft on hand with 50 allocated, so 204 ft available. Suction means rigid helix; this item is a rubber suction hose.

### Exercise 1.5 (Day 5): Three Real Stock Orders

Enter each in P21PLAY, have your mentor review, then release.

1. **Counter sale (Montgomery Counter Sales, 910):** 25 ft `AW-32-RD` (2" red air & water hose) and 2 ea `150012469` (0808 brass MNPT x hose barb). Note the terms on account 910 and what that means at the counter.
2. **Phone order (A-1 Industrial Maintenance, 10350):** 50 ft `HSE GP 050 RBR RED` (1/2" red GP hose). Look at their order history first. What does their PO numbering look like?
3. **International Paper Prattville (10549):** 2 ea `F4-2424-FL`. Check the credit status before you save, then watch what happens at release.

**Mentor check:** 910 is COD, Due Immediately: payment at the counter. A-1 uses short sequential POs (175, 179, 186, 223, 225 in April). For IP Prattville, the trainee checks credit status first. If the account is on hold, the order holds; the trainee tells the customer politely and routes to accounting (never work around a hold).

### Exercise 2.1 (Day 6): Pricing, Margin, Freight

1. A customer asks for `HB5K-8` at $5.00/ft. Look up the last price MR&G charged and the moving average cost at location 110. Calculate margin at both prices.
2. Georgia Pacific Pennington (10510) has terms "2% 15, net 60." Explain those terms in one sentence.
3. Enter three P21PLAY orders for any real account: one Prepaid & Add, one Collect, one Will Call.
4. Hydraulic: Boise Cascade buys `HS5K-24`. Read the item description. What is the working pressure and reinforcement? Is it braid or spiral construction?

**Mentor check:** HB5K-8 last price $6.41. Check the trainee's math against the cost P21PLAY shows: margin = (price − cost) ÷ price. A lower price still needs a reason and approval per MR&G pricing rules. 2% 15 net 60: 2% discount if paid in 15 days, otherwise due in 60. HS5K-24: -24 (1-1/2"), 6-wire, 5,100 psi, spiral.

### Exercise 2.2 (Day 7): Mystery Fittings

Identify 12 fittings from the tray. For each, record OD, threads per inch, seat angle or seal type, and final ID. Then find the matching P21 item. Your tray includes BSPP pieces; these are stocked items:

| Item ID | Description | On hand (10/16) |
|---|---|---|
| F2-0808-BSPFS90 | 2-wire 0808 BSPP female swivel 90° | 16 |
| F2-0606-BSPFS90 | 2-wire 0606 BSPP female swivel 90° | 39 |
| F2-0404-BSPFS90 | 2-wire 0404 BSPP female swivel 90° | 36 |
| F2-0405-JFS | 2-wire 0405 JIC female swivel | 54 |
| F2-0405-JFS90S | 2-wire 0405 JIC female swivel 90° | 20 |

Quote three of your identified fittings in P21PLAY to Montgomery Counter Sales (910).

### Exercise 2.3 (Day 8): Quote to Order

Account: **Boise Cascade (10399)**, Chapman, AL.

1. Create a P21PLAY quote for 2 ea `HSE 4W 24 X 6FT 6IN W/ 2424 FL 61 E/E` (-24 hose, 6'6", 2424 Code 61 flange both ends). Use the last price from history. Set a 30-day expiration.
2. Check stock on the components: `HS5K-24` hose and `F4-2424-FL` couplings. Do we have enough for 2 assemblies?
3. Calculate material cost per assembly from moving average costs and the margin at the quoted price (before labor).
4. Customer accepts with PO 4006-PRACTICE. Convert the quote to an order.
5. Confirm the quote shows converted/closed.
6. Run your open quote list and write a follow-up plan for anything older than 14 days.

**Mentor check:** last price $493.68 each. Stock 10/16: 74.59 ft hose (need 13 ft), 9 couplings (need 4). Material cost per assembly = 6.5 ft of hose plus 2 couplings at P21PLAY moving average cost; check the trainee's margin math against it.

### Exercise 2.4 (Day 9): Build and Verify

With Eric Jones, build one of the assembly Boan Contracting (10398) bought in April on order 1021835 (PO 1986-SK140):

- Item `HB5K-4-0405JFS-0405JFSL-7.6`
- Hose `HB5K-4` (-4, 2-wire, 5,100 psi), 7.6 ft
- Fittings `F2-0405-JFS` (straight JIC female swivel) and `F2-0405-JFS90S` (90° JIC female swivel)

Tasks:

1. Look up the crimp spec for HB5K-4 with these couplings. Record die and target diameter.
2. Calculate cut length from catalog cutoff allowances.
3. Build it, orient the 90° per Eric's direction, measure two crimp readings per end, and record.
4. Proof test at 2× working pressure if Eric approves. Record results.
5. Complete the inspection checklist.

### Simulation 2.5 (Day 10): "The Hoses We Got in April"

*Scenario:* A maintenance planner at Boise Cascade calls: "We got some hoses from y'all back in April. I need some more of the same fittings that were on that hose."

Tasks:

1. Figure out which Boise Cascade account (10399 or 10400). Ask the right question.
2. Search Customer Sales History for April 2026. Find the hydraulic hose assembly orders.
3. Open the orders and read the lines. Record order numbers, POs, assembly item, hose item, coupling item, and prices.
4. The caller wants "the same fittings." Couplings like these are crimped. Decide what to offer: loose couplings, or a built assembly. Explain why.
5. Check current stock and price on the couplings.
6. **Before you quote, compare the assembly description to the hose item description. Write down what doesn't match and who you'd ask.**
7. Enter the quote or order in P21PLAY based on what the caller decides.

**Mentor check:** account 10399 (Chapman). Orders 1020742 (4/13, PO "JAMES") and 1020846 (4/14, PO 163972), each 1 ea `HSE 4W 24 X 6FT 6IN W/ 2424 FL 61 E/E` at $493.68, built from 6.5 ft `HS5K-24` and 2 ea `F4-2424-FL` ($157.36 each, 9 on hand). Mismatch: the assembly says 4-wire; the hose item says 6-wire, 5,100 psi. Confirm with Eric before quoting. Also note "JAMES" was typed as a PO number: a name, not a PO.

### Exercise 3.1 (Day 11): Material Match

For each service, pick a gasket material and thickness, explain in one sentence, and find a stocked P21 sheet item that fits:

1. 3" Class 150 RF, 60 psig, 180°F caustic (white liquor)
2. 6" Class 150 RF, 150 psig saturated steam (366°F)
3. 4" FF cast iron water pump flange, 80 psig ambient water
4. 2" Class 300 RF, 400 psig, 600°F hot oil
5. 3" FRP flange, chlorine dioxide service, low pressure

Stocked sheets to choose from (sold by the square inch):

| Item ID | Description |
|---|---|
| SHT INERTECH 60X60 PTFE | ePTFE, 60" x 60" x 1/8" |
| GSKT SHT DURLO PTFE | Durlon 9000 filled PTFE, 60" x 60" x 1/8" |
| SHT SHEET DURLON90 60X60 PTFE | Durlon 9000, 60" x 60" x 1/64" |
| 150016595 | Green sheet, 60" x 63" x 1/16" |
| 150013106 | Green sheet, 60" x 63" x 1/8" |
| GSKT SHT BLACK 8300 | Black sheet, 60" x 60" x 1/8" |
| SHT PAK 48X0125 NEO | Neoprene, 48" wide x 1/8" |
| SHT PAK 48X0125 VITON | Viton, 48" wide x 1/8" |
| SHT 48X0125 RED SBR | Red SBR, 48" wide x 1/8" |

Confirm the grade of the green and black sheets with Kevin Johnson before you count on them for steam or oil.

**Mentor check:** (1) EPDM 1/8" or ePTFE; (2) a steam-rated compressed sheet after P×T check, or graphite; (3) full-face neoprene or SBR 1/8"; (4) graphite with insert, CNA out of range; (5) ePTFE full face (SHT INERTECH).

### Exercise 3.2 (Day 12): Yield and Price a Real Gasket Run

*Scenario:* Georgia Pacific Pennington (10510) asks for 40 ea 4" Class 150 RF ring gaskets and 20 ea 2", 1/16" green sheet.

1. Look up `150016595` in P21PLAY: sheet size, selling unit, and moving average cost.
2. Calculate the sheet cost: 60 × 63 = 3,780 SI × cost per SI.
3. Yield of 4" rings (OD 6.88") per sheet with 0.125" spacing.
4. How many 2" rings (OD 4.12") come from the 4" ring centers (ID 4.50")?
5. Material cost per 4" ring two ways: (a) sheet cost ÷ yield, (b) pitch square (7.005" × 7.005") × cost per SI. Which way does P21 bill if the item sells by SI?
6. Quote both lines in P21PLAY at target margin. Check GP Pennington's terms.
7. Shadow Kevin as he nests the job and compare his yield to yours.

**Mentor check:** pitch 7.005": 60 ÷ 7.005 = 8 across, 63 ÷ 7.005 = 8.99, so 8 down; 64 rings per sheet. Method (b) uses 49.07 SI per ring. Check the trainee's cost math against the P21PLAY cost per SI. All 20 of the 2" rings nest in the 4" centers. Terms 2% 15, net 60.

### Exercise 3.3 (Day 13): Leak Call

*Scenario:* International Paper Selma (10552) calls: "Your gasket leaked on our 6-inch steam line. We put it in yesterday." (Class 150, 150 psig steam, 1/16" compressed sheet ring.)

1. Pull IP Selma's recent orders and find gasket purchases. Record the order and PO.
2. Walk through the troubleshooting questions from Reference Sheet J.
3. Discover: installer reused the old bolts dry, tightened in a circle in one pass, and used anti-seize on the gasket face.
4. Write the reply: professional, helpful, no blame, with correct installation steps and the 8-bolt star sequence.
5. Enter a no-charge replacement order in P21PLAY only if your mentor approves. Note IP Selma's terms (Net 90).

### Simulation 3.4 (Day 14): Six-Call Desk Simulation (Real Accounts)

Mentor plays the callers. Work each start to finish in P21PLAY.

1. **Montgomery Water Works (10606):** "We need a 3-inch suction hose assembly, 20 feet, female cam and groove on one end, male NPT on the other, delivered to our new pump station." Run STAMPED, check `HSE WTR 300 RBR SUC` availability, create the practice ship-to, quote.
2. **Georgia Pacific Pennington (10510), order 1039780, PO 4500995240:** "We got the seal and the paddle blinds. Where are the two bellows?" Find: line 6 (`SS BELLOW 12 X 11 F X FL`) was received from Southeastern Hose on vendor PO 4009424 (10/13) but hasn't shipped. Line 10 (`EXP BELLOW 12X20 FX X FL`) is on backorder against vendor PO 4009425, Kadant Unaflex, due 11/3. Get line 6 moving and give the customer the line 10 date.
3. **Walk-in at the counter (910):** customer brings a hose end with a female swivel 90°: 14 TPI, about 0.83" thread, 55° form, 60° cone seat. Identify it (1/2" BSPP female swivel 90°, item `F2-0808-BSPFS90`), check stock, and quote a replacement assembly on `HB5K-8`.
4. **International Paper Prattville (10549):** buyer wants an order shipped today. Check credit status before promising anything. If the account is on hold, enter the order, explain the hold politely, and route to accounting.
5. **City of Montgomery Garage (10440):** "Who do you have as our contact?" P21 shows none. Add the caller as a contact and set document delivery.
6. **WestRock (10753), order 1040323, PO 29846666:** "When is the stainless braided hose shipping?" Find the line, check for a vendor PO, and call back with a date.

Scored on accuracy, customer communication, and data clean-up (anything you notice that should be fixed in live P21 goes on a list for your mentor, not changed by you).
