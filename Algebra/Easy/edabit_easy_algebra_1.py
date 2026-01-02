def color_invert(*rgb):
    List = []
    for i in rgb:
        invert = 255 - i
        List.append(invert)
    return List

result = color_invert(34,56,78)
print(result)
