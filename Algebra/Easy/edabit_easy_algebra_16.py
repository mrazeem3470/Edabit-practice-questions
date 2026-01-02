def is_good_match(lst):
    if len(lst) % 2 != 0:
        return "bad match"
    
    result = []
    for i in range(0, len(lst), 2):
        result.append([i] + [i+1])

    return result

answer = is_good_match([2,3,4,5])
print(answer)
