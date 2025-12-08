---
title: Week 1-Python basics
---

## I. Introduction to Python
### Overview & Characteristics
  * [cite_start]**General Purpose:** Python is a general-purpose programming language used for various tasks, including search engines (Google), mission-critical projects (NASA), and financial transactions[cite: 129, 130].
  * [cite_start]**Interpreted:** Code is translated and executed by an interpreter one statement at a time, unlike compiled languages where the entire source code is compiled before execution[cite: 147, 148].
  * **Object-Oriented:** Data in Python are objects created from classes. [cite_start]A class defines properties and methods for manipulating objects[cite: 156].
  * [cite_start]**History:** Created by Guido van Rossum in the Netherlands in 1990 and is Open Source[cite: 160, 161].
### Python 2 vs. Python 3
  * [cite_start]**Version Compatibility:** Python 3 is a newer version and is **not backward compatible** with Python 2[cite: 167].
  * [cite_start]**Course Standard:** This course uses Python 3, though differences are minimal[cite: 174, 177].
  * **Syntax Difference Example:**
    * [cite_start]**Python 2:** `print "text"`[cite: 178].
    * [cite_start]**Python 3:** `print("text")`[cite: 178].
  
---
## II. Programming Modes
### 1. Interactive Mode
  * [cite_start]**Execution:** Uses the Command Prompt or Shell to type `python`[cite: 8].
  * **Limitations:**
    * [cite_start]Not suitable for large programs[cite: 25].
    * [cite_start]Does not save statements; code cannot be reused in the future without retyping[cite: 26, 27].
    * [cite_start]Editing code is tedious as you must revisit previous commands[cite: 28, 29].
### 2. Script Mode
  * [cite_start]**Execution:** Code is written in a file (e.g., using Notepad), saved with a `.py` extension, and executed via the command line[cite: 34, 40, 46].
  * [cite_start]**Benefits:** Allows for saving, editing, and running larger blocks of code [cite: 36-40].
  
---
## III. Program Structure & Anatomy
### Basic Anatomy
  * [cite_start]**Statements:** Represents an action or a sequence of actions (e.g., `print("Welcome")`)[cite: 288, 342].
  * **Indentation:** Indentation matters in Python. [cite_start]Statements must be entered from the first column or consistently indented (typically 4 spaces)[cite: 290, 350, 382].
    * [cite_start]*Note:* Incorrect indentation will cause an error[cite: 352].
  * **Comments:**
    * [cite_start]Used to document code, describe sequences, or temporarily disable lines [cite: 484-486].
    * **Single Line:** Starts with `#`. [cite_start]Anything after `#` is ignored by Python[cite: 305, 482].
    * [cite_start]**Paragraph/Block:** Enclosed in triple quotes `"""` or `'''`[cite: 360].
### Planning with Pseudocode
  * [cite_start]**Definition:** A method of planning that enables the programmer to plan without worrying about syntax[cite: 81].
  * [cite_start]**Sequence:** Based on the assumption that the computer executes the program from the beginning to the end (SEQUENCE)[cite: 57, 59].
  * [cite_start]**Process:** Think about the goal, run through the steps, and write them in simple English before typing the program[cite: 65, 66].
  
---
## IV. Variables & Identifiers
### Variables
  * [cite_start]**Definition:** A named place in memory where a programmer can store data and retrieve it later[cite: 521].
  * **Assignment:** Uses the `=` operator. [cite_start]The expression on the right is evaluated and assigned to the variable on the left[cite: 573, 574].
    * [cite_start]Example: `radius = 20`[cite: 419].
    * [cite_start]Simultaneous assignment is possible: `x, y = y, x`[cite: 615].
  * **Named Constants:** Python has no special syntax for constants. [cite_start]By convention, use **all uppercase letters** to denote a constant (e.g., `PI = 3.14`)[cite: 623, 624].
### Identifier Rules
  * [cite_start]**Allowed Characters:** Letters, digits, underscores (`_`), and asterisks (`*`)[cite: 491].
  * **Starting Character:** Must start with a letter or an underscore. [cite_start]**Cannot** start with a digit[cite: 492].
  * [cite_start]**Case Sensitivity:** Python is case sensitive (e.g., `spam`, `Spam`, and `SPAM` are different)[cite: 502, 506].
  * [cite_start]**Reserved Words:** Identifiers cannot be reserved words (keywords like `if`, `while`, `class`, `import`, `return`, etc.)[cite: 493, 513].
  
