# SECTION 2: Module Documentation & Instructional Guides

## Part A: P21 Workflow Guides

### Guide 2.1: Customer Lookup & Navigation

**Purpose:** Before quoting, entering an order, or answering a question, know who you're talking to, what they're allowed to buy on, and how they're priced.

**Steps**

1. Open **Customer Master Inquiry** (or Customer Maintenance in view mode if your role allows).
2. In the **Customer ID** field, search one of three ways:
   - Exact Customer ID, then Tab.
   - Partial customer name, then Tab or the lookup button. Use the shortest unique piece ("WESTROCK" beats "WestRock Mahrt Mill").
   - Phone number or city using the search window's filter columns.
3. Confirm the right account. Many mills have several accounts (by mill, by department, by bill-to). Check the **bill-to address** and the **ship-to list** before choosing.
4. Read the **Credit** information:
   - **Credit Limit** and **Credit Limit Used / Available**
   - **Credit Status** (for example: normal, COD, Cash Only, Hold)
   - **Terms ID** (Net 30, 1% 10 Net 30, COD, Credit Card)
5. Read the **Notepads**. Notes marked mandatory pop up in Order Entry. Look for: PO required, release numbers required, receiving hours restrictions, tax exemption details, preferred brands.
6. Review **Order History** (Sales History / Order Inquiry tab): last 10 orders, items bought, prices paid, PO numbers used. This is the fastest way to find "the same hose as last time."
7. Review **Open Orders** and **Open Quotes** for this customer before creating new ones. Avoid duplicates.
8. Review the **Pricing** setup: pricing library or price page assignment, any contract pricing, and **Customer Part Numbers** (their number mapped to our Item ID).
9. Check the **Salesrep** and **inside sales owner** assigned to the account so you know who to loop in.

**Key fields to know**

| Field | Why you check it |
|---|---|
| Customer ID | The unique account key; every order and quote hangs on it |
| Credit Status | Hold or COD changes what you can promise |
| Terms ID | Tells you how the customer pays |
| Notepads | Customer-specific rules you must follow |
| Pricing Library | Controls the price P21 offers automatically |
| Customer Part No. | Lets you enter their part number and land on our item |
| Salesrep ID | Who owns the relationship |

**Common mistakes to avoid**

- Picking the first account that pops up without confirming the bill-to. Mills often have parallel accounts.
- Skipping notepads, then missing a required release number.
- Quoting a price from memory instead of letting P21 price it, then checking it.
- Creating a new customer when one already sits in P21 under a slightly different spelling. Search by phone and city before asking for a new account.
- Promising a ship date to a customer on credit hold.

---

### Guide 2.2: Ship-To Creation & Maintenance

**Purpose:** Get product delivered to the right dock with the right tax.

**Before you start:** Search the customer's current ship-to list. Most "new" addresses turn out to be a building or gate already on file.

**Steps (new ship-to)**

