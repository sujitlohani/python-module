import random

"""Create a class called Student with attributes name, age, and grades (a list of integers). 
Write a method average_grade that calculates and returns the average grade of the student. Create three Student objects and print their average grades.
"""
class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def average_grade(self):
        if not self.grades:
            print (f"{self.name}'s grades has not been entered!")
            return 0
        
        count = len (self.grades)
        total = 0
        for grade in self.grades:
            total += grade

        avg_grade = total / count
        return avg_grade

student1 = Student ("Sujit", 20)
student2 = Student ("Sajjan", 23)
student3 = Student ("Swojan", 21)

student1.grades = [88, 89, 93]
student2.grades = [74, 61, 83]
student3.grades = [85, 96, 75]

print (f"{student1.name}'s average grade is {student1.average_grade()}")
print (f"{student2.name}'s average grade is {student2.average_grade()}")
print (f"{student3.name}'s average grade is {student3.average_grade()}")




"""Create a class called Book with attributes title, author. Write a method short_title that returns the first 10 characters of the book's title. 
Create three Book objects and print their short titles.
"""
class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def short_title(self):
        if not self.title:
            print ("The book has no recorded title")
        
        shortened = ""
        for char in range(min (10, len (self.title))):
            shortened += self.title[char]
        return shortened
    
book1 = Book ("Harry Potter and the Sorcerers Stone", "J.K. Rowling")
book2 = Book ("One P", "Eiichiro Oda")
book3 = Book ("Goosebumps: Haunted Halloween", "R.L. Stine")

print (f"{book1.title}'s shortened version is {book1.short_title()}")
print (f"{book2.title}'s shortened version is {book2.short_title()}")
print (f"{book3.title}'s shortened version is {book3.short_title()}")




"""Create a class called StudentResult with attributes name, age, and average_grade and include a method has_passed that returns True if the student's average grade is 50 or higher, 
and False otherwise. Create three Student objects and print the names of the students who have passed.
"""
class StudentResult:
    def __init__ (self, name, age, avg_grade):
        self.name = name
        self.age = age
        self.avg_grade = avg_grade

    def has_passed(self):
        
        if self.avg_grade >= 50 and self.avg_grade <= 100:
            return True
        elif self.avg_grade < 50 and self.avg_grade > 0:
            return False
        else:
            print (f"{self.name}'s grades are invalid!")

student1 = StudentResult ("Sujit", 20, 95)
student2 = StudentResult ("Sajjan", 23, 101)
student3 = StudentResult ("Swojan", 21, 21)

print (f"{student1.name}'s pass status: {student1.has_passed()}")
print (f"{student2.name}'s pass status: {student2.has_passed()}")
print (f"{student3.name}'s pass status: {student3.has_passed()}")




"""Create a class called ShoppingCart with a list attribute items (each item is a dictionary with keys name and price). 
Write a method total_price that calculates and returns the total price of all items in the cart. Create a ShoppingCart object, add five items to it, and print the total price.
"""
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, name, price):
        if price < 0:
            print (f"Invalid price for {name}")
        else:
            self.items.append({"name": name, "price": price})

    def total_price (self):
        total = 0
        for item in self.items:
            total += item ["price"]
        return total
    
cart = ShoppingCart()
cart.add_items ("Milk", 100)
cart.add_items ("KitKat", 120)
cart.add_items ("Airpods", 5500)
cart.add_items ("Chips", 200)

print (f"The grand total of items in the shop is Rs.{cart.total_price()}")



"""Create a class called TextAnalyzer with a string attribute text. Write a method word_count that returns the number of words in the text.
Create a TextAnalyzer object with a sample text and print the word count
"""
class TextAnalyzer:
    def __init__ (self):
        self.string = "" 

    def add_text(self, words):
        if words:
            if self.string:
                self.string += " " + words
            else:
                self.string = words


    def word_count(self):
        words = self.string.split()
        return len (words)
    
text = TextAnalyzer()
text.add_text ("Hello I am")
text.add_text ("I am testing")
text.add_text ("this method")

print ("The count of words in the string is", text.word_count())



"""Create a class called Playlist with a list attribute songs (each song is a dictionary with keys title and artist). 
Write a method shuffle that randomly shuffles the songs in the playlist. Create a Playlist object, add five songs to it, shuffle the playlist, and print the shuffled list of songs.
Hint : 
Use random.shuffle(list_varible) to shuffle (preq. import random)
Use loop to print the shuffled songs with title and artist
"""
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist):
            self.songs.append({"title": title, "artist": artist})

    def shuffle(self):
        random.shuffle(self.songs)

    def display_songs (self):
        for song in self.songs:
            print(f"Title: {song['title']}, Artist: {song['artist']}")
    
playlist = Playlist()

playlist.add_song("Great Gig in the Sky", "Pink Floyd")
playlist.add_song("Kashmir", "Led Zeppelin")
playlist.add_song("Nutshell", "Alice in Chains")
playlist.add_song("Lovers Rock", "TV Girl")
playlist.add_song("Save Your Tears", "The Weeknd")

playlist.shuffle()
playlist.display_songs()