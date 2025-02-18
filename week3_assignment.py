"""Write a function count_vowels(text) that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
The function should be case insensitive (i.e., treat uppercase and lowercase letters the same).
"""
def count_vowels(text):
    text = text.lower()
    vowels_list = "aeiou"
    found_vowels = []
    vowel_count = 0
    for char in text:
        if char in vowels_list:
            vowel_count += 1
            found_vowels.append(char)

    return vowel_count, found_vowels

word = input("Enter a word: ")
count, vowels = count_vowels(word)
print("Vowel count:", count)
print("Vowels:", ",".join(vowels))



""" Write a function find_maximum(list1) that takes a list of numbers as input and returns the maximum number from the list. (Do not use the built-in max() function)."""
def find_maximum(list1):

    if not list1:
        return None

    maximum = list1[0]
    for i in list1:
        if (i > maximum): 
            maximum = i
    return maximum

list1_input = list(map(int, input("Enter numbers separated by spaces: ").split()))
max_number = find_maximum(list1_input)
print ("Maximum number:", max_number)



""" Write a function multiplication_table(n) that takes a number n as input and prints the multiplication table of n from 1 to 10. """
def multiplication_table(n):
    for i in range (1, 11):
        product = n * i
        print (f"{n} x {i} = {product}")

num = int (input("Enter a number: "))
multiplication_table(num)



""" Write a function largest_word(sentence) that takes a sentence as input and returns the longest word in the sentence. 
If there are multiple words of the same length, return the first one that appears.
"""
def largest_word (sentence):
    words = sentence.split()
    if not words:
        return None
    
    largest = words[0]
    for i in words:
        if (len(i) > len(largest)):
            largest = i
    return largest
        
sentence = input ("Enter a sentence separated by spaces: ")
largest = largest_word(sentence)
print ("Largest word:", largest)



""" Write a function sum_of_list(numbers) that takes a list of numbers as input and returns the sum of all elements in the list. (Do not use the built-in sum() function)."""
def sum_of_list(numbers):
    if not numbers:
        return None
    
    sum = 0
    for i in numbers:
        sum += i

    return sum

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print ("Sum of all elements in list:", sum_of_list(numbers))



"""Write a function to_title_case(sentence) that takes a sentence as input and returns the sentence in title case, where the first letter of each word is capitalized."""
def to_title_case(sentence):
    words = sentence.split()
    if not words:
        return None
    
    new_words = [word.capitalize() for word in words]
    new_sentence = " ".join(new_words)
    return new_sentence

input_sentence = input ("Enter a sentence: ")
print ("New sentence:", to_title_case(input_sentence))



"""Write a function is_palindrome(word) that takes a string as input and returns True if the word is a palindrome (reads the same forward and backward), otherwise returns False."""
def is_palindrome(word):
    reversed_word = "".join(reversed(word))
    if (word == reversed_word):
        return True
    else:
        return False

word = input ("Enter a word: ")
print (is_palindrome(word))



"""Write a function char_count(s) that takes a string as input and returns a dictionary where keys are the characters and values are their frequencies in the string."""
def char_count(s):
    frequency = {}

    for i in s: 
        if (i in frequency):
            frequency[i] += 1
        else:
            frequency[i] = 1
    
    return frequency

word = input("Enter a string: ")
print (char_count(word))





    

    
