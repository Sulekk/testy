# Zapisywanie do pliku
def save_to_file(data, filename):
    # TODO: Sprawdzić, czy plik istnieje przed zapisaniem
    with open(filename, 'w') as file:
        json.dump(data, file)

# Wczytywanie z pliku
def load_from_file(filename):
    # TODO: Dodać obsługę wyjątków dla błędów odczytu
    with open(filename, 'r') as file:
        return json.load(file)

# Operacje na studentach
def add_student(students, student):
    # TODO: Walidacja danych wejściowych studenta (np. unikalne ID)
    students.append(student)
    return students

def remove_student(students, student_id):
    # TODO: Dodać log, jeśli student o podanym ID nie istnieje
    return [s for s in students if s['id'] != student_id]

# Operacje na obecności
def mark_attendance(students, student_id, present=True):
    # TODO: Obsłużyć przypadek, gdy student o podanym ID nie istnieje
    for student in students:
        if student['id'] == student_id:
            student['attendance'] = present
    return students
