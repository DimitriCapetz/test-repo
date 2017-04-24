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
