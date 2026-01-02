def sum_num(lst):
    result = 0
    for i in lst:
        if isinstance(i, (int,float)) and not isinstance(i,bool):
            result += i
    return result
        
sum = sum_num([1,2,"13","4","645"],)
print(sum)




