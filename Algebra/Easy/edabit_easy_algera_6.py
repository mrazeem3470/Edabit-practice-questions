def count(*args):
    total = 0
    for i in args:
        if i in [2,3,4,5,6]:
            total += 1
        elif i in [10, "J", "Q", "K", "A"]:
            total -= 1

    return total

result = count(5,9,10,3,"J","A",4,8,5)
print(result)