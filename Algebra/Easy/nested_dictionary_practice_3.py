cars = {
  "car1": {"brand": "BMW", "year": 2020},
  "car2": {"brand": "Audi", "year": 2022}
}
for x,obj in cars.items():
  print(x)
  for y in obj:
    print(y + ":", obj[y])