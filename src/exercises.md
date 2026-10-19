# Section 7: Exercises

Every exercise uses real customers, contacts, orders, and items from P21. Work them in **P21PLAY**. Each request could come by phone or across the counter; handle it the same way.

Stock and order status in P21PLAY change over time. When what you find differs from what's written here, trust P21PLAY and write down what you found. Where a scenario needs a caller who isn't in P21 yet, the name is marked as a practice caller.

Mentor check notes after each exercise are for the mentor reviewing your work in Block D.

## Week 1

### Exercise 1.1 (Day 1): Navigation Scavenger Hunt

Using only inquiry windows (Guide 3.1):

1. Add Order Entry, Customer Master Inquiry, Item Master Inquiry, Ship To Maintenance, Contact Maintenance, and Order Inquiry to your favorites.
2. Search customers by city "Prattville." Record the customer ID for International Paper Prattville.
3. Record its terms, credit status, and number of ship-tos.
4. Record its last three orders: PO numbers and order totals.
5. Search customers for "Boise Cascade." You'll find two accounts. Record both IDs and bill-to cities. Write one sentence on how you'd tell which one a customer means.
6. Look up these items. Record the description, unit of measure, and available quantity at location 110:
   - `HB5K-8`
   - `150016595`
   - `HSE WTR 300 RBR SUC`
   - `FIT CAM CPLG 300 ALM C`

**Mentor check:** IP Prattville is 10549, Net 60, one ship-to; ask what credit status the trainee found and what it means for an order. Boise Cascade 10399 bills to Chapman, AL; 10400 bills to Boise, ID; ask which mill and match the ship-to. `150016595` is green gasket sheet sold by the square inch (SI). Check that the trainee read available, not just on hand.

### Exercise 1.2 (Day 2): Read the Customer

Account: **WestRock Company (10753)**.

Write a one-paragraph account brief: terms, credit status, salesrep, number of ship-tos and contacts, how often they order, what they typically buy, and any notepads.

Then answer:

1. Four of the five ship-tos show a PO box. Which ship-to is a real delivery address?
2. List the contacts. Which are real people, and which is a placeholder for an invoice mailbox?
3. Open order 1040323 (PO 29846666). What is the backordered item, and what is its disposition?

**Mentor check:** Net 120, salesrep 1005, five ship-tos. The deliverable ship-to is 10756, WestRock Mill Company Demopolis (28270 Highway 80 West). Contacts: Michael Boyd and Vijaya Gangamuni (Purchasing), Charlie Witherspoon, and "WestRock Co. (invoices)" as the AP placeholder. Order 1040323 line 1 is `150019658`, a 3" stainless braided hose x 8' with 150# flanges, disposition B.

### Exercise 1.3 (Day 3): Contacts That Need Work

**Part A: City of Montgomery Garage (10440).** P21 shows no contacts on this account.

*Request (practice caller, phone or counter):* "I'm Dana Reese, fleet parts buyer for the City garage. I'll be placing your orders now. Invoices still go to the Finance Department, Accounts Division."

In P21PLAY:

1. Search for duplicates on the name and email before adding.
2. Add Dana Reese as a Purchasing contact on 10440 with practice phone and email.
3. Set quotes and acknowledgments to go to the new contact.
4. Open ship-to 10439 (City of Montgomery Landfill). What's typed in Address 1? Why does that belong in Contact Maintenance?
5. Add a dated note on the customer.

**Part B: other accounts.** Look at the contacts on Georgia Pacific Pennington (10510), Montgomery Water Works (10606), and Montgomery Counter Sales (910). For each, write down anything that looks wrong or out of date.

Role play: run a STAMPED interview with your mentor asking for "a hose for the shop air reel."

**Mentor check:** Part A: an "Attn:" line with a person's name sits in ship-to 10439's address; it should move to a contact (with a mentor's OK; don't change live data). Part B: GP has two named contacts (Cade Baker, Justin Phillips) plus a "past due" placeholder; Water Works has only an invoice placeholder and no named buyer; 910 still lists a former employee as a contact. All three go on the clean-up list.

