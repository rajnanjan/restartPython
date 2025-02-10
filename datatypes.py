# DATA TYPES

"""
---> Data types define the type of data a variable can hold. 
     They help in memory allocation and operations on variables.
---> Python provides different data types to handle various kinds of data.
"""

# Primitive Data Types (Basic, immutable)

""" 
Integer (int) -> Whole numbers (e.g., 10, -5)
Floating-point (float) -> Decimal numbers (e.g., 3.14, -0.99)
String (str) -> Sequence of characters (e.g., "hello", 'Python')
Boolean (bool) -> True or False
"""
# Collection Data Types (Stores multiple values)
""" 
List (list) -> Ordered, mutable, allows duplicates ([1, 2, "apple"])
Tuple (tuple) -> Ordered, immutable ((10, 20, "banana"))
Set (set) -> Unordered, unique values ({1, 2, 3})
Dictionary (dict) -> Key-value pairs ({"name": "Alice", "age": 25})
"""
# Special Data Types
"""
NoneType (None) -> Represents absence of value (None)
Complex (complex) -> Numbers with real & imaginary parts (2 + 3j)
"""
# Type Conversion
"""
Implicit -> Python converts automatically (int + float -> float)
Explicit -> Using int(), float(), str(), list(), etc.
"""

# Integer (int)
"""  
Stores whole numbers (positive, negative, or zero).
No size limit in Python (depends on memory).
"""
x = 10   # Integer
y = -5   # Negative Integer
z = 0    # Zero

print(x, y, z)

# Floating-point (float)
"""
Stores decimal numbers.
Follows IEEE 754 floating-point standard. // needs to explore about IEEE 754 
"""

a = 3.14 # float values
b = -0.99 # negative float values
c = 1.0   # Also a float
print (a, b, c)

# String (str)
"""
9880282618--pravin
Sequence of characters enclosed in single (' ') or double (" ") quotes.
Immutable (cannot be changed after creation).
"""

name = "Python"
greeting = 'Hello'

print(name,greeting)
print(type(name),type(greeting))

# Boolean (bool)

"""
Stores True or False.
Used in logical operations.
"""
is_active = True
has_permission = False

print("type of isactiv--->",type(is_active),"\n","type of has premission-->", type(has_permission))

# Collection Data Types (Stores Multiple Values)

# List (list)
"""
Ordered, mutable, allows duplicates.
Can store different data types.
"""

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4.5]

print("type of fruits:", type(fruits), "\n", "type of numbers:", type(numbers))

