def calculator(num1, operator, num2):
    if operator == "/":
        if num2 == 0:
            return "can't divide by 0!"
        else:
            return num1 / num2
    
    elif operator == "+":
        return num1 + num2
    
    elif operator == "-":
        return num1 - num2
    
    elif operator == "*":
        return num1 * num2
    
result = calculator(3,"+",0)
print(result)
    



