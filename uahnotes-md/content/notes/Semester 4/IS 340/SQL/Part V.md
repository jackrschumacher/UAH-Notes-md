---
title: Part V
---

## Nested Queries (Subqueries)

A **nested query** (inner query / subquery) is a `SELECT` statement embedded inside another query (the **outer query**).  
- ### Why use them?
- Aggregate functions cannot be used directly in a `WHERE` clause
- A subquery in `WHERE` can compute an aggregate first, then pass the result to the outer query's condition
- ### Syntax Rules
- Always enclosed in **parentheses**
- Can return a single value, a single-column result set, or a multi-column result set
- Generally does **not** include `GROUP BY`, `HAVING`, or `ORDER BY` (unless `TOP` is used with `ORDER BY`)
- Follows the same `SELECT` syntax as a standard query
  
  ```sql
  -- General form
  SELECT columns
  FROM table
  WHERE column operator (
    SELECT column
    FROM table
    [WHERE condition]
    [GROUP BY column]
    [HAVING condition]
  );
  ```
- ### Example — Subquery in WHERE (Q28)
  ```sql
  -- Products priced below the overall average
  SELECT productid, productname, productprice
  FROM product
  WHERE productprice < (SELECT AVG(productprice) FROM product);
  ```
  
  ```sql
  -- INVALID — aggregate function cannot go directly in WHERE
  WHERE productprice < AVG(productprice);  -- ❌ Error
  ```
  
  How it works:  
	1. Inner query runs first → computes `AVG(productprice)` → returns a single value
	2. Outer query uses that value as the filter threshold
---

- ## IN
  
  `IN` compares a value against a **set of values** and returns rows where the value matches any member of the set. Cleaner alternative to chaining `OR` conditions.  
- ### Basic IN with a literal list
  ```sql
  -- Q29: Using OR (verbose)
  SELECT productid, productname, productprice
  FROM product
  WHERE productid = '1X1' OR productid = '2X2' OR productid = '3X3';
  
  -- Q29alt: Equivalent using IN (cleaner)
  SELECT productid, productname, productprice
  FROM product
  WHERE productid IN ('1X1', '2X2', '3X3');
  ```
- ### IN with a Subquery
  When the set of values comes from another table, combine `IN` with a nested query.  
  
  ```sql
  -- Q30: Products where total qty sold > 3 (qty data is in 'includes' table)
  SELECT productid, productname, productprice
  FROM product
  WHERE productid IN (
    SELECT productid
    FROM includes
    GROUP BY productid
    HAVING SUM(quantity) > 3
  );
  ```
  
  How it works:  
	1. Inner query groups `includes` by `productid` and filters to those with `SUM(quantity) > 3` → returns a list of productids
	2. Outer query retrieves full product details for only those productids
	  ```sql
	-- Q31: Products sold in more than one transaction
	SELECT productid, productname, productprice
	FROM product
	WHERE productid IN (
	SELECT productid
	FROM includes
	GROUP BY productid
	HAVING COUNT(tid) > 1
	);
	  ```
---

- ## Key Distinctions
  
  | Concept               | Detail                                                       |
  | --------------------- | ------------------------------------------------------------ |
  | Inner query           | Runs **first**, passes result to outer query                 |
  | `IN` with list        | Use for a **known, static** set of values                    |
  | `IN` with subquery    | Use when the set must be **derived** from another table      |
  | Aggregate in `WHERE`  | ❌ **Not allowed** directly — wrap in a subquery instead      |
  | Aggregate in subquery | ✅ Allowed — subquery runs as a `SELECT`, which supports aggregates |
