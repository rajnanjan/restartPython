
"""
---> Lists are used to store multiple items in a single variable
---> Lists are one of 4 built-in data types in Python used to store collections of data, 
     the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage 
---> Lists are created using square brackets,
---> List items are ordered, changeable, and allow duplicate values.
"""

nos = [12,13,14,15,16,17,18,19,20] # list
invoices = ['inv100', 'inv101', 'inv102', 'inv103', 'inv104', 'inv105', 'inv106',]
active= [False,True,False,False,False,False]


# accessing the list 
"""
---> List items are indexed, so via index we can able to access the elements which are present in the list
---> for loop iteration we can access the elements which are present in the list
---> List items are ordered means oreder will notchanged, 
---> and we can modify the list means changeable, and allow duplicate values.
"""
print(nos[0]) # access the first element of the list 
print(nos[-1]) # accessing the last element of the list
print(nos[len(nos)-1]) # accessing the last element of the list

print("LENGTH OF the list", len(nos)) # length of the list
print(type(nos)) # type of the list


"""
---> and we can use the constructor to create a list
"""

compant_name = list(("raj","siddu","stage")) # node should be use the (()) paranteses
print(compant_name) 




# removing the given value from the list
places = ["kozhikode","kochi", "munnar", "bengaluru","coimbatore", "kozhikode","kochi","munnar","bengaluru", "kozhikode"]
removeplace = "kozhikode"
for place in places:
    if removeplace == place:
        places.remove(place)
        print (place)
print(places)
places.sort() #ascending order
print(places) 
places.sort(reverse=True) #reverse order
print(places)

# adding the elements 
places.append("mysore")
print(places)

copyPlaces = places.copy() # copy the list
print("copy lists ", copyPlaces)
placeName = "Bengaluru"
mysorecount = copyPlaces.count(placeName)
print(mysorecount)

# Change list elements

drinks = ["cock", "pepsi","mango"];

drinks[0] = "lemon" # changein the element based on the index 
drinks[0:3] = ["apple", "orange","grapes","saptota"] # changin the element based on the range of index
drinks[-1] = ["kiwi", "dragon fruits"] # if we mention only index value then ans will be  ['apple', 'orange', 'grapes', ['kiwi', 'dragon fruits']]
drinks[2] = ["kiwi", "dragon fruits"] # if we mention only index value then ans will be ['apple', 'orange', ['kiwi', 'dragon fruits'], ['kiwi', 'dragon fruits']]
print(drinks)
drinks[0:3] = ["pineapple", "muskmelon"] # we can mention the range of value from 0 to 3 means  4 values insetead of 4 we are adding only 2
drinks[0:3] = "orange" # in this case each character will be consider as elements ans : ['o', 'r', 'a', 'n', 'g', 'e'] we are trying to spread the value and assgin in the list

# insert function

# drinks.insert("coconut")  # it will throw the Type error becoz we have mention the index where value needs to be inserted 
drinks.insert(1,"coconut") 

# insert function wont be replace the previous list element


# append function

drinks.append("butterfruit") # add the element in the end of the list 
# drinks.append(1,"butterfruit") # append function will take only one argument

# Extend List
colddrinks = ["pepsi","cocacola","miranta","fanta"]
drinks.extend(colddrinks) # it will add the colddrink elments to the drink list

# we can add the any Iterable value

drinks.extend("charcters") # stings alse iterables each charcter consiter as elements

print(drinks)

# Remove List Items

# Remove functions
"""
remove function will remove the given element from the list; only frist accurance value 
"""

removedelement = drinks.remove("coconut") # remove functio wont the return the removed value
print(removedelement)

# POP function
drinks.pop() #  it will remove the last element if we are not mentioning the index value 
print(drinks)
drinks.pop(1) #  it will remove the last element if we are not mentioning the index value 
removeValue = drinks.pop(1) # pop function will return the removed value 
print(removeValue)

print(drinks)
# deletedValue = del drinks[1] we can assign the del function response
del drinks[1] # del function will delete the element based on the given index value
print(drinks)
# del drinks
# print(drinks) # it will throw the name error becoz drinks list is deleted now we trying to access the list 
drinks.clear() # this will clear the list 
print(drinks) # it will return the empty list 

# looping the list 
"""
for loop 
while loop
"""

# for loop we can acchieve with elements and index value based on the below 
cars = ["swift","dzire","polo","i10","i20","santro"]

for car in cars: # accessing via elements
    print(car) # it will return the each cars elements

for i in range(len(cars)): # accessing via index value
    print(cars[i]) # it will return the i index elements in the car list


# while loop 

i = 0
while i < len(cars):
    print("from While loop",cars[i]) # it will return the i index elements in the car list
    i += 1 # increment the i value 
    # i++ this increments it wont work in python

# example 2
j = 0
while (True):
    if(j < len(cars)): 
     print(cars[j])
     j += 1
    else:
        break # break


# sorts function 
cars.sort()
sortedList = cars
sortedList1 = cars.sort() # sort function will return None
print("sortedList", sortedList)
print("sortedList1", sortedList1)


# sorting in descending order or reversed

cars.sort(reverse= True) # order the elements in descending order
reversedList = cars
print("reversedList", reversedList)

