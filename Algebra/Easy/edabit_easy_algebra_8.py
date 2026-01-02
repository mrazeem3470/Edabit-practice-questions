def is_automorphic(n):
    square =  n*n
    digits = len(str(n))
    if square % (10**digits) == n:
        return True
    else:
        return False


result = is_automorphic(7)
print(result)