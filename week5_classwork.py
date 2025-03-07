"""WAP to create a function that takes a list of numbers as parameters and 
1. prints the square of each number
2. prints the square of number only if the square is an even number
3. store even square number in another list"""

def SquareNum(list1):
    for num in list1:
        square = num ** 2
        print (f"Square of {num} is: {square}")

def EvenSquareNum(list1):
    for num in list1:
        if num % 2 == 0:
            square = num ** 2 
            print (f"Square of even {num} is: {square}")

def EvenSquareList(list1):
    even_list = []
    for num in list1:
        if num % 2 == 0:
            square = num ** 2 
            even_list.append(square)

    return even_list


list_input = list(map(int, input("Enter numbers separated by spaces: ").split()))

print (f"Input list: {list_input}")
SquareNum(list_input)
EvenSquareNum(list_input)
print (f"New list of even square is: {EvenSquareList(list_input)}")

    

            