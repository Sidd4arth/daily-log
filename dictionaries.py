dict={}

#creating a dictionary
#- in built
dict1=dict()
#using empty constructor
dict2={}
#creating a dictionary with some key value pair
dict3={'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dict3)
#accessing values using keys
name=dict3['name']
print(name)
age=dict3['age']
print(age)
#adding new key value pair
dict3['country']='USA'
print(dict3)
#updating value of existing key
dict3['age']=31
print(dict3)
#removing key value pair using pop
dict3.pop('city')
print(dict3)
#removing key value pair using del
del dict3['country']
print(dict3)
#checking if key exists
is_name_in_dict3='name' in dict3
print(is_name_in_dict3)
is_city_in_dict3='city' in dict3
print(is_city_in_dict3)
#dictionary methods
print(dict3.keys()) # dict_keys(['name', 'age'])
print(dict3.values()) # dict_values(['Alice', 31])
print(dict3.items()) # dict_items([('name', 'Alice'), ('age', 31)])
