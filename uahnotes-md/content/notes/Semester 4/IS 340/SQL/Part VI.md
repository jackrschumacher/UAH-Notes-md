---
title: Part VI
---

### 1. JOIN Basics

- **JOIN** = Querying multiple tables in one `SELECT`
- Most common: Join on **Primary Key** ↔ **Foreign Key**
- Can also do ad-hoc joins (not based on defined relationships)
- Default = **INNER JOIN** (INNER keyword optional)

  **Two main syntaxes:**  

  ```sql
  -- Old style (WHERE clause)
  SELECT ...
  FROM product, vendor
  WHERE product.vendorid = vendor.vendorid;
  
  -- Modern style (recommended)
  SELECT ...
  FROM product JOIN vendor 
    ON product.vendorid = vendor.vendorid;
  ```

  **Important**: Order of tables in FROM does **not** matter for INNER JOIN.  
- ### 2. Cartesian Product (No Join Condition)
- Occurs when you list multiple tables in FROM **without** a join condition
- Every row of first table combines with every row of second table
- Example: 6 products × 2 vendors = 12 rows (very bad for large tables)
- ### 3. How Joins Work Internally
  1. Create Cartesian product
  2. Apply join condition
  3. Keep only rows that satisfy the condition (for INNER JOIN)

- ### 4. Types of Joins

  | Join Type      | Keeps                                             | Use Case                               |
  | -------------- | ------------------------------------------------- | -------------------------------------- |
  | **INNER JOIN** | Only matched rows                                 | Most common                            |
  | **LEFT JOIN**  | All rows from left table + matches from right     | "All from A, optional from B"          |
  | **RIGHT JOIN** | All rows from right table + matches from left     | Rarely used (can be rewritten as LEFT) |
  | **FULL JOIN**  | All rows from both tables (matches + non-matches) | Rare                                   |

  **OUTER** keyword is optional.  

  **LEFT JOIN example** (most useful):  
  ```sql
  SELECT v.vendorname, i.invoicenumber
  FROM vendors v LEFT JOIN invoices i 
    ON v.vendorid = i.vendorid;
  ```
  → Shows all vendors, even those with no invoices (NULLs in invoice columns).  
- ### 5. Table & Column Aliases (Very Important)

  ```sql
  -- Table aliases (AS is optional)
  FROM product p, vendor v
  -- or
  FROM product AS p JOIN vendor AS v ON p.vendorid = v.vendorid
  
  -- Column aliases (for output readability)
  SELECT p.productid AS pid, 
       p.productname AS pname,
       (i.quantity * p.productprice) AS amount
  ```

  **Rules**:  
- Table aliases can be used everywhere (SELECT, WHERE, etc.)
- Column aliases can **only** be used in SELECT and ORDER BY (not in WHERE/GROUP BY/HAVING)
- ### 6. Joining Multiple Tables (>2)
  ```sql
  SELECT t.tid, t.tdate, p.productname, i.quantity
  FROM salestransaction t 
    JOIN includes i ON t.tid = i.tid
    JOIN product p ON i.productid = p.productid
  ORDER BY t.tid;
  ```
- ### 7. Self-Join (Join table to itself)
- Used for hierarchical/unary relationships (e.g., employee-manager, client-referred-by)
- Requires **different aliases** for the two copies of the table

  ```sql
  SELECT c.ccname AS client, r.ccname AS recommender
  FROM corpclient c 
    JOIN corpclient r ON c.ccidreferredby = r.ccid;
  ```
- ### 8. ALTER TABLE
  ```sql
  -- Add column
  ALTER TABLE vendor 
    ADD vendorphonenumber CHAR(12);
  
  -- Drop column
  ALTER TABLE vendor 
    DROP COLUMN vendorphonenumber;
  ```
- ### Key Takeaways for Notes
- Always use **explicit JOIN ... ON** syntax (modern & clearer)
- Understand **Cartesian product** — never forget the join condition!
- LEFT JOIN is the most useful outer join
- Use **aliases** liberally for readability
- Self-joins need two different table aliases
