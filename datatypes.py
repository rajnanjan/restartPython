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
# del name[0] typeError becoz python does not support item deletion and additions
# name[0]= "pythoness"
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


#Tuple (tuple)
"""
Ordered, immutable, allows duplicates.
Faster than a list.
"""
invoicesStatus = ("closed","open","dispute","p2p")

print("type of invoicesStatus:", type(invoicesStatus))

# Set (set)
"""
Unordered, mutable, unique values only.
No duplicate values.
"""
unique_numbers = {1, 2, 3, 3, 4}

print("Type of unique_numbers",type(unique_numbers))

unique_numbers.add(5)   # Add an element
unique_numbers.remove(2)  # Remove an element
print(unique_numbers)
unique_numbers.add(5) # if duplicated will not throw error and it wont add in the set 
print(unique_numbers)
# unique_numbers.remove(9)  # will get the keyerror we trying to delete the key which is not present in set

# Dictionary (dict)
"""
Stores key-value pairs.
Unordered (Python 3.6+ maintains order).
"""
apiDetails={
    "url":"http://localhost:8000/api/v1/invDetails",
    "method":"GET", 
}

apiDetails["headers"]="bearer <token>"

# accessing the keys

print(apiDetails["headers"])
# print(apiDetails.method)  Attribute error dict doesn't  support .access


# Special Data Types
"""
NoneType (None)
Represents absence of value.
"""
result = None # case sensitive
print("type of result: ", type(result)) # NoneType
# result = none # we will get NameError none is not define

# Complex (complex)
# Stores real + imaginary numbers (a + bj).

num = 2 + 3j
print("Type of num ", type(num)) # complex


# Type Conversion (Type Casting)
# Python allows converting between data types.
# Implicit Conversion (Done by Python) which is automatically done by python

x = 10      # int
y = 3.5     # float
result = x + y  # Automatically converted to float
print(result)  # Output: 13.5

# Explicit Conversion (Manual)
# which we are converting based on the requirement

a = "100"
b = int(a)  # Convert string to integer

c = 5.5
d = int(c)  # Convert float to integer (truncates decimals)
print(d)
e = list("hello")  # Convert string to list

"""
Interview Tips:
List vs. Tuple?

Lists are mutable, tuples are immutable.
Tuples are faster than lists.
Set vs. List?

Set has unique values & is unordered.
List allows duplicates & is ordered.
Dict vs. Set?

Dict has key-value pairs.
Set has only unique values.
"""


# One more is Range 

customers = range(50,60)
print(customers, "type of customers : ", type(customers))
customers = range(40)
print(customers, "type of customers : ", type(customers))

# for loop by using the range
for i in customers:
    print(i)

print(memoryview(bytes(5)))