# Ask user to take 3 digits as input and then print the average of those 3 numbers. Using String formatting.

#  Manually 

# num1= input("Enter the first number: ")
# num2= input("Enter the second number: ")
# num3= input("Enter the third number: ")

num1, num2, num3 = input("Enter three numbers separated by comma: ").split(",")

# average = (int(num1) + int(num2) + int(num3)) / 3

# print(f"The average of three numbers is: {average}")
print(f"The average of three numbers is: {(int(num1) + int(num2) + int(num3)) / 3}")

# Bonus - Try taking all inputs comma separated in one line.