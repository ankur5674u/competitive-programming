__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '02-19-2020'

"""https://www.techgig.com/practice/question/dlA4ZjNCTE1kNmdtbzlybWwwRzNkZz09#"""

from collections import namedtuple


def main():
    Student = namedtuple('Student', ['marks', 'name'])
    number_of_student = int(input())
    student = []
    header = input().split()
    for i in range(number_of_student):
        data = tuple(input().split())
        if data[0].isdigit():
            student.append(Student(data[0], data[1]))
        else:
            student.append(Student(data[1], data[0]))
    average_marks = round(sum([int(s.marks) for s in student]) / len(student), 2)
    print(average_marks, end="")