1. Open **Ship To Maintenance**.
2. Enter the **Customer ID**. Leave **Ship To ID** blank for P21 to assign the next number (or follow MR&G's numbering convention if your trainer shows one).
3. Enter the **Ship To description/name line** exactly as the customer wants it on the packing list (for example, "IP Prattville, Storeroom Dock 3").
4. Enter **Address 1, Address 2, City, State, Zip**. Use Address 2 for building, gate, or dock. Verify the zip against USPS lookup.
5. Enter **Phone** and a receiving **Contact** if the customer gives one.
6. Set **Tax Group ID** based on the delivery address (state, county, city jurisdiction). Set **Taxable** to Yes unless a valid exemption certificate is on file.
7. If exempt, enter the **Exemption Number** and confirm a copy of the certificate is on file with accounting. No certificate, no exemption.
8. Set **Salesrep ID** and **Territory** to match the account owner.
9. Set **Default Carrier / Ship Via** (our truck, UPS Ground, LTL carrier, customer pickup).
10. Set **Freight Code** (Prepaid & Add, Prepaid, Collect, Third Party, Will Call) per the customer agreement.
11. Enter **Delivery/Shipping Instructions** (receiving window, PO must be on label, call before delivery, gate pass required).
12. Set **Preferred/Default Location** to 110 (Montgomery) unless instructed otherwise.
13. Save. Reopen the ship-to and confirm every field saved.

**Steps (update a ship-to)**

1. Open the ship-to and note the current values in your notebook.
2. Make the change. If the address changes to a new physical site, create a new ship-to instead of overwriting; overwriting rewrites history on old orders.
3. Add a notepad entry with the date, your initials, and who requested the change.
4. If tax group changes, alert accounting.

**Common mistakes to avoid**

- Overwriting an old ship-to with a new location. History and tax records get scrambled.
- Using the bill-to tax setup for a ship-to in another county or state.
- Marking a ship-to exempt on a verbal promise.
- Typing delivery instructions in the address lines, which then print on labels and confuse carriers.
- Creating duplicates (same address, different ID). Search first.

---

### Guide 2.3: Order Entry

**Purpose:** Turn a customer request into an accurate order that picks, ships, and bills correctly the first time.

**Header (steps 1 to 12)**

1. Open **Order Entry**.
2. Confirm your **Taker** shows your own ID.
3. Enter **Customer ID**. Read any mandatory notepad pop-ups.
4. Select **Ship To ID**. If the address is new, stop and run Guide 2.2 first.
5. Select **Contact ID** (who placed the order). If the caller isn't in P21, add them per Guide 2.5 now.
6. Enter **PO Number** exactly as the customer gives it. If the customer requires a PO and has none, the order waits.
7. Enter any **Release Number / Job Number** fields the customer requires.
8. Confirm **Location** = 110.
9. Set **Requested Date** (when the customer needs it) and **Promise Date** if your configuration uses it.
10. Confirm **Carrier / Ship Via** and **Freight Code** pulled from the ship-to; change only if the customer asks for this order.
11. Confirm **Terms** pulled correctly.
12. Add an **order-level note** for anything picking, shipping, or billing needs to know.

**Lines (steps 13 to 22)**

13. Enter **Item ID**. If the customer gives their own part number, enter it; P21 resolves it through **Customer Part Number** cross-reference. If they give a competitor or manufacturer number, use **Item Search** with the number in the description or alternate code columns.
14. Enter **Quantity Ordered** and confirm **Unit of Measure** (EA, FT, RL, SH). Hose sold by the foot vs by the reel is a classic error.
15. Check **Quantity Available** at location 110.
16. Set **Disposition** when stock is short. Common P21 dispositions:
    - **B** Backorder: ship what we have, backorder the rest
    - **H** Hold: hold the whole line
    - **S** Special Order: non-stock item, creates a purchase need
    - **D** Direct Ship: vendor ships straight to the customer
    - **T** Transfer: pull from another TRG location
    - **C** Cancel
    Confirm MR&G's active codes with your mentor.
17. Review **Unit Price**. Look at where the price came from (pricing service/price inquiry). Compare to order history.
18. **Price overrides:** Change Unit Price only with a reason (quote number, contract, manager approval). Check the line **Gross Profit / Margin %** after the change. If margin drops below MR&G's floor, get approval from your mentor or Greg before saving.
19. **Tax overrides:** Change the order or line taxable status only with a certificate on file or accounting approval. Note the reason on the order.
20. **Freight:** Add freight lines per freight code (Prepaid & Add gets a freight charge; Prepaid does not; Collect and Third Party need the account number in the shipping instructions).
21. Review the order total. Read every line out loud back to the customer for phone orders: item, quantity, price, ship date.
22. **Release:** Save. If the customer is on credit hold, the order holds; tell the customer and notify accounting. Otherwise, confirm the pick ticket prints (or prints in the next pick ticket run) for location 110.

**Hose assemblies (step 23)**

23. Enter the assembly item (or build the assembly using MR&G's assembly item setup) with hose, both fittings, and any protective sleeve or guard. Enter the overall length and fitting orientation in the line note if not built into the item. Confirm with Eric Jones how assemblies route to the shop (production order or assembly ticket). Never promise same-day assemblies without checking the bench queue.

**Special account handling:** United Rentals hose orders tied to the Bay Area contract follow their own MR&G process. Route those to your mentor until trained on that SOP.

**Common mistakes to avoid**

- Wrong unit of measure (FT vs RL, EA vs PK).
- Backordering when another TRG location has stock (check transfer option first).
- Changing price without checking margin.
- Leaving the PO field blank for a PO-required customer; the invoice gets rejected and payment stalls.
- Entering a customer part number into the quantity field (it happens, and it creates absurd order totals). Always glance at the extended total.
- Not telling the customer about a backorder before they hang up.

---

### Guide 2.4: Quoting

**Purpose:** Give the customer a clear, accurate, profitable price they can act on.

**Create a quote (steps 1 to 10)**

1. Open **Order Entry** and mark the document as a **Quote** (or open Quote Entry, depending on MR&G's menu).
2. Enter **Customer ID**, **Ship To ID**, and **Contact ID** (the requester).
3. Enter the customer's **RFQ number or reference** in the PO/Reference field.
4. Set **Quote Expiration Date**. MR&G default guidance: 30 days for stock items; shorter for metals, PTFE, and anything tied to volatile supplier pricing. Confirm current guidance with Greg.
5. Enter each **Item ID** and **Quantity**. Quote exactly what was asked; add alternates as separate, clearly noted lines.
6. For non-stock items, get current vendor cost and lead time before quoting. Note the source (vendor quote number, date).
7. Enter **Lead Time / Ship Date** per line ("Stock," "3 to 5 days," "2 weeks ARO").
8. Review **Unit Price** and **Margin %** per line (see margin analysis below).
9. Add quote notes: freight terms, validity, any assumptions ("Quote assumes 150# RF flanges, 1/16" thickness").
10. **Check the extended total before saving.** A quantity typo once created a quote line worth tens of millions of dollars in MR&G's system and distorted the open quote pipeline for months. Read the total; if it looks wrong, it is.

**Send and track (steps 11 to 14)**

11. Save and send the quote using the contact's document delivery preference (email PDF).
12. Log a follow-up: high-value quotes in 2 business days, all others within 5.
13. Run the **open quote report / quote inquiry** for your accounts weekly. Follow up, revise, or close.
14. Close or cancel dead quotes with a reason (lost to price, lost to lead time, project canceled). Clean data makes the pipeline report trustworthy.

**Convert to an order (steps 15 to 18)**

15. When the customer accepts, open the quote and use the **convert quote to order** function (your trainer shows the exact menu path on MR&G's setup). Do not retype the quote as a new order; you lose the link and the quote stays open.
16. Enter the customer's **PO number** on the new order.
17. Re-check quantity, price, and expiration. If the quote expired, re-confirm cost before honoring.
18. Confirm the quote shows as converted/closed.

**Margin analysis**

- **Gross margin % = (Sell − Cost) ÷ Sell × 100.**
- Know which cost P21 shows (moving average, replacement, or vendor cost) and use replacement cost on items with recent price increases.
- Example: Cost $42.00, sell $60.00. Margin = (60 − 42) ÷ 60 = 30%.
- Do not confuse margin with markup. A 30% markup on $42.00 is $54.60, which is only a 23.1% margin.
- Anything below MR&G's margin floor needs approval before the quote goes out.

**Common mistakes to avoid**

- No expiration date, then honoring a year-old price after a cost increase.
- Retyping instead of converting, which leaves orphaned open quotes.
- Quoting non-stock items from old cost.
- Leaving quotes open forever. Dead quotes make the pipeline look bigger than it is.
- Quoting a hose assembly without confirming all STAMPED details.

---

### Guide 2.5: Contact Maintenance

**Purpose:** Every customer call, quote, acknowledgment, and invoice reaches the right human. This guide aligns with MR&G's Contact Maintenance SOP.

**Steps (add a contact)**

1. Search first: open **Contact Maintenance** and search by last name, email, and phone. Duplicates cause missed invoices.
2. Enter **First Name** and **Last Name**, **Title**.
3. **Link** the contact to the **Customer ID** (and ship-to, if the contact works at a specific site).
4. Enter **Direct Phone**, **Extension**, **Mobile**, and **Email Address**. Confirm spelling by reading the email back letter by letter.
5. Assign the **role tag** (contact class or user-defined field on MR&G's setup):
   - **AP** (receives invoices, statements)
   - **Purchasing** (sends POs, receives quotes and acknowledgments)
   - **Maintenance** (technical questions, end user)
   - Others your trainer shows (Storeroom, Engineering)
6. Set **document delivery preferences**: which documents go to this contact by email (quotes, order acknowledgments, invoices, statements).
7. Add a contact note if relevant ("Prefers text for pickup notices").
8. Save. Reopen the customer and confirm the contact appears.

**Steps (edit or retire a contact)**

1. If a contact leaves the company, do not delete. Mark inactive per MR&G practice and move their document delivery roles to the replacement contact.
2. Add a note with date and your initials.
3. If the departing contact received invoices, alert accounting.

**Common mistakes to avoid**

- One contact used for everything, so invoices land in a maintenance planner's inbox.
- Leaving a departed contact active as the invoice recipient.
- Typos in email addresses (always read back).
- Creating a second record for a contact already in P21.

---
