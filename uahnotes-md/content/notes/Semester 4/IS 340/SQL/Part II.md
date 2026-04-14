---
title: Part II
---

- ## INSERT INTO
  

Used to populate tables with data after they are created.  
- ### Rules
- Values follow the same column order as the `CREATE TABLE` statement
- Character types (`CHAR`, `VARCHAR`) → wrap values in **single quotes**
- Numeric types (`INT`, `NUMERIC`) → no quotes
- Non-optional (NOT NULL) columns must always have a value
- ### Syntax
  ```sql
  INSERT INTO table_name VALUES ('X1', 'X2', ...);
  ```
- ### ZAGI Example – Inserting Data
  ```sql
  INSERT INTO vendor VALUES ('PG', 'Pacifica Gear');
  INSERT INTO vendor VALUES ('MK', 'Mountain King');
  
  INSERT INTO category VALUES ('CP', 'Camping');
  INSERT INTO category VALUES ('FW', 'Footwear');
  
  INSERT INTO product VALUES ('1X1', 'Zzz Bag',    100, 'PG', 'CP');
  INSERT INTO product VALUES ('2X2', 'Easy Boot',   70, 'MK', 'FW');
  INSERT INTO product VALUES ('3X3', 'Cosy Sock',   15, 'MK', 'FW');
  INSERT INTO product VALUES ('4X4', 'Dura Boot',   90, 'PG', 'FW');
  INSERT INTO product VALUES ('5X5', 'Tiny Tent',  150, 'MK', 'CP');
  INSERT INTO product VALUES ('6X6', 'Biggy Tent', 250, 'MK', 'CP');
  
  INSERT INTO region VALUES ('C', 'Chicagoland');
  INSERT INTO region VALUES ('T', 'Tristate');
  
  INSERT INTO store VALUES ('S1', '60600', 'C');
  INSERT INTO store VALUES ('S2', '60605', 'C');
  INSERT INTO store VALUES ('S3', '35400', 'T');
  
  INSERT INTO customer VALUES ('1-2-333', 'Tina', '60137');
  INSERT INTO customer VALUES ('2-3-444', 'Tony', '60611');
  INSERT INTO customer VALUES ('3-4-555', 'Pam',  '35401');
  
  INSERT INTO salestransaction VALUES ('T111', '1-2-333', 'S1', '01/Jan/2020');
  INSERT INTO salestransaction VALUES ('T222', '2-3-444', 'S2', '01/Jan/2020');
  INSERT INTO salestransaction VALUES ('T333', '1-2-333', 'S3', '02/Jan/2020');
  INSERT INTO salestransaction VALUES ('T444', '3-4-555', 'S3', '02/Jan/2020');
  INSERT INTO salestransaction VALUES ('T555', '2-3-444', 'S3', '02/Jan/2020');
  
  INSERT INTO includes VALUES ('1X1', 'T111', 1);
  INSERT INTO includes VALUES ('2X2', 'T222', 1);
  -- etc.
  ```
- ### Data Loading Sequence (Referential Integrity)
- Tables **without** foreign keys must be loaded **first**
- Loading order for ZAGI:
	1. `region`, `vendor`, `category`, `customer`
	2. `store`, `product`
	3. `salestransaction`
	4. `includes`

- Raw data reference: textbook p. 145, Fig. 5.1c
  
---
- ## DROP TABLE
  
  Permanently removes a table and all its data. **Cannot be undone.**  
- ### Rules
- Drop in **reverse** of the loading sequence (child tables before parent tables)
- Tables with FKs pointing to another table must be dropped before that table
- ### Valid DROP Sequence for ZAGI
  ```sql
  DROP TABLE includes;
  DROP TABLE salestransaction;
  DROP TABLE store;
  DROP TABLE product;
  DROP TABLE vendor;
  DROP TABLE region;
  DROP TABLE category;
  DROP TABLE customer;
  ```
  
---
- ## SELECT
  
  Used to retrieve data from tables. Most commonly issued SQL statement.  
- ### Full Clause Order
  ```sql
  SELECT   <columns, expressions>
  FROM     <tables>
  WHERE    <row condition>
  GROUP BY <grouping columns>
  HAVING   <group condition>
  ORDER BY <sort columns>;
  ```
- ### Basic Retrieval
  ```sql
  -- All columns
  SELECT * FROM product;
  
  -- Specific columns
  SELECT productid, productprice FROM product;
  
  -- Custom column order
  SELECT productname, productid, vendorid, categoryid, productprice FROM product;
  ```
- ### Derived / Calculated Columns
  ```sql
  -- Price with 10% increase
  SELECT productid, productprice, productprice * 1.1 FROM product;
  
  -- With alias
  SELECT productid, productprice, productprice * 1.1 AS "productprice*1.1" FROM product;
  
  -- Calculated balance
  SELECT InvoiceTotal, PaymentTotal, CreditTotal,
       InvoiceTotal - PaymentTotal - CreditTotal AS BalanceDue
  FROM Invoices;
  ```
- ### Arithmetic Operator Precedence
	1. `*` Multiplication
	2. `/` Division
	3. `%` Modulo
	4. `+` Addition
	5. `-` Subtraction

