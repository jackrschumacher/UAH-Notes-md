---
title: Part IV
---

- ## Aggregate Functions
  Used to answer managerial summary questions (totals, averages, counts, etc.).  
  
  | Function | Description                | Works On              |
  | -------- | -------------------------- | --------------------- |
  | `COUNT`  | Number of rows selected    | Any type              |
  | `SUM`    | Total of non-null values   | Numeric only          |
  | `AVG`    | Average of non-null values | Numeric only          |
  | `MIN`    | Lowest non-null value      | Numeric, date, string |
  | `MAX`    | Highest non-null value     | Numeric, date, string |
- ### Key Rules
- `AVG`, `SUM`, `MIN`, `MAX` require a **column name** as argument — e.g., `AVG(productprice)`
- `COUNT` can use `*` or a column name as argument
- All aggregate functions **ignore NULL values** except `COUNT(*)`
- Aggregate functions **cannot be used in a WHERE clause** (they execute at step 4, after WHERE at step 2)
- When aggregates are in `SELECT`, individual non-aggregated columns must also appear in `GROUP BY`
- Use `DISTINCT` inside aggregate to count/sum only unique values
- ### Examples (ZagiMore DB)
  ```sql
  -- Average product price
  SELECT AVG(productprice) FROM product;
  
  -- Total number of products
  SELECT COUNT(*) FROM product;
  
  -- Number of distinct vendors in product table
  SELECT COUNT(DISTINCT vendorid) FROM product;
  
  -- Stats for CP category
  SELECT COUNT(*) AS "count*",
       AVG(productprice) AS "AVGproductprice",
       MIN(productprice) AS "MINproductprice",
       MAX(productprice) AS "MAXproductprice"
  FROM product
  WHERE categoryid = 'CP';
  ```
- ### Examples (AP Database)
  ```sql
  -- Count unpaid invoices and total amount due
  SELECT COUNT(*) AS NumberOfInvoices,
       SUM(InvoiceTotal - PaymentTotal - CreditTotal) AS TotalDue
  FROM Invoices
  WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;
  
  -- Count distinct vs all vendors for invoices after 7/1/2019
  SELECT COUNT(DISTINCT VendorID) AS DistinctNumberOfVendors,
       COUNT(VendorID) AS EveryVendorInTable,
       AVG(InvoiceTotal) AS AverageInvoiceAmount,
       SUM(InvoiceTotal) AS TotalInvoiceAmount
  FROM Invoices
  WHERE InvoiceDate > '2019-07-01';
  
  -- Label + count + avg + sum in one query
  SELECT 'After 7/1/2019' AS SelectionDate,
       COUNT(*) AS NumberOfInvoices,
       AVG(InvoiceTotal) AS AverageInvoiceAmount,
       SUM(InvoiceTotal) AS TotalInvoiceAmount
  FROM Invoices
  WHERE InvoiceDate > '2019-07-01';
  
  -- MIN/MAX on non-numeric (alphabetical)
  SELECT MIN(VendorName) AS FirstVendor,
       MAX(VendorName) AS LastVendor,
       COUNT(VendorName) AS NumberOfVendors
  FROM Vendors;
  ```
  
---
- ## GROUP BY
  Groups rows that share the same value in specified column(s), then applies aggregate functions to each group.  
- ### Rules
- Any non-aggregated column in `SELECT` **must also appear** in `GROUP BY`
- Multiple `GROUP BY` columns form a hierarchy (each is subordinate to the previous)
- `WHERE` filters rows **before** grouping; `GROUP BY` then groups the remaining rows
- ### Examples (ZagiMore DB)
  ```sql
  -- Q16: Per vendor — product count and avg price
  SELECT vendorid,
       COUNT(*) AS "No of Products by Vendor",
       AVG(productprice) AS "Avg Product Price"
  FROM product
  GROUP BY vendorid;
  
  -- Q18: Per vendor — count of products priced >= $100
  SELECT vendorid, COUNT(*)
  FROM product
  WHERE productprice >= 100
  GROUP BY vendorid;
  
  -- Q19: Group by vendor AND category
  SELECT vendorid, categoryid, COUNT(*), AVG(productprice)
  FROM product
  GROUP BY vendorid, categoryid;
  
  -- Q20: Per product — total units sold (from includes table)
  SELECT productid, SUM(quantity) AS "Sum(Quantity)"
  FROM includes
  GROUP BY productid;
  
  -- Q21: Per product — number of transactions it appeared in
  SELECT productid, COUNT(*) AS "Count*"
  FROM includes
  GROUP BY productid;
  ```
