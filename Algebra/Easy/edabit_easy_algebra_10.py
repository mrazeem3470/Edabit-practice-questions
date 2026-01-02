def marathon(*args):
    if not args:
        return False
    total_distance = 0
    for i in args:
        total_distance += abs(i)

    if total_distance == 25:
        return True
    else:
        return False
    
result = marathon(1,6,7,11)
print(result)