# Python-Fundamentals
This repository contains notes from the course __Python Fundamentals__ from __Pluralsight__ by __Austin Bingham__ and __Robert Smallshire__.


# Module 1:

## Pyhton Overview Part 1:
- A general purpose programming language. 
- Python is an interpreted language however the code in compiled invisibly. 
- Python is strongly typed i.e. every object has a type.

      >> `a = '1' + 1`
      >> This will give TypeError.
- Python is dynamically typed which means there is no type checking prior to running the code.

      >> `a = '1'`
      >> `a = 1`
      >> This is allowed.


# Module 2:

## Read-Eval-Print-Loop: REPL

## Zen of Python:
- PEP: python enhancement proposals

## Scalar Type:
- Built-In data types:
   1. Primitive Scalar Type: int, float, None, Bool
   2. Collection Type: str, range, tuple, list, Dictionary, set


# Module 3:

## str:
- collection of unicode codepoints.
- not called as collection of characters because not all unicode codepoints are characters.
- They are immutable. You can replace it but cannot update it.
- Python doesn't have char. Even string with single character is also a str.
- Check out Escape Sequence and Raw String.
- Because strings are immuatble, string functions returns a new updated strings instead of updating previous strings. e.g. s = s.upper()

## bytes:
- collection of bytes.
- Can be constructed using:
   1. s = b"data"
   2. using the bytes() constructor
- string can be encoded to bytes and bytes can be decoded to str.

## list:
- mutable sequence of objects.

## dict:
- mutable sequence of key-value pair.
- dict are oredered from Python 3.6 onwards.


# Module 4:

## Introduction:
- Module: collection of similar functions in a source code file.
- Module is only run once and it is done when it is imported.


## Distinguish between Module Import and Module Execution:
- print(`__name__`) gives different results on executing or when importing.
- When imported, `__name__` attribute will store the name of the script file.
- When executed as a isolated python script, `__name__` attribute will contain the value "__main__".
- Hence, the code written under `if __name__ == "__main__":`  will only be executed if the script is run and not when imported. 


## The Python Execution Model:
- Any .py file can be considered as a module.
- Modules and scripts are interchangable based on context and usage.
- A bigger python file handling large operations should be considered as Python Program instead of Python Script or Python module.

## Main function and command line arguments:
- `from module import *` opens up to possibility of namespace clash is python programs so it should be avoided.
- `sys.argv` attribute gives access to command line arguments. `sys.argv[0]` stores the name of the file.  




# Module 5:

### Introducntion:
- Variable Assignment:
-  1. When we write `x = 1000`, x is an object refrence pointing to a int object 1000.
-  2. When we rewrite `x = 500`, int object being immutable is not updated, instead x points to a new int object 500.
-  3. Because int 1000 is no longer referred by any object reference the python garbage collector clears the memmory.
-  `id()`: Returns a integer identifier which is unique throughout the life of the object.
-  `a is b` gives same result as `id(a) == id(b)` i.e. they both refer to same object.

### Argument Passing:
- Arguments passed is a function are passed by refrence and not pass by value.
- Types of Argument:
   1. Positional Argument
   2. Arbitrary Positional Argument
   3. Keywoard Argument
   4. Arbitrary Keywoard Argument
   5. Default Argument
-  Check out: [5 Types of Arguments in Python Function Definitions](https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)

### Python Type System:
- Python is stong and dynamic typed.
- Dynamic Typing indicates that the type of varaible is not defined and decided at run time.
- Strongly typed means the variables do have a type and it matters when performing operations. 
- e.g. you cannot add a string with an integer as neither of it will be implicilty converted.

### Variable Scoping:
- LEGB Scope in Python:
  1. Local
  2. Enclosing
  3. Global
  4. Built-in 
- Check LEGBscope.py file.



# Module 6: Collections

### Tuples:
- Hetrogenous immutable sequence.
- Tuple unpacking

### str:
- Homogenous immutable sequence of unicode codepoints.
- String concatenation with `+` or `join()`.
- `join()` is preferred over`+` as it does not use too many temporary variables.
- Syntax: `"<seperator>".join(sequence)`. e.g. `a = ";".join(["1","2","3"])` => `a = '1;2;3'`.
- Use `a = a.split(";")` to reverse it.
- To concatenate: Invoke Join on empty text.
- String Formatiing:  
   1. `a = "{0}, {1}".format(1,2)`
   2. `a = "{}, {}".format(1,2)`
   3. `a = "{x}, {y}".format(y=2, x=1)`
   4. `a = "{lst[0]}, {lst[1]}".format(lst = [1,2])`
   5. `a = "{math.pi}, {math.e}".format(math = math)`  # here math is the imported module

