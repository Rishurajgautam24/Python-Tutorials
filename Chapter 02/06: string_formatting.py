#  String Formatting
#  String formatting lets you inject items into a string rather than trying to chain items together using commas or string concatenation. As a quick comparison, consider:

name = "Rishu"
age = 22

print("Hello"+ name + "you are" + str(age) + "years old.")
print("Hello", name, "you are", age, "years old.") #ugly looking

#  This is a valid way of formatting a string, but it's not the preferred way. You can use the %s operator to format a string. The %s operator lets you add a value into a string via substitution. The %s operator will replace %s with the value that follows it. For example:

# in python 2.7

# print("Hello %s you are %s years old." % (name, age))

# in python 3 {.format()} is used
print("Hello {} you are {} years old.".format(name, age))


# in python 3.6 f-string is used

print(f"Hello {name} you are {age} years old.") 

# this is the best way to format a string in python 3.6

#  No need to worry about type whether it is in string or integer. It will automatically convert it into string.


