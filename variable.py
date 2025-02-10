
## vairables
""" 
----> Variables are used to store the value to reuse
----> Python has no command for declaring a variable. like in javascript (let, var, const)
----> A variable is created the moment you first assign a value to it.
"""
variable ="a"
typeOfvariable= type(variable)
print(variable)
print(typeOfvariable)
"""
---> dont need to mention the type of variable we can reassign the different data type
"""
variable1 = 120;
print(variable1, type(variable1))
variable1 = "--string value--";
print(variable1, type(variable1))

# If we want to specify the data type then that can done via casting

variable2 = int(3); variable5 = int(5)
variable3 = str(3)
variable4 = float(3)
print(variable3,variable4,variable2,variable5,variable1)

# string variable can be create via '', "" quotes, and back ticks  we cant use in python
variable6 = repr({variable,variable1,variable2,variable3,variable4, variable5}); # printable object (converting that object to a string.)
# repr used 
print(variable6)
print("repr type ---->", type(variable6))

# in Python variable or case senctive
name = "raj n"
Name = "raj_nanjan";
fristname = "raj"
fristName = "raj "
print(name,Name,fristName,fristname)

"""
---> Rules of variable declarations
---> A variable name must start with a letter or the underscore character
---> A variable name cannot start with a number
---> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
---> Variable names are case-sensitive (age, Age and AGE are three different variables)
---> A variable name cannot be any of the Python keywords
        --Python has a set of keywords that are reserved words that cannot be used as variable names, 
          function names, or any other identifiers.
"""
_frist = "raj"
frist_ = "raj"
frist_name = "raj"
name1 = "raj"
raj = "raj"

"""
---> multiple assignments
---> variable and values both numbers should be equal
"""
# v1,v2,v3,v4 = "value1","value2",123,True,123123 # error tooo many values to unpack
v1,v2,v3,v4 = "value1","value2",123,True
# m1,m2,m3 = "same value for all variable" #  following error will get ValueError: too many values to unpack (expected 3)  
m1=m2=m3= "same value for all variable" # correct one for same value for multiple variables
print(v1,v2,v3,v4)
print(m1,m2,m3)

# outpput variables 
"""
---> print() function is used to output the variable
---> we can print the multiple values together by useing the ,
---> and we can use the + symbol aslo NOTE: concatenate will work only str to str, number to number ,
---> The best way to output multiple variables in the print() function is to separate them with commas, 
     which even support different data types.
---> Python inserts a space between the two values by default, resulting in the output
---> If you wanted to change the separator, you could specify the sep parameter in the print() function
"""
print(v1,v2,v3,v4) 
# print(v1+v2+v3+v4) # type error will come because string and number cannot be concatenated
print("stat"+"start",4667 + True) # In pythone True will treate as 1 so ans will be (statstart 4668)

print("stat"+"start",4667 + True,sep='***')


# Global Variables
"""
Global Variable is accessible by inside and outside function block
"""
# example 1 
globalVariable= 20
if(True):
   globalVariable = 25
   print("inside if block",globalVariable) 
print("outside if block",globalVariable)

# example 2
def variableScope():
   globalVariable = 24
   print("inside function block",globalVariable)
variableScope()
print("outside function block",globalVariable)

#example 3

if(True):
   blockOrGlobal = "YES YOU CAN ACCESS THE VARIABLE"
print("checking can be accessable the if block variable ---->",blockOrGlobal)

def blkOrGlb():
   scope = "Block"
# blkOrGlb() 
# print("checking can be able to access the fucntion block variable---->", scope) # we will get an NameError because we trying to access the function variable 

def createGlobalVariable():
   global scope
   scope = "This one is a Global Variable"
createGlobalVariable()
print("checking can be able to access the fucntion block variable---->", scope) # this will also throw an Error because the function is still not excuted 

