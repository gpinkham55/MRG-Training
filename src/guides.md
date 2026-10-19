# Section 3: P21 Guides

Work every guide in **P21PLAY**. Labels follow standard Prophet 21; your mentor will point out where our screens differ. The same steps apply whether the customer is on the phone or standing at the counter.

## Guide 3.1: Navigation

**Purpose:** Get comfortable moving around P21 before you touch a customer's order.

**Steps**

1. Log in with **your own user ID**. Every order and quote carries the ID of the person who keyed it.
2. Find the main menu. (Grid pattern on the left bar) Windows are grouped by area: Orders (order entry, RMA entry, transaction inquiry), CRM (customer inquiry, ship-to maintenance, and contact maintenance), and inventory (item master inquiry, item maintenance, inventory reports).
3. Add the windows you'll use every day to your favorites or toolbar: Order Entry, Customer Master Inquiry, Item Master Inquiry, Ship To Maintenance, Contact Maintenance, Order Inquiry, etc.
4. **Search fields:** most ID fields (customer, ship-to, item, contact) open a search window. Type part of the value and tab out, or use the lookup button. Filter on unique attributes (Location ID, Customer Name).
5. **Tabs:** most windows have tabs across the top. The header tab holds the main record; other tabs hold related detail (ship-tos, contacts, history, notes). Click through every tab the first time you open a window.
6. **Multiple windows:** you can keep Customer Inquiry open beside Order Entry. Drill into fields that open in a new tab.
7. **Inquiry vs. Maintenance:** inquiry windows only let you look. Maintenance windows update records. When you only need to look, use the inquiry window so nothing changes by accident.
8. **Save:** changes aren't kept until you save. P21 will prompt to save when you close a window with unsaved changes. 
9. **Notepads:** customers, items, and orders can carry notes. A mandatory note pops up when you open the record. **Always** read notes before clearing them out.

**Common mistakes to avoid**

- Working in live P21 when you meant P21PLAY. Check the system name in the title bar before you start.
- Using a maintenance window "just to look" and saving a change by accident.
- Clicking past a pop-up note without reading it.

## Guide 3.2: Customer Inquiry & Sales History

**Purpose:** Before you quote, enter an order, or answer a question, know who the customer is.

**Steps**

1. Open **Customer Master Inquiry** (F8).
2. Search for the customer by ID, by part of the name, or by phone or city. Use the shortest unique piece ("WESTROCK" beats "WestRock Mill Company").
3. **Confirm the right account.** Many customers have more than one account (Boise Cascade has two, billing to different cities). Know which one you're working with before you proceed.
4. Read the **credit** information: credit limit, credit status (for example normal, COD, hold), and terms.
5. Read the **notepads**: PO required, release numbers, receiving hours, tax exemption, preferred brands.
6. Look at **ship-tos** and **contacts**. Do you know who you're talking to? Are they on the account? Add them now in contact maintenance or when the call is completed.
7. Open **sales history** for the customer. Filter by date range and by item or description. This is the fastest way to find "the same hose as last time" or "what we bought back in April."
8. Open the order from history and read the lines: item IDs, quantities, units, prices, PO.
9. Check **open orders** and **open quotes** before you create anything new. Avoid duplicates.
10. Note the **salesrep** on the account so you know who to loop in.

**Key fields**

| Field | Why you check it |
|---|---|
| Customer ID | Get this wrong and we may not get paid |
| Credit Status | Hold or COD changes what you can promise |
| Open Orders/Open Quotes | Don't duplicate work |
| Notepads | Customer-specific rules you must follow |
| Salesrep | Who owns the relationship |

**Common mistakes to avoid**

- Picking the first account that comes up without checking the bill-to/ship-to.
- Closing notepads without reading the note, then making the mistake the note was created to keep you from making.
- Quoting a price from memory instead of checking history and letting P21 price it.
-  Promising a ship date to a customer on credit hold.## Guide 3.3: Ship-To Maintenance

## Guide 3.3: Ship-to Maintenance 
  
**Purpose:** Get product to the right dock with the right sales tax.

**Before you start:** search the customer's current ship-to list. Most "new" addresses are already on file.

**Steps (new ship-to)**

