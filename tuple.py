"""
---> Tuples are the one of the 4 built-in datatypes in python.
---> Tuple items are ordered, unchangeable, and allow duplicate values.
---> Tuples also extrogenious types means we can store any datatype
---> tuples also indexed so we can access the tuple by index value
---> Tuples are immutable means once we created then we cant able to modified or changing is not allowed
"""

# syntax
# status = ("Online", "Offline","Busy", "Do not Distrub") # we can create tuples by keeping inside the parantese () and seprating by ,
status = tuple(("Online", "Offline","Busy", "Do not Distrub")) # we can create tuples by casting  tuple()
# status = tuple("Online", "Offline","Busy", "Do not Distrub") # It will throw the type error becoz tuple will take only one arugment
myName = tuple("Raj")
print(status[2])
# ans will be "r", "a", "j" bcoz strings also iterable each character treat as elements
print("type of myName", type(myName)," value of myName", myName)
# myAge = tuple(26) # it will throw the error becoz integer is not iterable
# myAge = tuple((26)) # it will throw the error becoz integer is not iterable
# print(myAge, type(myAge))
ages = (26)
# ans will get as integer  becouse inside the parentheses single integer value treat as integer
print(ages,type(ages)) 
ages = (26,)
# , make differenc when , is used then treat as tuple
print(ages,type(ages)) 


# accessing the tuples 
# ---> we can acheieve by index and loop

print(ages[0])
for i in status: print(i)

for f in range(len(status)):
    print(f)
    print("from for loop by range",status[f])

j=0
while j < len(status):
    print("from while loop",status[j])
    j +=1


# access the tuple by range of index 

print(" by index range", status[:])
print(" by index range", status[0:])
print(" by index range", status[:4])
# When slicing a tuple using an index range, Python does not throw an error even if the end index exceeds the tuple's length.
# Instead, Python returns all available elements up to the end of the tuple.
# here we are saying that starting point will be the first element and upto 9 values even if tuple have only 4 value
print(" by index range", status[:9]) 
# this will throw the error because we trying to access the 9 index item
# here we are saying that print the 9 index item in tuple, but tuple have only 4 values 
# print(" by index range", status[9])
# print(" by index range", status[-9]) index error

"""
Key Takeaway:
Slicing beyond a tuple's length is safe -> Python just gives all available elements.
Accessing an out-of-range index directly throws an error (IndexError).

"""
print(" by negative index range", status[-(len(status))])
status = ("open", "closed", "pending", "approved")

print(" by negative index range", status[-1:6])
"""
Breakdown:
status[-1] refers to last element.
6 is out of range, but slicing does not raise an error.
The slice status[-1:6] means "get elements from index -1 (approved) to index 6 (exclusive)".
Since 6 is out of range, Python simply takes "approved".
Ans ----> ('approved',)

"""
print(" by negative index range", status[-1:-7])
"""
Breakdown:
status[-1] → "approved", status[-7] does not exist.
Slicing moves left to right.
Since -1 is greater than -7, the slice is invalid (empty result).
output : ()

"""
print(" by negative index range", status[-1:0])
"""
Breakdown:
status[-1] ->"approved", status[0] -> "open".
Again, slicing moves left to right.
Here, -1 (rightmost element) is greater than 0 (leftmost element).
Since slicing requires start < end to return elements, this results in an empty tuple.
Output: ()
"""

"""
Summary of Python Slicing Rules:
Slicing beyond the available range is safe -> It does not throw an error.
Slicing moves from left to right → If start > end, the result is an empty tuple.
Negative indexing works-> But slicing must still follow the left-to-right rule.
"""


# we can check the item is present or not by using the in keyword

print("open" in status) # return True
print("Raj" in status) # return False

# modifying the masters adding the one more value
masters = ('invoice','customers','vendors')
print("Intial masters",masters)
add_masters = list(masters)
add_masters.append("stocks")
masters = tuple(add_masters)
print("adding the stocks :",masters, type(masters))
remove_masters = list(masters)
remove_masters.remove("invoice")
masters = tuple(remove_masters)
print("remoing the invoices: ",masters)
firstIndex = list(masters)
del firstIndex[0]
masters = tuple(firstIndex)
print("removing the first index: ",masters)

# unpacking the tuples ***********

# (frist,second,thrid)= masters # ValueError  we will get, bocoz we are trying to assign 2 values to 3 variables
# print(frist,second,thrid)
(frist,second) = masters
print(frist,second)
adding_values = list(masters)
adding_values.extend(["invoices","customers","users","agents"])
print(adding_values)
masters = tuple(adding_values)
(*first,last) = masters 
# first will be the list of elements not inclued last index
# last will be the last index  value of master
print(first,last)
(first,*last) = masters
# first will be the 0 index value of master
# last will be the all values expect 0 index value
print(first,last)

(first,*middle,last) = masters
# first will be the 0 index value of master
# last will be the last index value of master
# middle will be the  rest of the masters value

print(first,middle,last)
# (first,middle,last) = masters  # Value error becoz we have more value but we are trying to assign 3 varibles
print(first,middle,last)

# combined tuples we can assing one or more tuples to variables
combinedTuples = masters + status
print(combinedTuples, type(combinedTuples))
multipledRuples = masters*3
multipledRuples_second = (masters+status)*3
# multipledRuples = masters**3 Type Error becoz we are tring  unsupored operand
print("******************************************************************************")
print(multipledRuples_second)

print(multipledRuples_second.count("approved"))
print(multipledRuples_second.index("approved"))