- Use **parentheses** to override default order
- ### String Functions
  ```sql
  -- Concatenate initials using LEFT()
  SELECT VendorContactFName, VendorContactLName,
       LEFT(VendorContactFName, 1) + LEFT(VendorContactLName, 1) AS Initials
  FROM Vendors;
  ```
- ### Date Functions
  ```sql
  -- Age of an invoice in days
  SELECT InvoiceDate,
       GETDATE() AS 'Today''s Date',
       DATEDIFF(day, InvoiceDate, GETDATE()) AS Age
  FROM Invoices;
  ```
- `GETDATE()` → returns current date/time (no parameters needed)
- `DATEDIFF(unit, start, end)` → difference between two dates
  
---
- ## WHERE Clause
  
  Filters which rows are returned.  
- ### Comparison Operators
  | Operator     | Meaning                  |
  | ------------ | ------------------------ |
  | `=`          | Equal to                 |
  | `<`          | Less than                |
  | `>`          | Greater than             |
  | `<=`         | Less than or equal to    |
  | `>=`         | Greater than or equal to |
  | `!=` or `<>` | Not equal to             |
- ### Examples
  ```sql
  -- Price > 100
  WHERE productprice > 100;
  
  -- Multiple conditions (AND)
  WHERE productprice <= 110 AND categoryid = 'FW';
  
  -- NOT condition
  WHERE productprice <= 110 AND NOT categoryid = 'FW';
  -- equivalent:
  WHERE productprice <= 110 AND categoryid <> 'FW';
  
  -- Date filter
  WHERE tdate < '2013-01-04';
  ```
- ### BETWEEN
  ```sql
  WHERE productprice BETWEEN 35 AND 100;        -- inclusive
  WHERE InvoiceDate BETWEEN '2020-01-01' AND '2020-01-31';
  WHERE VendorZipCode NOT BETWEEN 93600 AND 93799;
  WHERE InvoiceDueDate BETWEEN GetDate() AND GetDate() + 30;
  ```
- ### IN
  ```sql
  WHERE VendorState NOT IN ('CA', 'NV', 'OR');
  ```
- ### IS NULL / IS NOT NULL
  ```sql
  WHERE PaymentDate IS NULL;
  WHERE PaymentDate IS NOT NULL;
  ```
- ### Handling NULLs – COALESCE and ISNULL
  ```sql
  -- COALESCE: returns first non-null in list
  SELECT PaymentDate, COALESCE(PaymentDate, '1900-01-01') AS NewDate
  FROM Invoices;
  
  -- ISNULL: replaces null with a specified value
  SELECT PaymentDate, ISNULL(PaymentDate, '1900-01-01') AS NewDate
  FROM Invoices;
  ```
- `COALESCE` is more flexible (accepts a list); `ISNULL` takes exactly two expressions
- Both require matching data types
- ### Logical Operators
  ```sql
  WHERE VendorState = 'NJ' AND YTDPurchases > 200
  WHERE VendorState = 'NJ' OR YTDPurchases > 200
  WHERE NOT (InvoiceTotal >= 5000 OR NOT InvoiceDate <= '2020-02-01')
  -- simplified:
  WHERE InvoiceTotal < 5000 AND InvoiceDate <= '2020-02-01'
  ```
  
---
- ## Type Conversion – CAST and CONVERT
- ### CAST
  ```sql
  SELECT InvoiceDate, InvoiceTotal,
       CAST(InvoiceDate AS varchar)  AS varcharDate,
       CAST(InvoiceTotal AS int)     AS integerTotal,
       CAST(InvoiceTotal AS money)   AS moneyTotal
  FROM Invoices;
  ```
- Integer ÷ Integer = Integer (truncated, not rounded)
- Cast one operand to `decimal` to get decimal division:
	- `50/100` → `0`
	- `50/CAST(100 AS decimal(3))` → `0.500000`
- ### CONVERT (also formats dates)
  ```sql
  SELECT CONVERT(varchar, InvoiceDate)       AS varcharDate,
       CONVERT(varchar, InvoiceDate, 1)    AS mm/dd/yy,
       CONVERT(varchar, InvoiceDate, 107)  AS "Mon dd, yyyy"
  FROM Invoices;
  ```
  
---
- ## TOP / ORDER BY
  ```sql
  -- Top 5 most expensive products
  SELECT TOP 5 productid, productname
  FROM product
  ORDER BY productprice DESC;
  
  -- Top 5 percent
  SELECT TOP 5 PERCENT invoiceid, ...
  FROM invoices
  ORDER BY balancedue DESC;
  
  -- Top 5 percent including ties
  SELECT TOP 5 PERCENT WITH TIES invoiceid, ...
  
  -- Offset/fetch (pagination)
  SELECT ...
  ORDER BY balancedue DESC
  OFFSET 0 ROWS
  FETCH FIRST 10 ROWS ONLY;
  ```
  
---
- ## Subquery in WHERE
  ```sql
  -- Product with highest price
  SELECT productid, productname
  FROM product
  WHERE productprice = (SELECT MAX(productprice) FROM product);
  ```
  

