def total_distance(height,length,tower):
    steps = tower / height
    distance = height + length
    result = steps * distance
    return result
total_rasta = total_distance(0.2,0.4,100.0)
print(round(total_rasta))