---
## V. Data Types & Math
### Numerical Data Types
  * [cite_start]**Integer (`int`):** Whole numbers (e.g., 3, -14, 0)[cite: 630, 639].
  * [cite_start]**Float (`float`):** Numbers with decimal parts (e.g., 3.0, 98.6, -2.5)[cite: 631, 640].
  * [cite_start]**Scientific Notation:** Floating-point literals can use `e` or `E` for exponents[cite: 678, 681].
    * [cite_start]Example: `1.23456e+2` is equivalent to `123.456`[cite: 679].
### Operators
  | Operator | Name | Example | Result | Citation |
  | :--- | :--- | :--- | :--- | :--- |
  | `+` | Addition | `34 + 1` | [cite_start]35 | [cite: 651] |
  | `-` | Subtraction | `34.0 - 0.1` | [cite_start]33.9 | [cite: 651] |
  | `*` | Multiplication | `300 * 30` | [cite_start]9000 | [cite: 651] |
  | `/` | Float Division | `1 / 2` | [cite_start]0.5 | [cite: 651] |
  | `//` | Integer Division | `1 // 2` | [cite_start]0 | [cite: 651] |
  | `**` | Exponentiation | `4 ** 0.5` | [cite_start]2.0 | [cite: 651] |
  | `%` | Remainder | `20 % 3` | [cite_start]2 | [cite: 651] |
### Operator Precedence (Order of Evaluation)
  
  
  [cite_start]Python follows specific rules for which operators execute first, generally from left to right[cite: 701, 708]:
  1.  [cite_start]**Parentheses:** `()`[cite: 709].
  2.  [cite_start]**Exponentiation:** `**`[cite: 710].
  3.  [cite_start]**Multiplication, Division, Remainder:** `*`, `/`, `//`, `%`[cite: 711].
  4.  [cite_start]**Addition and Subtraction:** `+`, `-`[cite: 711].
### Type Conversion & Math Notes
  * [cite_start]**Mixing Types:** If an operation involves an integer and a float, the integer is converted to a float, and the result is a float[cite: 767].
  * [cite_start]**Augmented Assignment:** Shortcuts for math operations[cite: 779].
    * [cite_start]`i += 8` is equivalent to `i = i + 8`[cite: 783, 784].
  * **Conversion Functions:**
    * [cite_start]`int(4.5)` returns `4`[cite: 807].
    * [cite_start]`float(4)` returns `4.0`[cite: 807].
    * [cite_start]`str(4)` returns `"4"`[cite: 807].
    * [cite_start]`round(4.6)` returns `5`[cite: 808].
  
---
## VI. Functions
  
  * [cite_start]**Definition:** Equivalent to a static method in Java[cite: 320].
  * **Syntax:**
    ```python
    def name():
        statement
        statement
    ```
    [cite_start][cite: 322-325]
  * **Usage:** Must be declared *above* the code that calls it. [cite_start]Statements inside must be indented[cite: 335, 336].
  
---
## VII. Debugging & Errors
### Types of Errors
  1.  **Syntax Errors:**
    * [cite_start]An error of language resulting from code that does not conform to the syntax (e.g., missing a `:`)[cite: 98, 99].
    * [cite_start]Result: `SyntaxError: invalid syntax`[cite: 104].
  2.  **Runtime Errors:**
    * [cite_start]Code is syntactically correct but causes an error during execution (program aborts)[cite: 106, 400].
    * Examples:
        * [cite_start]`ZeroDivisionError`: Division by zero[cite: 113].
        * [cite_start]`NameError`: Using a variable (`spam`) that is not defined[cite: 116].
        * [cite_start]`TypeError`: Trying to combine incompatible types (e.g., 'str' and 'int')[cite: 119].
        * [cite_start]`OverflowError`: Result too large to be stored[cite: 662].
  3.  **Logic Errors:**
    * [cite_start]The program runs but produces an incorrect result[cite: 402].
  
---
## VIII. Input and Output
  
  * **Console Output:**
    * [cite_start]`print("text")` prints text to the console[cite: 296].
    * [cite_start]`print()` prints a blank line[cite: 297].
    * [cite_start]Escape sequences like `\"` work as they do in Java[cite: 298].
  * **Console Input:**
    * [cite_start]Use the `input` function: `variable = input("Enter a string: ")`[cite: 469, 472].
    * [cite_start]Use `eval` to evaluate a string as a number/expression: `eval("5 + 10")`[cite: 473, 476].
-