#Write a function that accepts *args and prints only the even numbers.
def is_even(*args):
    L = []
    for i in args:
        if i % 2 == 0:
            L.append(i)
    return L

print(is_even(12,34,56,79,97,32,123,479))