""" Write a Python program that takes a list of numbers and:
Print the numbers in the list but skip numbers that are divisible by 5.
Stops the loop if a number greater than 50 is encountered. 
"""
num_list = []
for i in range (1, 11):
    num = int (input("Enter an integer: "))
    num_list.append(num)
for i in num_list:
    if (i > 50):
        break
    elif (i % 5 == 0):
        continue
    print (i)



""" Write a Python program that takes a password as input and checks its strength based on the following conditions:
Weak: If the password is less than 6 characters or only contains letters.
Moderate: If the password has at least 6 characters and contains both letters and numbers.
Strong: If the password has at least 8 characters, contains letters, numbers, and special characters (@, #, $, %, &). 
"""
special_char = "@#$%&"
has_char = False
has_num = False
has_special = False

password = input ("Enter your password: ")
# creating variables that check conditions 
for i in password:
    if ("a" <= i <= "z" or "A" <= i <= "Z"):
        has_char = True
    elif ("0" <= i <= "9"):
        has_num = True
    elif i in special_char:
        has_special = True

if (len(password) < 6 or (not has_num and has_char and not has_special)):
    print ("Weak")
elif (len(password) >= 6 and has_num and has_char and not has_special):
    print ("Moderate")
elif (len(password) >= 8 and has_num and has_char and has_special):
    print ("Strong")
else:
    print ("Invalid password!")



""" Write a Python program that takes a string as input and returns a new string where every alternate word is reversed while keeping the order of the words intact.
Example Input/Output:
Input: "Python is an amazing programming language"
Output: "Python si an gnizama programming egaugnal” 
"""
sentence = input ("Enter a sentence: ")
words = sentence.split()

for i in range(0, len(words), 2):  
    words[i] = words[i][::-1]


print("Output:", " ".join(words))


""" Write a Python program that takes a list of words and finds all words that appear more than once, storing them in a dictionary with their frequency count.
Example Input/Output:
Input: ["apple", "banana", "apple", "orange", "banana", "banana"]
Output: {'apple': 2, 'banana': 3} 
"""
list_word = ["apple", "banana", "grapes", "apple", "apple", "mango", "banana", "apple","banana","mango"]
count_word = {}

for word in list_word:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1

repeated = {word: count for word, count in count_word.items() if count > 1}
print ("Output: ", repeated)


""" Create a dictionary called books where the keys are book titles (strings) and the values are the number of copies available for each book (integers). For example:
books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10,  # You can add more books
}
Write a Python program that does the following:
Prompts the user to enter the name of the book they want.
Prompts the user to enter the number of copies they want to buy.
Checks if the book exists in the books dictionary.
Prints the following messages based on availability:
"Available": If the book is in the dictionary and there are enough copies to fulfill the user's request.
"Partially Available": If the book is in the dictionary, but there are fewer copies than the user wants.
"Unavailable": If the book is not in the dictionary.
Important: Your program should handle the case where the user might enter something that is not a valid number of copies (e.g., letters, a blank input). Provide a clear message to the user if this happens and ask for number of copies again if the input by user is not an integer type
"""
books = {
    'Book1' : 5,
    'Book2' : 6,
    'Book3' : 2,
    'Book4' : 7,
    'Book5' : 4,
}

book = input ("Enter name of book you want: ")
if book in books:
    while True:
        copies = input ("Enter number of copies you want to buy: ")
        if (copies.isdigit() and int(copies) > 0):
            copies = int(copies)
            break
        else:   
            print ("Invalid entry! enter a valid number")
    
    if copies <= books[book]:
        print("Available")
    elif copies > books[book]:
        print("Partially Available")
    
else:
    print ("Unavailable")
    


""" Write a program in python which takes a list of words as input and store the frequency of each word in dictionary  
Input [“This”,”is”,”good”,”is”]
Output {“this”:1,”is”:2} 
"""
sentence = input ("Enter a sentence: ").split()
count_word = {}

for word in sentence:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1

print ("Output: ", count_word)
