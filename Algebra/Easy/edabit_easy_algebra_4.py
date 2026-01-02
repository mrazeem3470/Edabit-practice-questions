def num_layers(n):
    thickness = 0.5
    for i in range(n):
        thickness = thickness * 2
    thickness = thickness / 1000
    return str(thickness) + "m"

result = num_layers(5)
print(result)


        