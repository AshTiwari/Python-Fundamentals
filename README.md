# Python-Fundamentals
This repository contains notes from the course Python Fundamentals from Pluralsight by Austin Bingham and Robert Smallshire.


# Module 1:

## Pyhton Overview Part 1:
- A general purpose programming language. 
- Python is an interpreted language however the code in compiled invisibly. 
- Python is strongly typed i.e. every object has a type.
- Python is dynamically typed which means there is no type checking prior to running the code.


# Module 2:

## Read-Eval-Print-Loop: REPL

## Zen of Python:
- PEP: python enhancement proposals

## Scalar Type:
- Built-In data types:
   1. Primitive Scalar Type: int, float, None, Bool
   2. Collection Type: Dictionary


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
   2. using the bytees() constructor
- string is encoded to bytes and bytes is decoded to str.

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

## Introducntion:
- Variable Assignment:
-  1. When we write `x = 1000`, x is an object refrence pointing to a int object 1000.
-  2. When we rewrite `x = 500`, int objectg being immutable is not updated, instead x points to a new int object 500.
-  3. Because int 1000 is no longer referred by any object reference the python garbage collector clears the memmory.
-  id(): Returns a integer identifier which is unique throughout the life of the object.
-  `a is b` gives same result as `id(a) == id(b)` i.e. they both refer to same object.

## Argument Passing:
- Arguments passed is a function are passed by refrence and not pass by value.
- Types of Argument:
-  1. Positional Argument
-  2. Arbitrary Positional Argument
-  3. Keywoard Argument
-  4. Arbitrary Keywoard Argument
-  5. Default Argument
-  Check out: [5 Types of Arguments in Python Function Definitions] (https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)
-  





