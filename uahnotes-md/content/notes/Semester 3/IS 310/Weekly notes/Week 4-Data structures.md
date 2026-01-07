## I. Sequences and Lists
### Sequences
  * **Definition:** An object that contains multiple items of data stored one after another.
  * [cite_start]**Types:** Python provides different types of sequences, mainly **lists** (mutable) and **tuples** (immutable) [cite: 715-717].
### Lists
  * **Definition:** A mutable object that contains multiple data items (elements).
  * **Format:** `list = [item1, item2, etc.]`.
  * **Characteristics:**
    * [cite_start]Can hold items of different data types (e.g., integers, strings, floats) [cite: 722-725].
    * `print()` can display the entire list.
    * `list()` function converts other objects to lists.
### List Operations
  * **Repetition Operator (`*`):** Creates multiple copies of a list joined together. [cite_start]Format: `list * n` [cite: 749-752].
  * **Iteration:** You can iterate over a list using a `for` loop:
    ```python
    for item in list:
        # process item
    ```
  * **Indexing:**
    * Position of an element (starting at 0).
    * [cite_start]Negative indexes count from the end (`-1` is the last element) [cite: 760-763].
    * `len(list)` returns the number of elements.
  * [cite_start]**Mutability:** Elements can be changed using their index: `list[1] = new_value` [cite: 779-781].
  * [cite_start]**Concatenation (`+`):** Joins two lists together [cite: 787-788].
  * [cite_start]**Slicing:** Extracts a span of items: `list[start : end]` [cite: 795-797].
### List Methods & Built-in Functions
  | Method/Function | Description | Citation |
  | :--- | :--- | :--- |
  | `append(item)` | Adds item to the end of the list. [cite_start]| [cite: 816, 838, 845] |
  | `index(item)` | Returns the index of the first occurrence of item. [cite_start]| [cite: 817-818, 839, 846] |
  | `insert(index, item)` | Inserts item at a specific position. [cite_start]| [cite: 825, 840, 848] |
  | `sort()` | Sorts list in ascending order. [cite_start]| [cite: 827, 841, 853] |
  | `remove(item)` | Removes the first occurrence of item. [cite_start]| [cite: 828, 842, 854] |
  | `reverse()` | Reverses the order of elements. [cite_start]| [cite: 829, 843, 855] |
  | `del list[i]` | Removes element at specific index. [cite_start]| [cite: 860-861] |
  | `min()` / `max()` | Returns lowest/highest value in the sequence. [cite_start]| [cite: 862] |
### Copying Lists
  * **Reference vs. Value:** `list1 = list2` only makes `list1` reference the same object as `list2` (modifying one affects the other).
  * **True Copy:** Create a new list and copy elements:
    1.  Create empty list and append loop.
    2.  [cite_start]Concatenate existing list to a new empty list (`new_list = [] + old_list`) [cite: 870-873].
  
---
## II. Advanced List Features
### List Comprehensions
  * **Definition:** A concise expression to create a new list by iterating over an existing one.
  * [cite_start]**Basic Syntax:** `[item for item in old_list]`[cite: 909, 928].
  * [cite_start]**Calculations:** `[item**2 for item in list]` creates a list of squares[cite: 943].
  * [cite_start]**Filtering (if clause):** `[item for item in list if item < 10]` includes only items meeting criteria[cite: 964, 971].
### Two-Dimensional Lists
  * **Definition:** A list containing other lists as elements (nested list), often representing rows and columns.
  * [cite_start]**Processing:** Typically requires nested loops to process data (two indexes needed) [cite: 977, 981-982].
  
---
## III. Tuples
  
  * **Definition:** An immutable sequence (cannot be changed once created).
  * **Format:** `tuple_name = (item1, item2)`.
  * **Operations:** Supports indexing, slicing, `len()`, `min()`, `max()`, and `in` operator.
  * **Limitations:** Does **not** support `append`, `remove`, `insert`, `reverse`, or `sort`.
  * [cite_start]**Advantages:** Faster processing than lists and safer (data cannot be accidentally modified) [cite: 1010-1015, 1025-1030, 1037-1038].
  
---
## IV. Plotting with `matplotlib`
  
  * [cite_start]**Installation:** Not standard; install via `pip install matplotlib`[cite: 1056].
  * [cite_start]**Import:** `import matplotlib.pyplot as plt`[cite: 1075].
  * **Line Graph:** `plt.plot(x_coords, y_coords)` connects points.
  * **Bar Chart:** `plt.bar(left_edges, heights, bar_width, color)`.
  * **Pie Chart:** `plt.pie(values, labels=slice_labels)`.
  * [cite_start]**Display:** `plt.show()` renders the graph [cite: 1081, 1257, 1361-1362].
  
---
## V. Dictionaries
### Introduction
  * **Definition:** An object that stores a collection of data as key-value pairs (mappings).
  * **Format:** `dictionary = {key1: val1, key2: val2}`.
  * **Keys:** Must be immutable objects (e.g., strings, numbers, tuples).
  * **Retrieval:** `dictionary[key]`. [cite_start]Raises `KeyError` if key is not found [cite: 1409-1416, 1425-1426].
### Operations
  * **Adding/Modifying:** `dictionary[key] = value`. [cite_start]If key exists, value is updated; otherwise, new pair is added [cite: 1436-1437].
  * **Deleting:** `del dictionary[key]`.
  * [cite_start]**Length:** `len(dictionary)` returns number of pairs[cite: 1443, 1450].
  * **Methods:**
    * `clear()`: Empties the dictionary.
    * `get(key, default)`: Safely retrieves value without `KeyError`.
    * `items()`: Returns all keys and values as tuples.
    * `keys()`: Returns all keys.
    * `values()`: Returns all values.
    * [cite_start]`pop(key)`: Returns value and removes pair [cite: 1468-1471, 1479, 1490-1491].
### Dictionary Comprehensions
  * **Syntax:** `{item: item**2 for item in list}`. [cite_start]Creates a dictionary from a sequence [cite: 1516-1517, 1539].
  
---
## VI. Sets
### Introduction
  * **Definition:** An unordered collection of unique elements (no duplicates allowed).
  * **Creation:** `set_variable = set(argument)`. Argument must be iterable.
  * **Mutability:** Sets are mutable; elements can be added/removed.
### Set Operations
  * **Adding:** `add(item)` or `update(sequence)`.
  * **Removing:** `remove(item)` (raises error if missing) or `discard(item)` (no error).
  * **Set Math:**
    * **Union (`|`):** Contains all elements from both sets.
    * **Intersection (`&`):** Contains only elements found in *both* sets.
    * **Difference (`-`):** Elements in the first set but not the second.
    * [cite_start]**Symmetric Difference (`^`):** Elements in either set, but *not* both [cite: 1613-1614, 1620-1623, 1641-1646, 1653-1658, 1675-1681].
  * [cite_start]**Subsets/Supersets:** `issubset` (`<=`) and `issuperset` (`>=`) [cite: 1687-1691].
  
---
## VII. Serializing Objects
  
  * **Definition:** Converting an object to a stream of bytes to store in a file (Pickling).
  * **Process:**
    1.  `import pickle`
    2.  Open file for binary writing (`'wb'`).
    3.  **Pickle:** `pickle.dump(object, file)`.
    4.  [cite_start]**Unpickle:** `pickle.load(file)` (requires opening file for binary reading `'rb'`) [cite: 1749-1750, 1759-1763, 1768-1773].