1. Open **Ship To Maintenance** and enter the customer ID.
2. Enter the ship-to name exactly as it should print on the packing list (for example, "WestRock Mill Company, Demopolis").
3. Enter Address 1, Address 2, City, State, Zip. Use Address 2 for building, gate, or dock.
4. Enter a phone number and a receiving contact if the customer gives one.
5. Set the **tax** fields for the delivery address. Mark it exempt only when a valid certificate is on file with accounting.
6. Set **salesrep** and **territory** to match the account.
7. Set the default **carrier** (our truck, UPS, LTL, will call) and the **freight** terms the customer buys on.
8. Enter **delivery instructions** (receiving hours, call ahead, gate pass, PO on label).
9. Set the preferred location to **110** (Montgomery) unless told otherwise.
10. Save, then reopen the ship-to and confirm every field saved.

**Steps (update a ship-to)**

1. Note the current values in your notebook.
2. If the customer moved to a new physical site, create a new ship-to instead of overwriting. Overwriting rewrites history on old orders.
3. Add a note with the date, your initials, and who asked for the change.
4. Notify Accounting if tax jurisdiction changes.

**Common mistakes to avoid**

- Overwriting an old ship-to with a new location.
- Using a PO box as a delivery address. Several of our accounts bill to a PO box; trucks need a street address.
- Typing a person's name or delivery instructions in the address lines. Names belong in contacts; instructions belong in delivery instructions.
- Creating a duplicate ship-to for an address already on file.

## Guide 3.4: Contact Maintenance

**Purpose:** Every quote, acknowledgment, and invoice reaches the right person.

**Steps (add a contact)**

1. Search first: open **Contact Maintenance** and search by last name, email, and phone.
2. Enter first name, last name, and title.
3. Link the contact to the customer (and to a ship-to if they work at one site).
4. Enter direct phone, extension, mobile, and email. Read the email back letter by letter.
5. Assign the contact's role: AP (invoices, statements), Purchasing (POs, quotes, acknowledgments), Maintenance (technical questions), or others your mentor shows you.
6. Set which documents this contact gets by email.
7. Save, then reopen the customer and confirm the contact shows.

**Steps (edit or retire a contact)**

1. Don't delete a contact who left. Mark them inactive and move their document roles to their replacement.
2. Add a dated note with your initials.
3. If they received invoices, tell accounting.

**Common mistakes to avoid**

- One contact used for everything, so invoices land with a maintenance planner.
- A departed contact still set to receive invoices.
- Generic placeholder contacts ("Invoices," "past due") with no real person behind them. They have their place for AP mailboxes, but the account still needs a named buyer.

## Guide 3.5: Item Inquiry

**Purpose:** Answer "do you have it, where is it, and what does it cost?" fast and correctly.

**Steps**

1. Open **Item Master Inquiry** (F2).
2. Search by item ID, by part of the description, or by a supplier or customer part number. Reference Sheet O explains how our item IDs are built, which makes searching much faster.
3. Read the description and the **unit of measure**. Hose sells by the foot (FT); gasket sheet sells by the square inch (SI); fittings sell each (EA).
4. Check stock at **location 110**: on hand, allocated (already promised to orders), and available.
5. Check **other locations**. TRG locations can transfer stock to us. If we're short, another branch may have it.
6. Check **open purchase orders** for the item: how many are coming and when.
7. Check the **price** for the customer you're helping (price inquiry with their customer ID), not a list price.
8. Look at recent sales of the item to see who buys it and in what quantities.

**Common mistakes to avoid**

- Promising on-hand stock that's already allocated to another order.
- Reading the wrong unit of measure: 100 SI of sheet is about a 10" x 10" piece, not 100 sheets.
- Telling a customer "we don't have it" without checking other TRG locations and open POs.
- Quoting price without the customer ID, so the customer's pricing doesn't apply.

## Guide 3.6: Order Entry

**Purpose:** Turn a request into an order that picks, ships, and bills correctly the first time.

**Header (steps 1 to 12)**

1. Open **Order Entry**.
2. Confirm the **taker** shows your own ID.
3. Enter the **customer ID**. Read any pop-up notes.
4. Pick the **ship-to**. If the address is new, stop. Don't choose a ship-to id - go to the ship-to tab on the OE header and enter the new address information - the new ship-to id will be created when you save the order.
5. Pick the **contact** placing the order. If they aren't in P21, add them here.
6. Enter the **PO number** exactly as given. If the customer requires a PO and the order placer doesn't have one, the order waits.
7. Confirm the **location** is 110.
8. Add an order note for anything picking, shipping, or billing needs to know.

**Lines (steps 13 to 23)**

13. Enter the **item ID**. If the customer gives their own part number, enter it; the cross-reference finds our item. If they give a competitor's number, use item search.
14. Enter **quantity** and confirm the **unit** (EA, FT, SI).
15. Check **available** quantity at 110.
16. Set the **disposition** when stock is short:
    - **B** Backorder: ship what we have, backorder the rest
    - **H** Hold: hold the whole line
    - **S** Special order: non-stock item, creates a purchase need
    - **D** Direct ship: vendor ships to the customer
    - **T** Transfer: pull from another TRG location
    - **C** Cancel

    Confirm our active codes with your mentor.
