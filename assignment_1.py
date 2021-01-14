# Receive from user 3 inputs: Name, Age, Work
# Check if Name starts with "A". If not, keep asking for the name input
# Check if Age is a number and print result

name = ""  # add variable for name
while not name.startswith("A"):  # Check name starts with "A"
    name = input("Enter name: ")

age = input("Enter age: ")
if age.isdigit():  # Check Age is a number
    print("It is number")
else:
    print("It is not a number")
work = input("Enter work: ")
print(name + " is " + str(age) + " years old and works as: " + work)
