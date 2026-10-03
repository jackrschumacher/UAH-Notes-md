---
title: Chapter 3
---



### Basic database concepts

- How to map an ER diagram into a relational schema
- Relation can also refer to relational table or even just a table
- Column is a relation also sometimes referred to as a field or attribute
- Row is sometimes referred to as a tuple or a record
- Relation = Relational Table = Table
- Column = Attribute = Field
- Row = Tuple = Record
- **Primary key** \rarr every relation should have a column that serves a primary key. To distinguish one row from another
- ### Map entities into relations
- ### Mapping Entities with Composite Attribute into Relations
- ### Mapping Entities with Unique composite attribute into relations
	- Illustrates how an entity whose unique attribute is a composite attribute mapped into a relationship
	- Primary key that is composed of multiple attribute is called a **composite primary key**
- ### Mapping Entities with Optional Attributes into relations
- ### Entity Integrity Constraint
	- Refers to a rule that a relational database has to satisfy in order to be valid
	- **Entity integrity constraint is a relational database rule that states all primary key columns must have values**
	- No primary key column can be optional - all RDBMNS enforces this rule
- ### Foreign Key
	- Addition to mapping entities, relationship also have to be mapped
	- Foreign key is a mechanism that is used to depict relationships in the relational database model
	- For every occurrence of the foreign key, the relational schema contains a line pointing from foreign
	- 1:M, M:N, 1:1
- ### Mapping 1:M Relationships
- ### Mapping M:N Relationships
	- Relationship created to represent the M:N relationship itself
	- Two foreign keys form the composite primary key of the new relation
- ### Mapping 1:! Relationships
	- 1:1 relationships mapped in the same way as 1:M relationships
- ### Referential Integrity Constraint
	- Relational database rule that defines valid values
- ### Mapping ER diagram into relational schema
- ### Mapping entities with Canidate Keys