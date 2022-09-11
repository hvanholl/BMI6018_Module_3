### ASSIGNMENT 3: HANNAH VAN HOLLEBEKE u0697848 --------------------
print("Assignment 3")

### Problem 1 ------------------------------------------------------

# create list of at least 10 integers, ranging from zero to nine.
one_a = [3, 4, 1, 5, 4, 2, 8, 1, 1, 3, 5, 7, 3]
print("one_a: " + str(one_a) + " Length: " + str(len(one_a)))

# Add 3 to the fifth index. Insert method arguments (index, value). Changes original list.
#one_b = one_a[4] += 3
one_a.insert(5,3)
print("one_b: " + str(one_a))

# List comprehension. Iterates though list to create a new list with a different name. converts each integer to float as it iterates.
one_c = [float(x) for x in one_a]
print("one_c: " + str(one_c))

# convert to set which results in a unique set of values from list, unordered (but it is coming out ordered). 
one_d = set(one_c)
print("one_d: " + str(one_d)  + " " + str(type(one_d)))

# Method to add an integer to set. set can have different data types. Value added to the end of set. Is this supposed to happen?
one_d.add(10)
print("one_e: " + str(one_d))

# Pop an item from a set. Will take an out of the set. Random? but removing the first value everytime it is run. 
one_d.pop()
print("one_f: " + str(one_d))

# count items in set
print("one_g: Length of set one_f is " + str(len(one_d)))

# Are the lengths of the list and set the same? True or False
print("one_h: Is the length of the set the same as the list? " + str(len(one_c) == len(one_d)))

# coerce the set to a list and add new list to list one_a
one_i = list(one_d) + one_a
print("one_i: " + str(one_i))

# coerce one_i to set
one_j = set(one_i)
print("one_j: " + str(one_j))

# count elements in new set. Increased by one because now popped value is included in set, but as an integer, because it was in the original list. 
print("one_k: Length of set one_j is " + str(len(one_j)))

### PROBLEM 2 -----------------------------------------------------

# Pre-defined dictionary variables
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

# Create dictionary by combining three dictionaries in one. 
# Key is individual dictionary variable. Value is the variable. 
two_a = {"two_patient_dictionary_kinoko":two_patient_dictionary_kinoko, 
    "two_patient_dictionary_dango":two_patient_dictionary_dango, 
    "two_patient_dictionary_mochi":two_patient_dictionary_mochi}
print("two_a: " + str(two_a))

# Select name of Dango. First select outer dictionary key, then select inner dictionary key.
two_b = two_a['two_patient_dictionary_dango']['name']
print("two_b: " + str(two_b))

# Change the value of one of the keys. Use the nested key selection and assign it the desired value.
two_a['two_patient_dictionary_mochi']['year'] = 2018
print("two_c: " + str(two_a))

# Create dictionary with names as keys and year as values.
two_d = {'Kinoko':2021, 'Dango':2019, 'Mochi':2019}
print("two_d: " + str(two_d))

# Create a list of the dictionary keys. Keys method for dict data type. 
two_e = list(two_d.keys())
print("two_e: " + str(two_e))

# Create a list of the dictionary values. Values method for dict data type. 
two_f = list(two_d.values())
print("two_f: " + str(two_f))

# Make these a dictionary again. Zip function to combine the two lists in order as keys and values. 
two_g = dict(zip(two_e, two_f))
print("two_g: " + str(two_g))

## PROBLEM 3 ------------------------------------------------
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

# is e a subset of a
three_a = three_setE.issubset(three_setA)
print("three_a: Is setE a subset of SetA? " + str(three_a))

# is E a strict subset of A. E is not equal to A
three_b = three_setE < three_setA
print("three_b: Is SetE a strict subset of SetA? " + str(three_b))

# Intersection of A and B
three_c = three_setA.intersection(three_setB)
print("three_c: A and B intersection " + str(three_c))

# Union of C, D, and E
three_d = three_setC.union(three_setD, three_setE)
print("three_d: C, D, and E union " + str(three_d))

# Add 9 to set. 9 is already in the set so it will not change.
three_d.add(9)
print("three_e: " + str(three_d))

##PROBLEM 4 -------------------------------------------------------
# Create a variable of type int with the value of 8
four_a = 8
print("four_a: " + str(four_a))

# Create an empty list 
four_b = []
print("four_b: Empty list " + str(four_b))

# Using type(), add the type of four_a to this list.
four_b.append(type(four_a))
print("four_c: " + str(four_b))

# Add 0.39 to four_c. 
four_b.append(0.39)
print("four_d: " + str(four_b))

# Append the type of 0.39 to the list
four_b.append(type(four_b[1]))
print("four_e: " + str(four_b))

# Exponentiate to the -10, round it to no decimal places, append to list.
four_f = four_b.append(round(four_b[1]**-10))
print("four_f: " + str(four_b))

# Append the type to the list
four_b.append(type(four_b[3]))
print("four_g: " + str(four_b))

# Problem 5 -----------------------------------------------------

# Dictionary with index as key and list item as value 
five_a = dict(zip(range(0,len(four_b)), four_b))
print("five_a: " + str(five_a))

# Add integer 300 to the list as a string type
four_b.append(str(300))
print("five_b: " + str(four_b))

# Add the type of 300, index 5, to four_b
four_b.append(type(four_b[5]))
print("five_c: " + str(four_b))

# Set index 5 as the first two characters from index 5
four_b[5] = four_b[5][:2]
print("five_d: " + str(four_b))

# Append the type of four_b index five to the list
four_b.append(type(four_b[5]))
print("five_e: " + str(four_b))

# List comprehension to iterate over index 5 in list and convert to integer
five_f = [int(x) for x in four_b[5]]
print("five_f: " + str(five_f))

# Add the type of five_f to list
four_b.append(type(five_f))
print("five_g: " + str(four_b))

# Add type of three_setA to list
four_b.append(type(three_setA))
print("five_h: " + str(four_b))