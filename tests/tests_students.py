# Test zapisywania do pliku
def test_save_to_file(tmp_path):
    # TODO: Przetestować zapis do pliku w lokalizacji tylko do odczytu
    data = [{"id": 1, "name": "Alice"}]
    filename = tmp_path / "test.json"
    save_to_file(data, filename)
    assert filename.exists()

# Test wczytywania z pliku
def test_load_from_file(tmp_path):
    # TODO: Przetestować odczyt z uszkodzonego pliku JSON
    data = [{"id": 1, "name": "Alice"}]
    filename = tmp_path / "test.json"
    save_to_file(data, filename)
    loaded_data = load_from_file(filename)
    assert loaded_data == data

# Test dodawania studenta
def test_add_student():
    # TODO: Sprawdzić, co się dzieje, gdy dodajemy studenta z duplikatem ID
    students = []
    new_student = {"id": 1, "name": "Alice"}
    updated_students = add_student(students, new_student)
    assert len(updated_students) == 1
    assert updated_students[0] == new_student

# Test usuwania studenta
def test_remove_student():
    # TODO: Dodać przypadek testowy dla usunięcia nieistniejącego ID
    students = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    updated_students = remove_student(students, 1)
    assert len(updated_students) == 1
    assert updated_students[0]["id"] == 2

# Test oznaczania obecności
def test_mark_attendance():
    # TODO: Dodać test dla oznaczenia obecności na studencie spoza listy
    students = [{"id": 1, "name": "Alice", "attendance": False}]
    updated_students = mark_attendance(students, 1, True)
    assert updated_students[0]["attendance"] is True
