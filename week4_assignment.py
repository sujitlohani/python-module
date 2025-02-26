""" Write a Python function read_file_content(file_path) that takes the path of a text file as input and returns its content as a string.
Write another function write_to_file(file_path, content) that takes a file path and a string content as input and writes the content to the file
"""
# C:\Users\Sujit\OneDrive\Desktop\Python Module Assignment\file.txt
def read_file_content (file_path):
    content = ""
    with open (file_path, "r") as f:
        for i in f:
            content += i
    return content 

def write_to_file(file_path, content):
    with open (file_path, "w") as f:
        return f.write(content)
        
path_input = input ("Enter path to file: ")
input_content = input ("Enter content to enter: ")

write_to_file (path_input, input_content)
print (read_file_content(path_input))




""" Write a function find_longest_word(file_path) that reads a text file and returns the longest word in the file. """
def find_longest_word (file_path):
    longest_word = ""
    with open (file_path, "r") as f:
        for lines in f:
            words = lines.split()
            for word in words:
                if (len(word) > len(longest_word)):
                    longest_word = word
                
    return longest_word

print ("Longest word is ", find_longest_word(path_input))




"""Write a function check_file_empty(file_path) that takes a file path as input and returns True if the file is empty, and False otherwise."""
def check_file_empty (file_path):
    with open (file_path, "r") as f:
        if not f.read(1):
            return True
    return False

print (check_file_empty (path_input))




"""Write a function reverse_file_content(file_path) that reads a text file and writes its content in reverse order to a new file named reversed.txt."""
def reverse_file_content (file_path):
    with open (file_path, "r") as f:
        content = f.read()
        reversed_content = content [::-1]

    with open("reversed.txt", "w") as f:
        f.write(reversed_content)

reverse_file_content (path_input)
print ("Reversed content is in reversed.txt")




""" Write a Python function convert_to_uppercase that:
        Accepts a list of strings.
        Uses a lambda function inside map() to convert all strings in the list to uppercase.
        Return the list of uppercase strings.
"""
def convert_to_uppercase (input_list):
    uppercase_list = list (map (lambda x: x.upper(), input_list))
    return uppercase_list

input_list = []
n = int (input("Enter number of elements to add in list: "))
for i in range(n):
    words = input (f"Enter word {i+1}: ")
    input_list.append (words)

print ("Uppercase list:", convert_to_uppercase(input_list))




"""Write a Python function filter_even_length_words that:
        Accepts a list of strings.
        Uses a lambda function inside the filter() function to return only words that have an even length.
"""
def filter_even_length_words (input_list):
    even_length = list (filter (lambda x: len(x) % 2 == 0, input_list))
    return even_length

print ("Words that have even length:", filter_even_length_words(input_list))




"""Write a function process_file_with_lambda that:
Takes a file name as input.
Reads each line from the file and uses a lambda function to convert each word in the line to uppercase.
Write the processed lines back to the file.
"""
def process_file_with_lambda(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        processed_line = " ".join(map(lambda word: word.upper(), line.split()))
        processed_lines.append(processed_line)

    with open(file_path, "w") as f:
        for processed_line in processed_lines:
            f.write(processed_line + "\n")

process_file_with_lambda(path_input)
print("The file has been processed and updated.")









        