### Exercise 1.4 (Day 4): New Site Ship-To

Account: **Montgomery Water Works (10606)**, Net 30, one ship-to.

*Request:* "We're commissioning a new pump station at 1500 Practice Rd, Montgomery, Gate 2. Call the station before you deliver."

1. Confirm the site isn't already a ship-to.
2. Create the ship-to in P21PLAY with Gate 2 in Address 2.
3. Put the call-ahead in delivery instructions, not the address lines.
4. Check the customer for tax exemption before you set the ship-to's tax fields. Confirm with your mentor.
5. Set carrier and preferred location 110.

Product questions:

1. They want 20 ft of 3" suction hose. Look up `HSE WTR 300 RBR SUC`. How many feet are available?
2. Their pump has a 3" male groove adapter. Which cam and groove type goes on the hose, and what's our item ID for it in aluminum? In stainless?

**Mentor check:** available = on hand minus allocated. Suction means a rigid helix; this item is a rubber suction hose. A coupler goes on the hose: Type C. Aluminum `FIT CAM CPLG 300 ALM C`; stainless `150012302` or the crimp-style `FIT CAM CPLG 300 SS C CRIMP`.

### Exercise 1.5 (Day 5): Three Real Orders

Enter each in P21PLAY. Your mentor reviews before release.

