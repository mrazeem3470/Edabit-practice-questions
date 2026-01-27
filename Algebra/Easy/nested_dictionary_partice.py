student = {
    "student1" : {"name" : "Azeem", "hobby" : "cricket"},
    "student2" : {"name" : "Romeo", "hobby" : "Football"}
}
for x,obj in student.items():
  print(x)
  for  y in obj:
    print(y + ":", obj[y])