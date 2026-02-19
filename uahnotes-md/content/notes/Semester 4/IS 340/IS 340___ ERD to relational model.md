---
title: ERD to relational model
---

# Entities
- First step is to make tables from each entities
- Weak entities need different handling than regular entities

- ## Regular entities
  - Name the table \rarr does not have to be the same as the entity name
  - Choose a basic approach and be consistent
  - Some DB use plural nouns while others use singular nouns
  - #+BEGIN_EXAMPLE
    In our data model from Chapter 2.2, the entity employee might become a table named employee or employees. Another naming issue arises with table names containing multiple words; some databases choose to run these together, while others employ underscore characters. For example, the entity assembly line could become a table named assemblyline or assembly_line.
    #+END_EXAMPLE
  - Most attributes for the entity should be converted to columns
  - Do not create columns for derived attributes
  - Don't create columns for multivalued attributes
  - Create columns for the component attributes, not the composite ones
  - Can add constraints
  - Choose a key attribute- all should have at least one
  	- Simpler primary key columns are preferred over complex ones
- ## Example
  - ![image.png](../assets/image_1771363358875_0.png)
  -
  -
  - ![image.png](../assets/image_1771363424199_0.png)
- ## Weak Entities
  - Converted into tables in almost same way as regular
  - No ID key attributes
  - Has a partial key, must be combined with key of parent entity
  - #+BEGIN_EXAMPLE
    In our example, the assembly line entity is weak. Its partial key, the number of the assembly line within a particular factory, must be combined with the factory identity for full identification.
    #+END_EXAMPLE
  - Created from weak entity must therefore incorporate the kye from parent entity as an additional column
  - Primary key for new table will be comprised of columns created from parent key and from partial
  - Column created from parent key should be constrained to always match some key in the parent table
- ### Example
  - ![image.png](../assets/image_1771363621913_0.png)
  - #+BEGIN_EXAMPLE
    Using the above guidelines, we should create tables factory and assembly_line, and include a column in assembly_line for values from the city column of factory. A good choice of name for these “borrowed” columns is to concatenate the original table and column names together; in our case, this gives us the column factory_city. (We will use the term “borrow” in reference to this process of inserting a column in one table to hold values from the primary key column of a related table.) Here is the preliminary conversion of factory and the final conversion of assembly line:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771363685792_0.png)
- # Relationships
  - Use a table for a relationship
  - Known as a cross-reference table
  - Acts as an intermediary in three-way join with two (or more tables)
  - Some cardinality ratios permit simpler solutions
- ## Many-to-Many
  - Most general type of relationship
  - #+BEGIN_EXAMPLE
    Given a table A and a table B, we create a cross-reference table with columns corresponding to the primary keys of A and B. Each row in the cross-reference table stores one unique pairing of a primary key value from A with a primary key value from B. Each row thus represents a single connection between one row in A with one row in B. If a row in A is related to multiple rows in B, then there will be multiple entries with the same A primary key value, paired with each related B primary key value.
    #+END_EXAMPLE
  - #+BEGIN_EXAMPLE
    For example, our ERD indicates a many-to-many relationship between the entities vendor and part. A computer part (such as an 8TB hard drive) can come from multiple sellers, while sellers can sell multiple different computer parts:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771363859106_0.png)
  - #+BEGIN_EXAMPLE
    We create tables vendor and part following the guidelines above, and then create the cross-reference table vendor_part. (It is common to name a cross-reference table using the names of the two tables being related, although other schemes can of course be used.) Note that the supplies relationship also has a relationship attribute, price, which we can incorporate into the cross-reference table. The result, with some fictional data, is pictured below:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771363896938_0.png)
  - #+BEGIN_EXAMPLE
    Data in the cross-reference table is constrained in several ways. First, we only want to store the relationship between rows once, so we make the combination of primary keys from the related tables into a primary key for the cross-reference table. In our example, the primary key is the combination of vendor_name and part_number. Second, each of the borrowed primary key columns should be constrained to only hold values that are present in the original tables, using foreign key constraints.
    
    Table descriptions for vendor, part, and the vendor_part cross-reference table are given below:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771363932257_0.png)
