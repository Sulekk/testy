# -*- coding: utf-8 -*-
"""students.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l3Ra__w1D51GasYgtuQeZKrttGyWVx81
"""

import json

# Zapisywanie do pliku
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Wczytywanie z pliku
def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Operacje na studentach
def add_student(students, student):
    students.append(student)
    return students

def remove_student(students, student_id):
    return [s for s in students if s['id'] != student_id]

# Operacje na obecności
def mark_attendance(students, student_id, present=True):
    for student in students:
        if student['id'] == student_id:
            student['attendance'] = present
    return students