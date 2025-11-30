my__dict = {}
my__dict = {1 : 'apple' , 2: 'balls'}
my__dict = {'name' : 'Nozaina' , 1:[2,4,3]}
my__dict = {'name' : 'Noor' , 'age' : 11}
print(my__dict['name'])
print(my__dict.get('age'))
my__dict['age']= 12
print(my__dict)
my__dict['adress']= 'DownTown'
print(my__dict)
my__dict.pop('age')
print(my__dict)
print("Adress:", my__dict.get('adress'))
my__dict.clear()
print(my__dict)