1. **Counter walk-in (Montgomery Counter Sales, 910):** 25 ft `AW-32-RD` (2" red air and water hose) and 2 ea `150012469` (brass MNPT x hose barb). What are the terms on account 910, and what does that mean at the counter?
2. **Phone order (A-1 Industrial Maintenance, 10350):** 50 ft `HSE GP 050 RBR RED`. Check their history first. What do their PO numbers look like?
3. **International Paper Prattville (10549), contact Blake Wynne (Purchasing):** 2 ea `F4-2424-FL`. Check credit status before you save, then watch what happens at release.

**Mentor check:** 910 is COD, due immediately: payment at the counter. A-1 uses short sequential PO numbers. For IP Prattville, if the account is on hold, the order holds; the trainee tells the customer politely and routes to accounting (never work around a hold).

## Week 2

### Exercise 2.1 (Day 6): Pricing, Freight, and Hydraulic Hose

1. **Cowin Equipment (10462)** buys `HB5K-8` regularly. Open their sales history for that item. What prices have they paid, and did the price change? Why might it have changed, and what would you check before you answered the customer?
2. Georgia Pacific Pennington (10510) buys on "2% 15, net 60." Explain those terms in one sentence.
3. Enter three P21PLAY orders for any real account: one prepaid and add, one collect, one will call.
4. Boise Cascade buys `HS5K-24`. Read the item description. What size is it, how many wires, what working pressure, and is it braid or spiral?

**Mentor check:** Cowin has paid $6.01/ft and, more recently, $6.41/ft. Check for a supplier cost increase or a pricing change before explaining; don't guess. 2% 15, net 60: 2% off if paid within 15 days, otherwise due in 60. `HS5K-24`: -24 (1-1/2"), 6-wire, 5,100 psi, spiral.

### Exercise 2.2 (Day 7): Mystery Fittings

Identify 12 fittings from the tray. For each, record OD, threads per inch, seat or seal type, and final ID. Then find the matching item in P21PLAY using Reference Sheet O. The tray includes these stocked pieces:

| Item ID | Description |
|---|---|
| F2-0808-JFS | 2-wire, -08 JIC female swivel |
| F2-0808-OBM | 2-wire, -08 O-ring boss male |
| F2-0808-OFS | 2-wire, -08 ORFS female swivel |
| F2-0808-PM | 2-wire, -08 NPT male |
| F2-0808-BSPFS90 | 2-wire, -08 BSPP female swivel 90° |
| 7000-06-06 FG | Adapter, 3/8" male JIC x 3/8" male BSPT |

Quote three of your identified fittings in P21PLAY to Montgomery Counter Sales (910).

### Exercise 2.3 (Day 8): Where's My Order?

**Georgia Pacific Pennington (10510)**, contact Justin Phillips, PO 4500995240, our order 1039780.

*Request:* "We got the seal and the paddle blinds. Where are the two bellows?"

1. Find the order from the PO.
2. Read each line and its disposition.
3. For each bellows, find the purchase order behind it: vendor, promise date, quantity received.
4. One bellows shows received from the vendor but not shipped to GP. What do you do?
5. What do you tell the customer about the other one?
6. Add a dated note to the order.

Then do the same for **WestRock (10753), order 1040323, PO 29846666**, contact Michael Boyd: "When is the stainless braided hose shipping?"

**Mentor check:** order 1039780 line 6 (`SS BELLOW 12 X 11 F X FL`) was received on a vendor PO from Southeastern Hose but hasn't shipped; find it in the building and get it moving. Line 10 (`EXP BELLOW 12X20 FX X FL`) is on backorder against a vendor PO to Kadant Unaflex; give the customer that PO's promise date.

### Exercise 2.4 (Day 9): Build and Verify

With the Shop Mentor, build a copy of the assembly **Cowin Equipment (10462)** bought on order 1035074 (PO SPO025514):

- Item `HB5K-8-0808JFS-0808OBM-7.04`
- Hose `HB5K-8`, 7.04 ft
- Fittings `F2-0808-JFS` (JIC female swivel) and `F2-0808-OBM` (O-ring boss male)

1. Read the assembly item ID using Reference Sheet O and explain each part.
2. Look up the crimp spec for this hose and coupling series. Record die and target diameter.
3. Work out cut length from the catalog cutoff allowances.
4. Build it, take two crimp readings per end, and record them.
5. Proof test at 2x working pressure if the Shop Mentor approves.
6. Complete the inspection checklist (Reference Sheet I, part 8).

### Simulation 2.5 (Day 10): "The Hoses We Got in April"

*Request:* Dewayne Winslett from Boise Cascade: "We got some hoses from y'all back in April. I need some more of the same fittings that were on that hose."

1. Dewayne is a contact on Boise Cascade **10400**. Search both Boise accounts. Which one has the April hydraulic hose orders?
2. Search sales history for April. Find the hose assembly orders.
3. Open them and read the lines. Record order numbers, POs, assembly item, hose item, coupling item, and prices.
4. "The same fittings" are crimp couplings. Do you sell loose couplings, or build an assembly? Explain.
5. Check current stock and price on the couplings and hose.
6. Compare the assembly description to the hose item description. What doesn't match, and who would you ask?
7. Build a quote in P21PLAY (Guide 3.7) for two assemblies. Then convert it to an order with practice PO 4006-PRACTICE.

**Mentor check:** the April orders are on **10399** (Chapman): 1020742 (PO "JAMES") and 1020846 (PO 163972), each 1 ea `HSE 4W 24 X 6FT 6IN W/ 2424 FL 61 E/E` at $493.68, built from 6.5 ft `HS5K-24` and 2 ea `F4-2424-FL` ($157.36 each). The caller is set up on the other account; confirm which mill and fix the contact with a mentor's OK. Mismatch: the assembly says 4-wire, the hose item says 6-wire; confirm with the Shop Mentor before quoting. "JAMES" in the PO field is a name, not a PO.

## Week 3

### Exercise 3.1 (Day 11): Material Match

For each service, pick a gasket material and thickness, explain in one sentence, and find a stocked sheet item:

1. 3" Class 150 RF, 60 psig, 180°F caustic (white liquor)
2. 6" Class 150 RF, 150 psig saturated steam (366°F)
3. 4" FF cast iron water pump flange, 80 psig ambient water
4. 2" Class 300 RF, 400 psig, 600°F hot oil
5. 3" FRP flange, chlorine dioxide, low pressure

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

Confirm the grade of the green and black sheets with the Shop Mentor before you count on them for steam or oil.

**Mentor check:** (1) EPDM or ePTFE; (2) a steam-rated compressed or filled PTFE sheet after the P×T check, or graphite; (3) full-face neoprene or SBR 1/8"; (4) graphite with insert; (5) ePTFE full face.

### Exercise 3.2 (Day 12): Yield and Price a Real Gasket Order

**Georgia Pacific Pennington (10510)**, contact Cade Baker, order 1040693 (PO 4500998301): 10 ea `GSKT FF 4 150# X .125 9000`.

1. Read the item ID (Reference Sheet O). What is it?
2. What sheet item is it cut from? Find the sheet size and selling unit.
3. Using Reference Sheet K, what are the gasket's OD and ID, and how many bolt holes does it need?
4. How many fit on one sheet (square grid, 0.125" spacing)?
5. How many sheets does the order of 10 use?
6. What else is billed on a cut gasket order besides material?
7. Shadow the Shop Mentor as they nest a full-face job. Compare their yield to yours.

**Mentor check:** a full-face 4" Class 150 gasket, 1/8" Durlon 9000, cut from `GSKT SHT DURLO PTFE` (60" x 60", sold by SI). OD 9.00", ID 4.50", 8 bolt holes. Pitch 9.125": 6 across x 6 down = 36 per sheet, so 10 fit on one sheet. Waterjet labor (`OCI WATER JET LABOR`) goes on the order too.

### Exercise 3.3 (Day 13): Leak Call

**International Paper Selma (10552)**, contact Kevin Pugh (Purchasing): "Your gasket leaked on our 6-inch steam line. We put it in yesterday." (Class 150, 150 psig steam, compressed sheet ring.)

1. Search IP Selma's recent orders for gaskets. Record what you find.
2. Walk through the troubleshooting questions in Reference Sheet M.
3. You learn the installer reused old bolts dry, tightened in a circle in one pass, and put anti-seize on the gasket face.
4. Write the reply: helpful, no blame, with the correct steps and the 8-bolt star sequence.
5. Enter a no-charge replacement in P21PLAY only if your mentor approves. Note IP Selma's terms.

### Simulation 3.4 (Day 14): Six-Request Simulation

Your mentor plays the customers, some on the phone and some at the counter. Work each in P21PLAY.

1. **Montgomery Water Works (10606), phone:** "We need a 3-inch suction hose, 20 feet, female cam and groove on one end and male pipe thread on the other, delivered to our new pump station." Run STAMPED, check stock, create the practice ship-to, add the caller as a contact, and quote.
2. **Georgia Pacific Pennington (10510), Justin Phillips, phone:** "Where are the bellows on PO 4500995240?" (Exercise 2.3.)
3. **Counter walk-in (910):** a customer brings an adapter: one end 9/16-18 with a 37° cone, the other end tapered, 19 threads per inch, about 0.66". Identify it, find it in P21PLAY, and ring it up.
4. **International Paper Prattville (10549), Blake Wynne, phone:** wants an order shipped today. Check credit before you promise anything.
5. **City of Montgomery Garage (10440), counter:** "Who do you have as our contact?" Add them and set document delivery.
6. **Cowin Equipment (10462), counter:** brings in a blown hose: "Same as the one you made us before." Find it in their history and enter the order.

**Mentor check (item 3):** -6 JIC male x 3/8" BSPT male: `7000-06-06 FG`. **(Item 6):** history shows `HB5K-8-0808JFS-0808OBM-7.04` and a 30 ft `HB5K-8-0808JFS-0808JFS-30`; ask the customer to confirm length and ends before you pick one.

Scored on accuracy, customer communication, and data clean-up. Anything you notice that should be fixed in live P21 goes on a list for your mentor.
