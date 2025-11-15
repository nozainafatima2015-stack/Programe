num = int(input("Eneter a number:"))
Flag = False
if num > 1:     
    # check for factors
    for i in range (2,num):
        if (num % i) == 0:
            Flag = True
            break
if Flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")