- ### Common Error
  ```sql
  -- INVALID — vendorid in SELECT but not in GROUP BY
  SELECT vendorid, COUNT(*), AVG(productprice)
  FROM product;
  -- Fix: add GROUP BY vendorid
  ```
  
---
- ## HAVING
  Filters **groups** after `GROUP BY` runs. The `WHERE` equivalent for aggregated results.  
- ### WHERE vs. HAVING
  |                      | WHERE               | HAVING               |
  | -------------------- | ------------------- | -------------------- |
  | Filters              | Individual rows     | Groups (mini-tables) |
  | Runs at step         | 2 (before grouping) | 5 (after grouping)   |
  | Supports aggregates? | ❌ No                | ✅ Yes                |
- ### Rules
- A query with `HAVING` **must** also have `GROUP BY`
- `HAVING` can reference aggregate functions; `WHERE` cannot
- `WHERE` and `HAVING` can appear in the **same query** — `WHERE` filters rows first, then `GROUP BY` groups them, then `HAVING` filters the groups
- ### Examples (ZagiMore DB)
  ```sql
  -- Q22: Groups (vendor+category) with more than 1 product
  SELECT vendorid, categoryid, COUNT(*), AVG(productprice)
  FROM product
  GROUP BY vendorid, categoryid
  HAVING COUNT(*) > 1;
  
  -- Q23: WHERE + HAVING together — products >= $50, groups with > 1
  SELECT vendorid, categoryid, COUNT(*), AVG(productprice)
  FROM product
  WHERE productprice >= 50
  GROUP BY vendorid, categoryid
  HAVING COUNT(*) > 1;
  
  -- Q24: Products where total qty sold > 3
  SELECT productid, SUM(quantity)
  FROM includes
  GROUP BY productid
  HAVING SUM(quantity) > 3;
  
  -- Q25: Products sold in more than 1 transaction
  SELECT productid, COUNT(*)
  FROM includes
  GROUP BY productid
  HAVING COUNT(*) > 1;
  
  -- Q26: Just the ProductID where total qty sold > 3
  SELECT productid
  FROM includes
  GROUP BY productid
  HAVING SUM(quantity) > 3;
  
  -- Q27: Just the ProductID sold in > 1 transaction
  SELECT productid
  FROM includes
  GROUP BY productid
  HAVING COUNT(*) > 1;
  ```
- ### Example (AP Database)
  ```sql
  -- Avg invoice total per vendor, only vendors with avg > $2000, sorted desc
  SELECT VendorID, AVG(InvoiceTotal) AS AverageInvoiceAmount
  FROM Invoices
  GROUP BY VendorID
  HAVING AVG(InvoiceTotal) > 2000
  ORDER BY AverageInvoiceAmount DESC;
  
  -- NOTE: This is INVALID — cannot use aggregate in WHERE
  -- WHERE AVG(InvoiceTotal) > 2000  ← causes an error
  ```
  
---
- ## SQL Clause Execution Order (Full Review)
  | Step | Clause     | Notes                                          |
  | ---- | ---------- | ---------------------------------------------- |
  | 1    | `FROM`     | Always executes first                          |
  | 2    | `WHERE`    | Filters individual rows; no aggregates allowed |
  | 3    | `GROUP BY` | Groups remaining rows                          |
  | 4    | `SELECT`   | Aggregate functions run here                   |
  | 5    | `HAVING`   | Filters groups; aggregates allowed             |
  | 6    | `ORDER BY` | Sorts final result                             |
  
  Memory tip: **SFW GHO** (execution order: 4-1-2-3-5-6)  
  
---
- ## Standard SQL Rules Summary
- `GROUP BY` expressions can only contain columns listed in `SELECT`
- Columns in a `HAVING` expression must be either an argument to an aggregate function or listed in `SELECT` / `GROUP BY`