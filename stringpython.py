# String str()

# A string in Python is a sequence of characters enclosed in single (' '), double (" "), 
# or triple quotes (''' ''' or """ """).

# Creating Strings
string1 = 'Hello'
string2 = "Python"
string3 = '''Multiline
String Example'''
string4 = """Another
Multiline String"""

# 2. accessing the string

# Strings in Python are indexed, meaning you can access characters using indexing and slicing.

text = "Python"
print(text[0])   # Output: P
print(text[-1])  # Output: n

# (b) Slicing
# Extracts a portion of a string.
# Syntax: string[start:end:step]

# print(text[0:4:0]) # Value Error cannot be step as zero
print(text[0:4:1]) # it wont skip it will every single value
print(text[0:4])  # this is same as above statement


# String Operations

# (a) Concatenation
# Joining two strings using +:

firstname = "Raj"
lastname ="Nanjan"
fullname = firstname + " " + lastname

print(fullname) 

# (b) Repetition
# Repeating a string using *:

mupltipleString = firstname * 3
# mupltipleString = firstname ** 3 Type Error it wont support 
print(mupltipleString)

# (c) Membership Operators (in, not in)

print("raj" in firstname)  #python case sensitive so False will be answer
print("Raj" in firstname)  # True will be answer
print("raj" not in firstname) # Needs to explore
# print(!("raj" not in firstname)) # Needs to explore

# 4. String Methods
# Python provides many built-in string methods:

text = " hello world "

print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.strip())      # "hello world" (removes spaces from both ends)
print(text.replace("hello", "Hi"))  # " Hi world "
print(text.split())      # ['hello', 'world'] (Splits based on space)
print(text.split("l"))      # ['hello', 'world'] (Splits based on space)
print(len(text))         # 13 (Length of string including spaces)
print(text.count("o"))   # 2 (Count occurrences of 'o')
print(text.startswith(" hello"))  # True
print(text.endswith("world "))    # True


# 5. String Formatting
# (a) Using .format()

# In python we can merge the number in a string or any other type
expreience = 3
intro = "Hi , my self Raj, i am a software developer and i have experience in years :{}" 
# intro = "Hi , my self Raj, i am a software developer and i have experience in years :"+expreience 
# type Error becoz we can concatenate the number and string
# to our come this in python a format option 
# 1.format()
print(intro.format(expreience)) # ans : Hi , my self Raj, i am a software developer and i have experience in years :3

# f string

desc = "software developer"
expreience = 3
print(f"Hi , my self Raj, i am a {desc.upper()} and i have experience in years :{expreience}")
# ans :Hi , my self Raj, i am a SOFTWARE DEVELOPER and i have experience in years :3

# 6. Escape Characters
# Escape sequences are used to include special characters in strings.

print("Hello\nWorld")   # New line
print("Tab\tSpace")     # Tab space
print("He said \"Python is great\"")  # Using double quotes inside a string basically skip the next character
print("Backslash: \\")  # Prints \

# 7. Raw Strings (r"...")
# Raw strings ignore escape sequences.

print(r"D:\Anniyarukku ulle vara tatai\restartPython") # if any \ skip is there also it works here becoz we are raw string

"""
Summary
Strings are sequences of characters enclosed in quotes.
Can be accessed using indexing and slicing.
Common operations include concatenation, repetition, membership testing.
Many built-in methods help with manipulation.
Strings are immutable (cannot be changed after creation).
Formatting is done using .format() or f-strings.
"""