17. Review the **unit price** and where it came from. Compare to history.
18. **Price overrides** need a reason (quote, contract, or Manager approval). Check the line margin after any change.
19. **Tax overrides** need a certificate on file or accounting's approval. Note the reason on the order.
20. **Freight:** add freight per the freight terms.
21. Read every line back to the customer: item, quantity, price, ship date. At the counter, show them the screen.
22. Check the **order total**. If it looks wrong, it is.
23. **Save and release.** If the customer is on credit hold, the order holds. Tell the customer politely and route to accounting.

**Hose assemblies (step 24)**

24. Enter the assembly item with its hose, both fittings, and any guard or sleeve. Put length and fitting orientation in the line note if the item doesn't carry them. Confirm with the Shop Mentor how assemblies route to the shop, and never promise a same-day assembly without checking the bench.

**Counter sales**

- Walk-in customers without an account go on the **counter cash account (910)**. It's COD: payment at the counter.
- Customers with an account who walk in still go on their own account, with their PO.

**Special handling:** some accounts and contracts have their own order process (for example, rental company hose orders that fall under another TRG location's contract). Route those to your Sales Mentor until you're trained on that process.

**Common mistakes to avoid**

- Wrong unit (FT vs. a reel, EA vs. a pack).
- Backordering when another TRG location has stock.
- Changing a price without checking margin.
- A name, phone number, or "PLEASE UPDATE PO" in the PO field.
- Not telling the customer about a backorder before they leave or hang up.

## Guide 3.7: Quoting

**Purpose:** Give the customer a clear, accurate price they can act on.

**Create a quote (steps 1 to 10)**

1. Open Order Entry and mark it as a **quote** (or open Quote Entry, depending on our menu).
2. Enter customer, ship-to, and contact.
3. Enter the customer's RFQ or reference number.
4. Set the **expiration date**. Ask the Manager for current guidance on standard validity.
5. Enter each item and quantity. Quote exactly what was asked; add alternates as separate, clearly noted lines.
6. For non-stock items, get current vendor cost and lead time before you quote.
7. Enter lead time per line ("Stock," "3 to 5 days," "2 weeks ARO").
8. Review price and margin per line.
9. Add notes: freight terms, validity, assumptions ("Quote assumes 150# RF flanges").
10. **Check the extended total before saving.** A quantity typo once created a quote line worth tens of millions of dollars and distorted the open quote report for months.

**Send and track (steps 11 to 14)**

11. Send the quote to the contact by their preferred method.
12. Set a follow-up: big quotes in 2 business days, others within 5.
13. Review your open quotes weekly. Follow up, revise, or close.
14. Close dead quotes with a reason (lost on price, lead time, or project canceled).

**Convert to an order (steps 15 to 18)**

15. When the customer accepts, open the quote and **convert** it to an order. Don't retype it.
16. Enter the customer's PO.
17. Re-check quantity, price, and expiration. If it expired, re-confirm cost first.
18. Confirm the quote shows as converted.

**Margin math**

- Gross margin % = (Sell − Cost) ÷ Sell × 100.
- Margin is not markup. A 30% markup is only a 23.1% margin.
- Anything below our margin floor needs Manager approval before it goes out.

**Common mistakes to avoid**

- No expiration date.
- Retyping a quote as an order, leaving the quote open.
- Quoting non-stock items from old cost.
- Quoting a hose assembly without all seven STAMPED answers.

## Guide 3.8: Order Inquiry & Follow-Up

**Purpose:** Answer "where's my order?" with facts, and fix what's stuck.

**Steps**

1. Get the customer's **PO** or our order number. If they have neither, search the customer's open orders by date and item.
2. Open **Order Inquiry** and read each line: shipped, open, and the disposition (B, S, T, H).
3. For backordered or special-order lines, check the **purchase order** behind it: vendor, promise date, and quantity received.
4. If the PO shows **received** but the line hasn't shipped, the product is probably in the building. Ask the warehouse to find it and get it moving.
5. Check **other TRG locations** for stock you could transfer.
6. Tell the customer what you found and when they'll hear from you next. Then call back when you said you would.
7. Add a dated note to the order.

**Common mistakes to avoid**

- Guessing ("it's probably on a truck").
- Sending the customer to the vendor. They bought it from us.
- Cancelling and re-entering an order, which breaks the PO match and the history.
