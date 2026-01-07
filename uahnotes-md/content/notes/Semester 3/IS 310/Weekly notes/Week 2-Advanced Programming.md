## I. Decision Structures
### Introduction to Decisions
  * [cite_start]**Control Structures:** While programs normally follow a sequential flow, control structures allow the program to alter this flow to suit specific situations [cite: 830-832].
  * [cite_start]**Decision Structure:** Also known as a "selection structure," this allows a program to execute different sequences of instructions for different cases[cite: 839, 884].
### The `if` Statement
  * **Syntax:**
    ```python
    if condition:
        statement
        statement
    ```
  * **Logic:**
    * [cite_start]The condition is evaluated first[cite: 865].
    * [cite_start]If **True**: The indented statements are executed[cite: 867].
    * [cite_start]If **False**: The statements are skipped[cite: 868].
  
  
  
  [Image of if statement flowchart]
### Relational Operators
  Relational operators determine the relationship between two values.
  
  | Operator | Mathematics | Meaning | Citation |
  | :--- | :--- | :--- | :--- |
  | `<` | $<$ | [cite_start]Less than | [cite: 964] |
  | `<=` | $\le$ | [cite_start]Less than or equal to | [cite: 964] |
  | `==` | $=$ | [cite_start]Equal to | [cite: 964] |
  | `>=` | $\ge$ | [cite_start]Greater than or equal to | [cite: 964] |
  | `>` | $>$ | [cite_start]Greater than | [cite: 964] |
  | `!=` | $\ne$ | [cite_start]Not equal to | [cite: 964] |
  
  * [cite_start]**Warning:** Do not confuse the equality operator `==` with the assignment operator `=`[cite: 1009].
### Boolean Expressions & Variables
  * [cite_start]**Boolean Expressions:** Expressions tested by `if` statements that evaluate to either `True` or `False`[cite: 934, 1031].
  * [cite_start]**Flags:** A boolean variable used to signal when a specific condition exists in a program[cite: 947].
### Comparing Strings
  * [cite_start]**Method:** Strings are compared character by character based on their ASCII/Unicode values (lexicographic ordering)[cite: 1016, 1143].
  * [cite_start]**Case Sensitivity:** Uppercase letters come before lowercase letters (e.g., "Bbbb" comes before "aaaa")[cite: 1017].
  
---
## II. Advanced Decision Logic
### The `if-else` Statement (Two-Way)
  * [cite_start]**Purpose:** A dual alternative decision structure that provides two possible paths of execution[cite: 1095].
  * **Syntax:**
    ```python
    if condition:
        statements
    else:
        other statements
    ```
    [cite_start][cite: 1097-1100]
  
  
  
  [Image of if-else statement flowchart]
### The `if-elif-else` Statement (Multi-Way)
  * **Purpose:** Allows for testing multiple conditions in order. [cite_start]It executes the block for the *first* true condition found and ignores the rest [cite: 1231-1232].
  * [cite_start]**Mutually Exclusive:** This structure sets up mutually exclusive code blocks[cite: 1230].
  * [cite_start]**Optional Else:** The `else` block is optional; without it, it is possible no indented block will execute[cite: 1240].
### Nested Decision Structures
  * [cite_start]**Definition:** A decision structure placed inside another decision structure[cite: 1248].
  * [cite_start]**Usage:** Commonly used when multiple criteria must be met (e.g., salary > 30k *and* years on job >= 2)[cite: 1251].
  * [cite_start]**Formatting:** Proper indentation is crucial for the interpreter and readability[cite: 1274].
### Logical Operators
  [cite_start]Operators used to combine boolean expressions[cite: 1332].
  
  1.  [cite_start]**`and`**: True only if **both** operands are true[cite: 1341].
  2.  [cite_start]**`or`**: True if **either** operand is true[cite: 1348].
  3.  [cite_start]**`not`**: Reverses the logical value (True becomes False, False becomes True)[cite: 1362].
  
  * **Short-Circuit Evaluation:**
    * For `or`: If the left operand is true, the rest is ignored (result is true).
    * [cite_start]For `and`: If the left operand is false, the rest is ignored (result is false) [cite: 1354-1356].
  * **Checking Ranges:**
    * [cite_start]Inside range: `x >= 10 and x <= 20`[cite: 1370].
    * [cite_start]Outside range: `x < 10 or x > 20`[cite: 1372].
  
---
## III. Repetition Structures
### The `while` Loop (Condition-Controlled)
  * [cite_start]**Behavior:** Repeats a set of statements as long as a condition is true[cite: 1402].
  * **Pretest Loop:** The condition is tested *before* the iteration. [cite_start]If false initially, the loop never runs [cite: 1425-1426].
  * **Infinite Loops:** Occur if the loop does not contain code to make the condition false. [cite_start]The loop repeats until interrupted [cite: 1453-1454].
  
  
  
  [Image of while loop flowchart]
### The `for` Loop (Count-Controlled)
  * [cite_start]**Behavior:** Iterates a specific number of times, typically over a sequence of data items [cite: 1462-1464].
  * [cite_start]**Syntax:** `for variable in [val1, val2]:`[cite: 1467].
  * [cite_start]**Target Variable:** References the current item in the sequence during each iteration[cite: 1501].
  * [cite_start]**The `range()` Function:** Simplifies creating iterable sequences[cite: 1490].
    * One argument: `range(stop)`
    * Two arguments: `range(start, stop)`
    * [cite_start]Three arguments: `range(start, stop, step)` [cite: 1493-1496].
    * [cite_start]Descending: Use a negative step value, e.g., `range(10, 0, -1)`[cite: 1519].
  
---
## IV. Common Loop Patterns
### Calculating a Running Total
  * [cite_start]**Accumulator:** A variable initialized to 0 outside the loop to store the total[cite: 1527].
  * [cite_start]**Process:** The loop reads each number and adds it to the accumulator[cite: 1526, 1539].
### Augmented Assignment Operators
  [cite_start]Shorthand operators for updating variables[cite: 1547].
  
  | Operator | Usage | Equivalent To | Citation |
  | :--- | :--- | :--- | :--- |
  | `+=` | `c += 3` | [cite_start]`c = c + 3` | [cite: 1572] |
  | `-=` | `y -= 2` | [cite_start]`y = y - 2` | [cite: 1565] |
  | `*=` | `z *= 10` | [cite_start]`z = z * 10` | [cite: 1566] |
  | `/=` | `a /= b` | [cite_start]`a = a / b` | [cite: 1567] |
### Sentinels
  * [cite_start]**Definition:** A special value marking the end of a sequence (e.g., an empty string or -1)[cite: 1583].
  * [cite_start]**Requirement:** Must be distinctive enough not to be mistaken for actual data[cite: 1585].
### Input Validation Loops
  * **Concept:** "Garbage in, garbage out" (GIGO). [cite_start]Programs should reject bad input [cite: 1593-1594].
  * [cite_start]**Logic:** Use a `while` loop that repeats *as long as* the input is invalid, prompting the user again[cite: 1601].
### Nested Loops
  * [cite_start]**Definition:** A loop contained inside another loop[cite: 1620].
  * [cite_start]**Execution:** The inner loop completes *all* its iterations for *each* single iteration of the outer loop[cite: 1653].
  * [cite_start]**Total Iterations:** Iterations of inner loop × Iterations of outer loop[cite: 1656].