- ## One to many
  - Can be implemented in the DB using cross-reference
  - Observing that rows on the many side of the relationship can be associated with at least one row from one side
  - #+BEGIN_EXAMPLE
    In our ERD, the employee entity participates in one-to-many relationships with both factory and itself:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771389669430_0.png){:height 488, :width 396}
  - #+BEGIN_EXAMPLE
    There is also a one-to-one relationship between employee and factory, which we will deal with in the next section.
    
    Considering first the works at relationship, we see that each employee works at no more than one factory. Therefore, we can include a column for the factory’s city in the employee table. For consistency with previous choices, we will call this column factory_city. This column should be constrained by a foreign key referencing the factory table.
    
    We also have the supervises relationship to deal with. In the same fashion as above, we should include a column in the employee table containing primary keys from the employee table. However, we should give careful consideration to the name we give this added column; employee_id would be a very misleading choice! A better choice is to consider the role of the employee whose id will be stored, and call the column supervisor_id.
    
    With these changes, the employee table now looks like:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771389814094_0.png)
  - Might choose to use a cross-reference table for the relationship between factory and model in anticipation of this possibility
- ## One to one
  - Can considered a special case of one to many relationships
  - Can utilize either approach suitable for one to many relationships
  - Will be preferable to borrow primary key from one table as FK in the other table
  - #+BEGIN_EXAMPLE
    In our example, we have a one-to-one relationship, manages, between employee and factory. We could therefore add another column to the employee table, this time for the city of the factory that the employee manages. However, most employees do not manage factories, so the column will end up containing many NULL values.
    
    On the other hand, every factory should have a manager (implied by the total participation of factory in the relationship). It makes perfect sense, then, to add a column to the factory table for the employee managing the factory. This is another situation in which it makes sense to name the column for the role of the employee in this relationship, so we will call the new column manager_id.
    
    Here is the completed factory table:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771390823529_0.png)
- ### Higher arity relationships
  - Relationships with 3 or more participants create a cross reference table
- ### Identifying relationships
  - Relationships for weak entities are necessarily one to many or one to one
  - Conversion of weak entity incorporates column containing primary key values from the parent table
- # Multivalued Attributes
  - Multivalued attributes can be used to model
  - Multivalued attribute used when a list of arbitrary values needs to be stored
  - No particular expectation that values will be examined in DB search
  - Best choice might be to make a simple table with two columns-one for the primary key of the owning table and one for the values themselves
  	- Each entry in the table associates one value with the instance of the entity
  - #+BEGIN_EXAMPLE
    In our example, computer models can be marketed to customers for different applications, such as gaming, video editing, or business use. This is represented in our data model with the multivalued application attribute:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771391878368_0.png)
  - ![image.png](../assets/image_1771391887525_0.png)
  - #+BEGIN_EXAMPLE
    Many applications also require the values associated with a multivalued attribute to be restricted to a certain list of values. In this case, an additional table is used. The additional table exists just to contain the allowed values, allowing us to constrain the data to just those values. For more complex values, an artificial identifier may be added as a primary key, and the primary key used in the multivalued attribute table instead of the values themselves, in which case the multivalued attribute table becomes a cross-reference table. For small lists of simple values (as in our example), this adds unnecessary complication.
    
    For our example, we will constrain the application column using a foreign key constraint referencing this simple table:
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771391907170_0.png)
- # Full model conversion
  - ![image.png](../assets/image_1771392271147_0.png)
  - ![image.png](../assets/image_1771392383059_0.png)
  - ![image.png](../assets/image_1771392391709_0.png)
  - ![image.png](../assets/image_1771392400429_0.png)
  - #+BEGIN_EXAMPLE
    The model table contains columns for the attributes of the model entity. Only the component attributes of the composite attribute designation are included; as designation was also the key attribute for model, the model table has a composite primary key. The table also includes a foreign key implementing the builds relationship. As mentioned in the text above, the builds relationship could alternatively be implemented using a cross-reference table connecting factory and builds, but we have opted for the simpler solution here. We assume that the designation of computer models includes the name of the computer line (e.g. “Orion”) and some particular version of the computer line, which we call the “number” of the model. These versions may contain letters as well as numbers (e.g., “xz450”), which is why a column named “number” is implemented as text.
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771392418408_0.png)
  - #+BEGIN_EXAMPLE
    The model_application table implements the multivalued attribute application of the model entity. Each row of the table contains a single application value describing a particular computer model. Note that, as the model entity has a composite primary key, the model_application table has a composite foreign key referencing its parent (not two separate foreign keys for each component of the parent key). Additionally, we constrain the values in application to come from a set list of possible values, contained in the application table (below).
    #+END_EXAMPLE
  - ![image.png](../assets/image_1771392493463_0.png)
  - ![image.png](../assets/image_1771392547396_0.png)
  - ![image.png](../assets/image_1771392559530_0.png)
  - ![image.png](../assets/image_1771392573423_0.png)
  -