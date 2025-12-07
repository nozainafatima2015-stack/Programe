my_dict = {"name": "Alice", "age": 30}
value = my_dict["name"]   

my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city", "Unknown")   

my_dict = {"name": "Alice", "age": 30}
target_value = 30
found_key = None
for key, value in my_dict.items():
    if value == target_value:
        found_key = key
        break
  
my_list = [1, 2, 3, 4, 5, 3]
index = my_list.index(3)  

my_list = [1, 2, 3, 4, 5, 3]
indices = [i for i, x in enumerate(my_list) if x == 3]  

my_string = "Hello, world!"
index = my_string.find("world")   