# Basic calculator using function 
def Addition (a, b):
    return a + b

def Subtraction (a, b):
    return a - b

def Multiplication (a, b):
    return a * b

def Division (a, b):
    return a / b

print ("""Operations available:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Divison 
       """)

choice = int (input("Enter a number (1-4) for operation to perform: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (choice == 1):
    print ("Sum:", Addition(num1, num2))
elif (choice == 2):
    print ("Subtraction:", Subtraction(num1, num2))
elif (choice == 3):
    print ("Multiplication:", Multiplication(num1, num2))
elif (choice == 4):
    print ("Division:", Division(num1, num2))
else:
    print ("Invalid option!")




# Dictionary
students = {
    "Sajjan" : 90,
    "Swachchha" : 78,
    "Subekshya" : 40,
    "Sujit" : 92,
    "Shija" : 93,
    "Swojan" : 20,
}

# Student with highest marks
highest = 0 
for key, value in students.items():
    if (value > highest):
        highest = value

print (f"Highest marks is {highest}")

# Remove students who scored below 50
remove_keys = []
for key, value in students.items():
    if (value < 50):
        remove_keys.append(key)

for i in remove_keys:
    students.pop(i)

print ("Marks above 50:", students)

# Sort dictionary in descending order based on marks
descending = sorted(students.items(), key = lambda item: item[1], reverse = True)
descending_dict = dict(descending)
print ("Dictionary in descending order:", descending_dict)

