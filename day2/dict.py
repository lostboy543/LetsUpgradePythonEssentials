dict1 = {1: 'apple', 2: 'ball',3:'cat',4:'dog',5:'elephant'}
print(dict1)
my_dict = {'fname': 'John','lname':'doe', 'age': 26}
print(my_dict['fname'])
print(my_dict.get('lname'))
print(my_dict.get('age'))
my_dict['address'] = 'Mumbai'
print(my_dict)
my_dict['age'] = 33
print(my_dict)
print(dict1.keys())
print(dict1.values())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.pop('fname'))
print(my_dict)
print(dict1.popitem())