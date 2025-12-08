---
title: Week 5- Inheritance
---

## I. Classes and Object-Oriented Programming (OOP)
### Procedural vs. Object-Oriented
  * **Procedural Programming:** Writing programs made of functions that perform specific tasks. [cite_start]Procedures operate on data items that are separate from the procedures [cite: 2680-2681].
  * **Object-Oriented Programming (OOP):** Focuses on creating objects. [cite_start]An **object** is an entity that contains both data (attributes) and procedures (methods) [cite: 2689-2690].
### Core OOP Concepts
  * [cite_start]**Encapsulation:** Combining data and code into a single object[cite: 2693].
  * **Data Hiding:** An object's attributes are hidden from code outside the object. [cite_start]Access is restricted to the object's methods to protect from accidental corruption [cite: 2706-2708].
  * [cite_start]**Object Reusability:** The same object can be used in different programs[cite: 2710].
### Classes vs. Instances
  * **Class:** Code that specifies the data attributes and methods for a type of object. [cite_start]It acts as a **blueprint** or cookie cutter [cite: 2733-2734].
  * [cite_start]**Instance:** A specific object created from a class (e.g., a specific house built from the blueprint)[cite: 2735].
### Defining Classes
  * **Syntax:**
    ```python
    class ClassName:
        def method(self):
            # statements
    ```
  * **The `self` Parameter:** Required in every method. [cite_start]It references the specific object instance the method is working on[cite: 2771].
  * **The `__init__` Method:** Also known as the **initializer**. It is automatically executed when an instance is created to initialize attributes [cite: 2777-2778].
  * **Creating Instances:**
    ```python
    my_instance = ClassName()
    ```
    [cite_start][cite: 2803].
### Attributes and Methods
  * [cite_start]**Hiding Attributes:** To make an attribute private, place two underscores before the name (e.g., `__current_minute`)[cite: 2813].
  * **Accessor Methods (Getters):** Return a value from an attribute without changing it[cite: 2882].
  * [cite_start]**Mutator Methods (Setters):** Store or change the value of an attribute[cite: 2883].
  * **The `__str__` Method:** Returns the object's state as a string. Automatically called when the object is passed to `print()` [cite: 2834-2835].
### Class Design (UML)
  * **UML Diagram:** Unified Modeling Language. Depicted as a box with three sections:
    1.  Class Name
    2.  Data Attributes
    3.  [cite_start]Methods [cite: 2896, 2898-2901].
  * **Finding Classes:** Look for nouns in the problem description. [cite_start]Refine the list by removing nouns that represent simple values or duplicates [cite: 2926-2929, 2954-2957].
  
---
## II. Inheritance
### Concepts
  * **"Is a" Relationship:** Exists when a specialized object has all characteristics of a general object plus specialized ones (e.g., A poodle *is a* dog; a car *is a* vehicle) [cite: 3000-3003].
  * **Inheritance:** Defines a new class that borrows behavior from another class.
    * **Superclass:** The general class being borrowed from.
    * [cite_start]**Subclass:** The new specialized class doing the borrowing [cite: 3015-3016].
### Benefits
  1.  [cite_start]**Avoids Duplication:** Common methods (e.g., `homeAddress`) are defined once in the superclass[cite: 3041].
  2.  [cite_start]**Code Reuse:** New classes are based on existing ones[cite: 3043].
### Syntax Example
  ```python
  class Parent:
    def func1(self):
        print("Hello Parent")
  
  class Child(Parent): # Inherits from Parent
    def func2(self):
        print("Hello Child")