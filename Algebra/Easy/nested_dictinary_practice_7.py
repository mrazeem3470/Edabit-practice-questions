data = {
  "A": {"Math": 80, "Sci": 70, "Eng": 90},
  "B": {"Math": 60, "Sci": 75, "Eng": 85}
}
for x,obj in data.items():
  print(x)

  print("Avgerage Marks" + ":",(obj["Math"] + obj["Sci"] + obj["Eng"])/3)