def Triangular_number(num):
    sum = 0 
    for i in range(1,num + 1):
        sum += i
    return sum
result = Triangular_number(6)
print(result)


def Triangle(formula):
    result = formula * (formula + 1) / 2
    return result
result = Triangle(6)
print(result)