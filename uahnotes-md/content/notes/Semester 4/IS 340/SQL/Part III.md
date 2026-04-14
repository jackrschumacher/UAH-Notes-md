---
title: Part III
---

- ## DISTINCT
Eliminates duplicate rows from query results. Placed immediately after `SELECT`.  
  
  ```sql
-- Without DISTINCT (returns duplicates)
SELECT vendorid FROM product;

-- With DISTINCT (unique values only)
SELECT DISTINCT vendorid FROM product;

-- Multiple columns (combination must be unique)
SELECT DISTINCT VendorCity, VendorState FROM Vendors;
  ```
---
- ## ORDER BY
  Sorts query results by one or more columns or expressions.  
  
  ```sql
  -- Ascending (default)
  SELECT productid, productname, categoryid, productprice
  FROM product
  WHERE categoryid = 'FW'
  ORDER BY productprice;
  
  -- Descending
  ORDER BY productprice DESC;
  
  -- Multiple columns (sort by categoryid first, then productprice within each category)
  ORDER BY categoryid, productprice;
  ```

---
- ## TOP Clause
  Returns a limited number of rows from the top of the result set. Best used with `ORDER BY`.  
  
  ```sql
  -- Top N rows
  SELECT TOP 5 VendorID, InvoiceTotal
  FROM Invoices
  ORDER BY InvoiceTotal DESC;
  
  -- Top N percent of rows
  SELECT TOP 5 PERCENT VendorID, InvoiceTotal
  FROM Invoices
  ORDER BY InvoiceTotal DESC;
  
  -- Top N WITH TIES (includes extra rows that tie with the last row)
  SELECT TOP 5 WITH TIES VendorID, InvoiceDate
  FROM Invoices
  ORDER BY InvoiceDate ASC;
  ```
  
---
- ## OFFSET / FETCH (Pagination)
  Returns a subset of rows starting at any point in the sorted result — unlike `TOP`, which always starts from the beginning.  
- `OFFSET` → how many rows to **skip**
- `FETCH` → how many rows to **return** after skipping
- Omitting `FETCH` returns all remaining rows
  
  ```sql
  -- First 5 rows
  SELECT VendorID, InvoiceTotal
  FROM Invoices
  ORDER BY InvoiceTotal DESC
  OFFSET 0 ROWS
  FETCH FIRST 5 ROWS ONLY;
  
  -- Rows 11 through 20
  SELECT VendorName, VendorCity, VendorState, VendorZipCode
  FROM Vendors
  WHERE VendorState = 'CA'
  ORDER BY VendorCity
  OFFSET 10 ROWS
  FETCH NEXT 10 ROWS ONLY;
  ```
  
---
- ## LIKE
  Pattern matching for partial string searches. Used in `WHERE` clause.  
- ### Wildcard Symbols
  | Symbol   | Meaning                                                    |
  | -------- | ---------------------------------------------------------- |
  | `%`      | Any string of zero or more characters                      |
  | `_`      | Any single character                                       |
  | `[abc]`  | Any single character listed in brackets                    |
  | `[a-z]`  | Any single character in the given range                    |
  | `[^abc]` | Any single character **not** in the list (caret = exclude) |
- ### Examples (ZagiMore DB)
  ```sql
  -- Product name contains 'Boot' anywhere
  WHERE productname LIKE '%Boot%';
  
  -- Product name ends with 'a'
  WHERE productname LIKE '%a';
  
  -- Store zipcode does NOT end with '0'
  WHERE storezip NOT LIKE '%0';
  ```
- ### Examples (AP Database)
  ```sql
  -- Cities starting with 'SAN' (e.g. "San Diego", "Santa Ana")
  WHERE VendorCity LIKE 'SAN%';
  
  -- Name: 'COMPU' + any one char + 'ER' + anything (e.g. "Compuserve", "Computerworld")
  WHERE VendorName LIKE 'COMPU_ER%';
  
  -- Last name is "Damien" or "Damion" (5th char is E or O)
  WHERE VendorContactLName LIKE 'DAMI[EO]N';
  
  -- State starts with N, second char is A through J (e.g. "NC", "NJ" — not "NV" or "NY")
  WHERE VendorState LIKE 'N[A-J]';
  
  -- State starts with N but second char is NOT K through Y
  WHERE VendorState LIKE 'N[^K-Y]';
  
  -- Zip code does NOT start with digits 1–9
  WHERE VendorZipCode NOT LIKE '[1-9]%';
  ```
  
---
- ## SQL Clause Execution Order
  Clauses are **written** in one order but **executed** in a different order.  
  
  | Execution Step | Clause                                  |
  | -------------- | --------------------------------------- |
  | 1              | `FROM`                                  |
  | 2              | `WHERE`                                 |
  | 3              | `GROUP BY`                              |
  | 4              | `SELECT` (aggregate functions run here) |
  | 5              | `HAVING`                                |
  | 6              | `ORDER BY`                              |
- Because aggregates execute at step 4, they **can** be used in `HAVING` (step 5) but **cannot** be used in `WHERE` (step 2)
- Memory tip: **SFW GHO** (41235 for execution order)