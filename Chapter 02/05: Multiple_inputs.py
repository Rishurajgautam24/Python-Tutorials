# name = input("What is your name? ")
# age = int(input("How old are you? "))

# print("Hello", name, "you are", age, "years old.")
# print("Hello "+ name + " you are " + str(age) + " years old.")


#  Multiple inputs in one line
# Space separated inputs
# name,age = input("Enter your name and age: ").split()
# print(name)
# print(age)


# comma separated inputs

# name,age = input("Enter your name and age: ").split(",")
# age=int(age)
# print(name)
# print(age)
# print(type(age))

# Separated by "|"

name,age = input("Enter your name and age: ").split("|")
age=int(age)
print(name)
print(age)
print(type(age))

