#In Python there are 3 types of numeric values

# int ( INTEGER)

#  which is whole number that can be + - 
# example:
age = 26
print(type(age))

# float which is decimal numbers(like 434.03938) that can be + - 

weight = 68.52
print(type(weight))

#  small calculation by using float and integer
height_cm = 168
height_mt = 1.68

BMI = weight/(height_mt *height_mt)
print(BMI,type(BMI))
meter = height_mt * height_mt
BMI = weight / meter
absBmi = round(BMI)
# BMI= int(BMI)
print("bbbb",absBmi,type(absBmi))
print(BMI,type(BMI))

decimalvalue_2 = "%.2f" % BMI  # we want only 2 values after . 
decimalvalue_1= "%.1f" % BMI # we want only 2 values after . 
decimalvalue_3= "%.3f" % BMI # we want only 3 values after .
print(decimalvalue_1, decimalvalue_2, decimalvalue_3)
print(type(decimalvalue_1), type(decimalvalue_2), type(decimalvalue_3)) # all are will be a string 

# Concept Behind "%.nf" % number
# is an example of string formatting in Python using the old-style string formatting (% operator).

"""
"%.2f": This is a format specifier.
. -> Indicates that we are specifying the number of decimal places.
2 -> Specifies that we want 2 decimal places.
f -> Stands for floating-point number.
"""
"""
2. Applying It to a Number
When the % operator is used, it replaces the format specifier with the given number, rounding it to the specified decimal places.

"%.2f" % 1.2399
The number 1.2399 is rounded to two decimal places.
1.2399 rounded to 2 decimal places = 1.24
"""

# try another way

print("************: ",len('%-15s' % "Raj"))

import random
print(random.random()) # random float value will be given by this function
print(random.randint(2,5)) # from 2 to 5 random value will be given by this function 
print(random.randrange(8)) # random value will be given by this function upto 8


# type convetertion

age = 26.3
weight = 68
height_cm = 164j
print(age, weight, height_cm)
print(type(age), type(weight), type(height_cm))
age = int(age)
weight = float(weight)
newComplex = complex(age)
# newfloat = float(height_cm) # we will ge the type error becoz we can't change the complex type
print(age,weight,newComplex)
print(type(age),type(weight),type(newComplex))