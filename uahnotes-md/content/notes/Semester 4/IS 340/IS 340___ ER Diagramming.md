---
title: ER Diagramming
---



# Basic model

- ERD is concerned with entities and relationships between them
- Connected with straight lines
- ## Entities
	- #+BEGIN_EXAMPLE
	  Ex: persons, products, companies
	  #+END_EXAMPLE
	- Things or objects with independent existence
	- Nouns
	- Rectangle shape with name
	- Entity models all of a type
- ## Attributes
	- Denoted by ovals attached by straight lines
	- Can attach many attributes as necessary to entity
- ## Keys
	- Has at least one attribute that uniquely identifies instances of the entity
	- Key attributes indicating by underlining the attributes label
	- ![image.png](../assets/image_1771121236757_0.png)
	- Allow for multiple key attributes
- ## Relationships
	- Two or more entities
	- Act like verbs in modeling language
	- ![image.png](../assets/image_1771121319609_0.png)
- ## Cardinality ratios and Participation
	- ![image.png](../assets/image_1771121427494_0.png)
	- ![image.png](../assets/image_1771121514735_0.png)
	- ![image.png](../assets/image_1771121523914_0.png)
- ## Example
	- ![image.png](../assets/image_1771121600173_0.png)
	-
	- #+BEGIN_EXAMPLE
	  Note that the factory entity does not use a generated key, but a “natural” one - the city in which the factory is located. (This only works if our company has no more than one factory in a city!)
	  
	  While this is only part of the complete model that we will ultimately develop, it is a valid ERD from which we could build a database. All of the necessary detail is in place.
	  
	  There is also no unnecessary duplication of information in our model. It is tempting to add attributes or other features that anticipate the database to come; for example, we might think that employees should have an attribute indicating at which factory they work. However, the fact that (at least some) employees work at a factory is already implicit in the relationship works at. This relationship will give rise to the necessary database structures connecting employees to factories.
	  #+END_EXAMPLE

