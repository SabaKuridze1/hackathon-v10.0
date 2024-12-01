def calculator(num1, operator, num2):
   if operator == '+':
        return num1 + num2

   elif operator == '*':
        return num1 * num2

   elif operator == '-':
         return num1 - num2
    
   elif operator =='/':
        return num1 / num2
    

result = calculator(1 + 2)
print(result)