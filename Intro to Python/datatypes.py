#Set a string variable, print and verify type.
string1 = "Dogs are a man's best friend."
print("The 'string1' variable = " + string1)
type_string = str(type(string1))
print("The 'string1' variable is " + type_string)
print()

#Set an integer variable, print and verify type.
integer1 = 12345
#Convert integer to string for concatenation.
print("The 'integer1' variable = " + str(integer1))
type_int = str(type(integer1))
print("The 'integer1' variable is " + type_int)
print()

#Set a float variable, print and verify type.
float1 = 1234.5678
#Convert float to string for concatenation.
print("The 'float1' variable = " + str(float1))
type_float = str(type(float1))
print("The 'float1' variable is " + type_float)
print()

#Set a boolean variable, print and verify type.
bool1 = 3 == 3
#Convert boolean to string for concatenation.
print("The 'bool1' variable = " + str(bool1))
type_bool = str(type(bool1))
print("The 'bool1' variable is " + type_bool)
print()

#Set a list variable, print and verify type.
list1 = ["item1","item2","item3"]
#Convert list to string for concatenation.
print("The 'list1' variable = " + str(list1))
type_list = str(type(list1))
print("The 'list1' variable is " + type_list)
print()

#Set a tuple variable, print and verify type.
tuple1 = ("item1",12345,"item3")
#Convert tuple to string for concatenation.
print("The 'tuple1' variable = " + str(tuple1))
type_tuple = str(type(tuple1))
print("The 'tuple1' variable is " + type_tuple)
print()

#Set a dictionary variable, print and verify type.
dict1 = {"location":"MN","status":"working","caffeine_level":"low"}
#Convert dictionary to string for concatenation.
print("The 'dict1' variable = " + str(dict1))
type_dict = str(type(dict1))
print("The 'dict1' variable is " + type_dict)
print()

#Access first item in list1
print("The first item in 'list1' is " + list1[0])
print()

#Access third item in tuple1
print("The first item in 'list1' is " + tuple1[2])
print()

#Access the location value in dict1
print("The location value in 'dict1' is " + dict1["location"])
print()
