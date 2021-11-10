# Python-Fundamentals
This repository contains notes from the course Python Fundamentals from Pluralsight by Austin Bingham and Robert Smallshire.


Module 1:

Pyhton Overview Part 1:
- A general purpose programming language. 
- Python is an interpreted language however the code in compiled invisibly. 
- Python is strongly typed i.e. every object has a type.
- Python is dynamically typed which means there is no type checking prior to running the code.


Module 2:

Read-Eval-Print-Loop: REPL

Zen of Python:
- PEP: python enhancement proposals

Scalar Type:
- Built-In data types:
   1. Primitive Scalar Type: int, float, None, Bool
   2. Collection Type: Dictionary


Module 3:

str:
- collection of unicode codepoints.
- not called as collection of characters because not all unicode codepoints are characters.
- They are immutable. You can replace it but cannot update it.
- Python doesn't have char. Even string with single character is also a str.
- Check out Escape Sequence and Raw String.
- Because strings are immuatble, string functions returns a new updated strings instead of updating previous strings. e.g. s = s.upper()

bytes:
- collection of bytes.
- Can be constructed using:
   1. s = b"data"
   2. using the bytees() constructor
- string is encoded to bytes and bytes is decoded to str.

list:
- mutable sequence of objects.

dict:
- mutable sequence of key-value pair.
- dict are oredered from Python 3.6 onwards.


Module 4:

Introduction:
- Module: collection of similar functions in a source code file.


Distinguish between Module Import and Module Execution:
- print(__name__) gives different results on executing or when importing.
- When imported, __name__ attribute will store the name of the script file.
- When executed as a isolated python script, __name__ attribute will contain the value "main".
- Hence, the code written under " if __name__ == "__main__": " will only be executed if the script is run and not when imported. 



