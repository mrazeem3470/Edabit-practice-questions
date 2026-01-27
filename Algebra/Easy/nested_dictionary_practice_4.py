laptops = {
  "l1": {"brand": "Dell", "price": 55000, "ram": "8GB"},
  "l2": {"brand": "HP", "price": 60000, "ram": "16GB"}
}
for x,obj in laptops.items():
  print(x)
  print("brand", obj["brand"])
  print("price", obj["price"])