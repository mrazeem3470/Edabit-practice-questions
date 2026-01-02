def add_total(a,b,c):
    final_value = a*(2**b)
    if final_value % c == 0:
        return True
    else:
        return False
    
result = add_total(5,2,1)
print(result)