#Create a function count_args(*args) that prints how many arguments were passed.

def count_args(*args):
    print("Number of arguments passed:", len(args))


count_args(1, 2, 3, 4, 5)
count_args("apple", "banana")
count_args()
