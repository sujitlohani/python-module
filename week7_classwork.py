class Student:
    def __init__ (self, name, studentid):
        self.name = name
        self.student_id = studentid
        self.courses = []

    def add_course (self, course):
        if course in self.courses:
            print (f"{course} is already enrolled")
        else:
            self.courses.append(course)
            print (f"{course} has been added successfully!")

    def remove_course (self, course):
        if course in self.courses:
            self.courses.remove(course)
            print (f"{course} removed successfully!")
        else:
            print (f"{course} doesn't exist in the list")

    def display_courses (self):
        if not self.courses:
            print (f"{self.name} is not enrolled in any courses")
        else:
            print(self.name, "is enrolled in:", ", ".join(self.courses))

student1 = Student("Sujit", 999)
student1.add_course ("Computer")
student1.add_course ("Physics")
student1.display_courses()

student1.remove_course ("Physics")
student1.display_courses()

student1.add_course("Python")
student1.display_courses()