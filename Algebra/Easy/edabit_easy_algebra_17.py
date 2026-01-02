def adjacent_product(lst):
    max_product = lst[0] * lst[1]

    for i in range(1, len(lst)-1):
        product = lst[i] * lst[i + 1]
        if product > max_product:
            max_product = product

    return max_product
result = adjacent_product([3,6,-2,-5,7,3])
print(result)