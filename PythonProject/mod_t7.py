my_dict = {'maxy': 2008, 'leha': 2003, 'sveta': 1996}
print(my_dict)
my_dict['denis'] = 2004
print(my_dict['sveta'], my_dict.get('dfgh'))
print(my_dict)
my_dict.update({"dad": 1961, 'mom': 1963})
print(my_dict)
print(my_dict.pop('sveta'))
print(my_dict)
#Множества
print(' ')
my_set = {2,5,4,5,3,8,8,True,True, 'knight'}
print(my_set)
my_set.add(7)
my_set.add(9)
my_set.discard(1)
print(my_set)