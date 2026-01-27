marks = {
  "Aman": {"Math": 80, "Science": 70},
  "Riya": {"Math": 90, "Science": 85}
}
for student_name, subjects in marks.items():
  print(student_name)
  total_marks = subjects["Math"] + subjects["Science"]
  print("Total Marks:", total_marks)