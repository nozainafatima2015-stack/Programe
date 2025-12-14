my__tuple = ()
print(my__tuple)

my__tuple = (1,2,3)
print(my__tuple)

my__tuple =(1,"Hello",3.4)
print(my__tuple)

my__tuple = ("mouse",[8,4,6],(1,2,3))
print(my__tuple)

my__tuple = ('p','e','r','m','i','t')
print(my__tuple[0])
print(my__tuple[5])

n_tuple = ("mouse",[8,4,6],(1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][1])

print("Sliced :",my__tuple[1:4])
for letter in(my__tuple):
    print("Hello",letter)