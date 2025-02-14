# Write a Python script that:
# Asks the user to enter a decimal number (float).
# Converts the number into an integer and a string.
# Displays all three values (original float, integer, and string) using string formatting
num = float (input("Enter a number: "))

integer_num = int (num)
string_num = str (num)

print ("Original Input:", num)
print ("Conversion to integer:", integer_num)
print ("Conversion to string:", '"'+ string_num+'"')


# Write a program that:
# Ask the user for their full name.
# Extracts the first letter of the first and last name using string slicing.
# Displays the initials in uppercase.
name = input("Enter your full name: ")

parts = name.split()
if len (parts) >= 2:
    initials = parts[0][0].upper() + "." + parts[1][0].upper()
    print ("The initials are: ", initials )


# Write a program that:
# Takes a string input from the user.
# Uses string slicing to reverse it.
# Prints the reversed string.
value = input("Enter a string: ")
reversed_val = value[::-1]
print ("Reversed string is:", reversed_val)


# Write a program that:
# Asks the user to enter a word and a starting index.
# Extracts and prints the substring from that index to the end using string slicing.
word = input("Enter a word: ")
starting_index = int(input("Enter a starting index: "))

if starting_index < len(word):
    print ("Substring from", starting_index,  "is:", word[starting_index:])
else:
    print ("Invalid index, try again!")


# Write a Python script that:
# Asks the user to enter an email address.
# Extracts the domain name (part after @) using string slicing.
# Prints the extracted domain.
email = input ("Enter an email: ")

if '@' in email:
    domain = email.split("@")[-1]
    print ("Domain:", domain)
else:
    print("Invalid email, try again!")


# Write a Python program that:
# Takes a word as input.
# Swaps its first and last character using string slicing.
# Displays the new word.
word = input ("Enter a word: ")

if len(word) > 1: 
    new_word = word[-1] + word[1:-1] + word[0]
    print ("Swapped word:", new_word)
else:
    print ("word must have atleast two characters!")



