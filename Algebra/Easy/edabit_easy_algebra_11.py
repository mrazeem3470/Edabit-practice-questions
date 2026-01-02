def two_digit_sum(num):
    first_num = num // 10
    second_num = num % 10
    result = first_num + second_num

    return result

sum = two_digit_sum(24)
print(sum)
