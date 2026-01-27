school = {
  "class1": {
    "student1": {"name": "Ayan", "Math": 85, "grade": "A"},
    "student2": {"name": "Zoya", "Math": 78, "grade": "B"}
  }
}
for class_name, students in school.items():
  for student_name, details in students.items():
    print(student_name)
    for detail in details:
      print(detail + ":", details[detail])