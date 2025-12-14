def is_disarium(num):
    """
     
    """
    
    num_str = str(num)
    
     
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    
     
    return total == num

 
number1 = 175
if is_disarium(number1):
    print(f"{number1} is a disarium number. ")
else:
    print(f"{number1} is not a disarium number.  ")

number2 = 89
if is_disarium(number2):
    print(f"{number2} is a disarium number .")
else:
    print(f"{number2}  is not a disarium number.")

number3 = 25
if is_disarium(number3):
    print(f"{number3} is a disarium number. ")
else:
    print(f"{number3} is not a disarium number. ")
