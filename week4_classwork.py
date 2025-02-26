# map and Filter 
def FilterOdd (list1):
    odd_list = list(filter(lambda x: x % 2 != 0, list1))
    return odd_list

given_list = [10, 15, 22, 33, 47, 50]
odd_list = FilterOdd (given_list)
print (odd_list)

sum_odd = 0
for num in odd_list:
    sum_odd += num

print ("Sum of odd numbers:", sum_odd)
    
    
# File Handling
with open ("file.txt", "w") as f:
    f.write("This is a new file created by me! Thanks for reading!")


word_count = 0
with open ("file.txt", "r") as f:
    for i in f:
        words = i.split()
        word_count += len (words)

print ("Word Count:", word_count)

