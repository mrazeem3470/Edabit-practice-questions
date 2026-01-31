#Write a function sum_numbers(*args) that accepts any number of integers and prints their sum.

def sum_numbers(*args):
  sum = 0
  for i in args:
    sum +=i
  return sum
print(sum_numbers(1,2,3,4,5))