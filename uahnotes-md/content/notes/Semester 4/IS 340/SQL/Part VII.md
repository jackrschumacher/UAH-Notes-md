---
title: Part VII
---

### 1. INSERT Statements

**Single Row**  

  ```sql
-- Without column list (values must match exact column order)
INSERT INTO InvoiceCopy 
VALUES (97, '456789', '2020-03-01', 8344.50, 0, 0, 1, '2020-03-31', NULL);

-- With column list (recommended - more flexible)
INSERT INTO InvoiceCopy (VendorID, InvoiceNumber, InvoiceTotal, ...)
VALUES (97, '456789', 8344.50, ...);
  ```
**Multiple Rows**  

  ```sql
INSERT INTO InvoiceCopy VALUES 
  (row1 values),
  (row2 values),
  (row3 values);
  ```
**Insert from Another Table (Very Useful)**  

  ```sql
INSERT INTO InvoiceArchive
SELECT * 
FROM Invoices 
WHERE InvoiceTotal - PaymentTotal - CreditTotal = 0;
  ```
- ### 2. UPDATE Statement
  
  ```sql
  UPDATE table_name
  SET column1 = value1, 
    column2 = value2
  WHERE condition;     -- ALWAYS use WHERE!
  ```
  
  **Examples:**  
- Update single row: `WHERE productid = '7×7'`
- Update multiple rows: `WHERE vendorid = 'MK'`
- Set all rows (dangerous): omit WHERE
- ### 3. DELETE Statement
  
  ```sql
  DELETE FROM table_name
  WHERE condition;
  ```
  
  **Tip**: Always include `WHERE` — without it, **all rows** will be deleted.  
- ### 4. Views (Virtual Tables)
- A saved `SELECT` query
- Does **not** store data physically
- Data is generated fresh every time the view is queried
- Can be used like a regular table in `SELECT`
  
  **Create View**  
  
  ```sql
  CREATE VIEW products_more_than_3_sold AS
  SELECT productid, productname, productprice
  FROM product
  WHERE productid IN (
    SELECT productid 
    FROM includes 
    GROUP BY productid 
    HAVING SUM(quantity) > 3
  );
  ```
  
  **Use View**  
  
  ```sql
  SELECT * FROM products_more_than_3_sold;
  ```
  
  **Drop View**  
  
  ```sql
  DROP VIEW view_name;
  ```
  
  **Views can include**:  
- Joins
- Aggregates (GROUP BY, HAVING)
- TOP, ORDER BY (in some DBMS)
- ### 5. SET Operators (Combine results of two SELECTs)
  
  Must be **union compatible** (same number of columns + matching data types)  
  
  | Operator           | Description                           | Duplicates |
  | ------------------ | ------------------------------------- | ---------- |
  | **UNION**          | All rows from both queries            | Removed    |
  | **INTERSECT**      | Only rows common in both queries      | Removed    |
  | **MINUS / EXCEPT** | Rows in first query but not in second | Removed    |
  
  **Example:**  
  
  ```sql
  SELECT * FROM products_more_than_3_sold
  UNION
  SELECT * FROM products_in_multiple_trnsc;
  ```
- ### 6. ALTER TABLE
  
  ```sql
  -- Add column
  ALTER TABLE vendor 
  ADD vendorphonenumber CHAR(11);
  
  -- Drop column
  ALTER TABLE vendor 
  DROP COLUMN vendorphonenumber;
  
  -- Add constraint
  ALTER TABLE manager
  ADD CONSTRAINT fk_residesin 
  FOREIGN KEY (mresbuildingid) REFERENCES building(buildingid);
  ```
- ### 7. Constraint Management (Key Points)
- Constraints enforce data integrity (PK, FK, UNIQUE, CHECK)
- Foreign keys can be added **after** tables are created using `ALTER TABLE`
- To drop related tables with FK constraints:
	1. Drop the FK constraint first, or
	2. Drop child table before parent table  
  

**Common Pattern for adding FK later:**

```sql
ALTER TABLE child_table
ADD CONSTRAINT fk_name
FOREIGN KEY (col) REFERENCES parent_table(pk_col);
```

- ### Key Takeaways
- Always use column lists in `INSERT` when possible
- **Never** run `UPDATE` or `DELETE` without `WHERE`
- Views = reusable saved queries (great for complex reports)
- Use `UNION`, `INTERSECT`, `MINUS` to combine query results
- Use `ALTER TABLE` to evolve table structure after creation
