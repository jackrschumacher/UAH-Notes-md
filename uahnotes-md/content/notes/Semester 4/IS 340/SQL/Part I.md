---
title: Part I
---



## SQL Command Categories

- **DDL** – Data Definition Language: create/modify database structure (`CREATE`, `ALTER`, `DROP`)
- **DML** – Data Manipulation Language: insert/modify/delete/retrieve data (`INSERT INTO`, `UPDATE`, `DELETE`, `SELECT`)
- **DCL** – Data Control Language: manage data access (`GRANT`, `REVOKE`)
- **TCL** – Transaction Control Language: manage transactions (`COMMIT`, `ROLLBACK`)
  - DCL and TCL are covered in Chapter 11
- ## SQL Syntax Notes
- Statements end with a semicolon `;`
- Keywords and identifiers are **not case-sensitive** (`SELECT` = `select` = `SeLeCt`)
- Statements can span multiple lines for readability
- ## SQL Data Types
- Each column must have a declared data type
- Data types define the kind of data allowed and permissible operations (numeric, text, etc.)
- See SQL Book Ch. 8 for the full list
- ## CREATE DATABASE
- Syntax: `CREATE DATABASE database_name;`
- Creates two files on the server:
  - `name.mdf` – holds the actual data
  - `name.ldf` – transaction log of all changes
- ## CREATE TABLE
- Used to define relational tables and specify constraints
- PK and FK constraints are declared inside the `CREATE TABLE` statement
- ### Syntax – Basic table with Primary Key
  ```sql
  CREATE TABLE vendor (
  vendorid   CHAR(2)      NOT NULL,
  vendorname VARCHAR(25)  NOT NULL,
  PRIMARY KEY (vendorid)
  );
  ```
- ### Syntax – Table with one Foreign Key
  ```sql
  CREATE TABLE store (
  storeid  VARCHAR(3) NOT NULL,
  storezip CHAR(5)    NOT NULL,
  regionid CHAR(1)    NOT NULL,
  PRIMARY KEY (storeid),
  FOREIGN KEY (regionid) REFERENCES region(regionid)
  );
  ```
- ### Syntax – Table with two Foreign Keys
  ```sql
  CREATE TABLE product (
  productid    CHAR(3)       NOT NULL,
  productname  VARCHAR(25)   NOT NULL,
  productprice NUMERIC(7,2)  NOT NULL,
  vendorid     CHAR(2)       NOT NULL,
  categoryid   CHAR(2)       NOT NULL,
  PRIMARY KEY (productid),
  FOREIGN KEY (vendorid)    REFERENCES vendor(vendorid),
  FOREIGN KEY (categoryid)  REFERENCES category(categoryid)
  );
  ```
- ## Referential Integrity Constraint
- A FK value in any row must **either** match a PK value in the referenced table **or** be `NULL`
  -