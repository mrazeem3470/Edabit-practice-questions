mobiles = {
  "phone1": {"brand": "Samsung", "price": 30000},
  "phone2": {"brand": "Apple", "price": 80000}
}
for x,obj in mobiles.items():
  print(x)
  for y in obj:
    print(y + ":", obj[y])