- # More complex modeling options
  - ## Recursive relationships
  	- Relationships can exist between entity and itself
  	- Frequently used in hierarchical relationships
  	- #+BEGIN_EXAMPLE
  	  Example: Each employee (except the head of the company) has a supervisor who is another employee. (One to many)
  	  #+END_EXAMPLE
  	- ![image.png](../assets/image_1771122003883_0.png)
  - ## Weak entities
  	- #+BEGIN_EXAMPLE
  	  In some situations, we may want to model an entity for which we do not have a unique identifier, but which can be uniquely identified in relationship with another entity. As an example, each of the factories of our computer manufacturer will contain assembly lines. We wish to track certain information about each assembly line in our database, such as the daily throughput of the assembly line (the number of computers it can produce in a day). We wish to model these as an entity in our data model, but it is not immediately clear what property of an assembly line would make a good identifier.
  	  
  	  We could, of course, give every assembly line a generated unique identifier, but there is a more natural way to identify assembly lines. In each factory, assembly lines are simply numbered starting from 1, most likely in order by their position on the factory floor. To identify a particular assembly line, we first state which factory it is in, and then its number within the factory.
  	  
  	  When an entity is dependent on another entity for full identification, the dependent entity is called a weak entity, and we notate it using a rectangle with doubled outline. The weak entity has only a partial, or weak, key - in our example, this is the number of the assembly line within the factory. We note the weak key using a dashed underline. We also call out the relationship that the weak entity depends on for its identity, to distinguish it from any other relationships the weak entity participates in. We call this relationship the identifying relationship, and draw it as a diamond with a doubled outline. The key of the parent entity together with the weak key of the weak entity constitutes a unique identifier for instances of the weak entity.
  	  #+END_EXAMPLE
  	- ![The weak entity assembly line and the entity factory and their attributes, connected by the one-to-many relationship contains; assembly line has attributes number and throughput](https://runestone.academy/ns/books/published/practical_db/_images/weak_entity.svg)
  - ## Composite attributes
  	- Might wish to model an attribute that is naturally composed of multiple parts
  	- Indicate that these attributes work together as part of a larger property of the entity
  	- Essential in cases where our key is itself composed of multiple attributes
  	- Must create composite attribute
  	- ![image.png](../assets/image_1771123728471_0.png)
  - ## Multivalued attributes
  	- Properties of entities are not simple values
  	- Doubled outline
  	- ![image.png](../assets/image_1771123839980_0.png)
  	- #+BEGIN_EXAMPLE
  	  In our example, computer models may be designed or marketed for particular applications, such as gaming, multimedia, or business. As computers may fit into more than one of these categories, we model it above as a multivalued attribute.
  	  #+END_EXAMPLE
  - ## Derived attributes
  	- Have important properties that we want to not on our data model, but which we would prefer to compute from other values in the data model, rather than store in the DB
  	- Age of a person is important property for many applications
  		- Bad idea for storing though, store BD and then calc cage
  	- #+BEGIN_EXAMPLE
  	  In our computer manufacturer example, we are interested in the total throughput of each factory. While we could make this an attribute of factory, we note that a factory’s throughput can be calculated by summing up the throughputs of the factory’s assembly lines. We model these calculated properties as derived attributes, using a dashed outline:
  	  #+END_EXAMPLE
  		- ![image.png](../assets/image_1771124527059_0.png)
  - ## Relationship attributes
  	- Most attributes attached to entitities
  	- Can also attach attributes to relationships
  	- Also do this when attribute property applies to entities
  	- **Most frequently occurs with many-to-many relationships**
  	- #+BEGIN_EXAMPLE
  	  Our fictional computer manufacturer buys computer parts from multiple vendors. The manufacturer considers certain parts that have similar properties to be a single “part”. For example, the database might contain an entry for the part “8TB 7200RPM hard drive”, regardless of brand. However, at any given time, one vendor’s price for a given part may be different from another vendor’s price for the same part. This price therefore cannot belong to the part entity - it depends on vendor, too. Similarly, vendors supply many different parts, so the price cannot belong to the vendor entity. Instead, it belongs to the relationship between these entities:
  	  #+END_EXAMPLE
  	- ![image.png](../assets/image_1771124670582_0.png)
  - ## Higher-arity relationships
  	- #+BEGIN_EXAMPLE
  	  We stated that two or more entities could participate in a relationship. While most relationships are binary, you may run into cases where you need to relate three (or more) entities. We do not have an example of this in our model. However, a classic example arises in the context of large organizations or government agencies with many projects involving complex contracts with parts suppliers. Projects use many parts, and parts may be used in multiple projects; additionally, the same part might be available from different vendors. Normally this might be modeled using two many-to-many relationships (very much like what is in our computer manufacturer model). However, if the company has legal agreements that, for a certain project, a certain type of part must come from a certain vendor, while for a different project, the same type of part must come from a different vendor, the situation is not easily modeled using binary relationships. What we need is a relationship that connects parts, projects, and vendors.
  	  
  	  In this example, the relationship is many-to-many-to-many, which may be notated as M:N:P (or N:N:N):
  	  #+END_EXAMPLE
  	- ![image.png](../assets/image_1771124792765_0.png)
  - ## Complete example
  	- ![image.png](../assets/image_1771124854409_0.png)
- # ERD designing DB
  - ERD produces an abstract model of the data
  - Contains no details specific to SQL or relational DB
  - #+BEGIN_EXAMPLE
    In a similar vein, we encourage you to avoid spending effort on perfect conformance to the ERD notation. In the interest of improved communication, you should feel free to adapt the notation to your needs. You can (and perhaps should) add text explanations wherever they are helpful - designing a large database is a complex endeavor, and it can be easy to forget the reasons for particular design decisions. Notational details will become more important in the later stages of design, however, as you begin to test your design with actual database construction.
    #+END_EXAMPLE
  - ## Anaylasis
  	- Requirements might be dictated by:
  		- Data domain
  		- User needs
  		- Data sources
  		- Application requirements
  	- Might need to talk to domain experts in the DB field
  	- Brainstorming entities, relationships
  	- Once you have a good set of data elements and relations you can work on an ERD
  	- Question all assumptions
  	- Might take time to build an ERD satisfactory for all
  - ## Design, implementation and beyond
  	- Once you have an ERD you can engage in further design activities
  	- Does not fully dictate how your db will be built-need to choose table and col names for a relational db as well as data types for different values
  	- Assumptions do not always hold \rarr important to resolve issues over time as encountered