### range:
- a.p of integers.
- Syntax: `range(start, stop, step)`
- Avoid: `for i in range(len(lst))`; Instead use: `for index, item in enumerate(lst)`.


### list:
- Hetrogenous mutable sequence.
- List slicing: `lst_slice = lst[start:end+1]`
- List Copying: List can be copied by following methods:
-  1. Assignment Operator `lst2 = lst1`
-  2. List Slicing: `lst2 = lst1[:]`
-  3. Copy Method: `lst2 = lst1.copy()`
-  4. List Comprehension: `lst2 = [item for item in lst1]`
- Shallow Copying in Python: 
-  1. When a list lst2 copies another list lst1, both lst1 and lst2 refer to different lists.
-  2. But the elements in them still refer to same list (if the element inside the first list is a LIST).
-  3. Check listCopying.py
- List Repetition: 
-  1. If an item inside a list is also a list, then repetition is shallow.
-  2. The repeted item which is also a list (sublist/nested list) refers to the same previous item (sub;list/ nested list).
-  3. Check listRepetition.py
- List Reverse:
-  1. Inplace reverse: `lst.reverse()`
-  2. New List: `lst2 = list(reversed(lst))`
- List Sorting:
-  1.In-plcae sorting: `lst.sort()`
-  2. New List: `lst2 = lst1.sort()`
-  Sort method takes two arguments: reverse and key
-  Key can be any callable object based on which sorting needa to be performed.
-  e.g. `lst.sort(key=len)` will sort based on the len(item).

### Dictionary:
- Stores key-value pairs.
- Has refrence for both keys and values.
- The key should be immutable so str, int and tuple are accepted and list are not.
- Because the keys are hashed and mutable objects like list can't be hashed.
- Dictionary Copying:
-  1. Copy method: `dict2 = dict1.copy()`
-  2. Dict constructor: `dict2 = dict(dict1)'
- Copy in dictionary is shallow just like in the list.
- Adding New items in dictionary: `dict1.update({dict2})`


### Sets:
- Unordered collection of unique and immutable objects.
- Set is mutable and elements can be added or removed but it's items are immutable as they are hashed to make search faster.
- Because items are immutable, they can't be a list.
- Items can be added using `add()` and `update()` where later is used for multiple items.
- Items can be removed using `remove()` and `discard()` where the latter doesn't give an error when element is not present.
- __Shallow Copying__: Set supports shallow copying.
- Set Algebra:
-  1. Union: `union()`
-  2. Intersection: `intersection()`
-  3. Difference: `difference()` 
-  4. Exclusive (in either one but not both): `symmetric_difference()`
-  5. `issubset()`
-  6. `issuperset()`
-  7. `isdisjoint()`

### Collection Protocol:
- Check collectionProtocol.jpg




# Module 7: Exception and Handling:

### Introduction:
- It gives mechansim to gracefully handle errors.

### Programmer Error:
- Errors like `IndentationError`, `SynataxError`, and `NameError` shouldn't be handled in `Exception`.
- It is because these errors encompasses the errors caused by programmer's mistakes which should be handled at runtime.

### Re-Raising Error:
- We can use Exception-Handling to handle an error and then proceed to re-raise the error.
- This way the error is raised like usual but along with that, we can peform little operations like printing our own error message.
- Check: reraiseError.py

### EAFP vs LBYL:
- EAFP: It's Easier to Ask Forgiveness than Permission.
-  1. It is a philosophy that says error should be handled when encountered and not before.
- LBYL: Look Before You Leap.
-  1. It is a philosophy which suggests all possible cases of errors should be found and handled before executing an opertaion.
-  Python offers EAFP with Exception-Handling.
-  LBYL will require lot of if conditions to check for error before an operation is executed.
-  Exception Handling first tries to execute operation and error is handled when generated.

### Clean-Up Actions:
- `finally` is used after `try` and all the `Except`.
- The code in `finally ` is executed no matter if `try` is successful or any one of the `Except`.
- Check exceptionHandling.py

### Platform Specific Code:
- Some code are OS-depenedent and will be different for Windows or Linux or MacOS.
- Such code can be implemented using Try and Except block.
- Check platformSpecificCode.py



# Module 8: Iterables

### Comprehension:
- It is an approach to define an iterable.
- It is declarative and functional in style.
- It is readable, expressive, effective and consice.

### Types of Comprehension:
- List Comprehension: `[ expr(item) for item in iterable ]`
- Set Comprehension: `{ expr(item) for item in iterable }`
- Dictionary Comprehension: `{ key_expr: value_expr for item in iterable }`

### List Comprehension:
- Syntax: `lst = 
