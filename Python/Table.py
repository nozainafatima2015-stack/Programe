num = int(input("Eneter a number: "))
print("Table of ", num)
for i in range(1,11):   
    mul = num*i
    print(num,"* %d = %d"%(i,mul))