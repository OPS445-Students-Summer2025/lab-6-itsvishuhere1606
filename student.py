#!/usr/bin/env python3
# Author ID: vishesh1

class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        gpa = 0.0
        for course in self.courses.keys():
            gpa = gpa + self.courses[course]
        print('GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses)))
