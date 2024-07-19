my_dict = {'Sergei': 1986, 'Olesya': 1995, 'Ilya': 2013}
print(my_dict)
print(my_dict['Sergei'])
print(my_dict.get('Galina'))
my_dict.update({'Anna': 1980,
                'Mike': 2001})
a = my_dict.pop('Olesya')
print(a)
print(my_dict)

my_set = {1,2,3,1,2,7,3.14,'S',1,7,'S',(9,8,7),3.14}
print(my_set)
my_set.add('D')
my_set.add(50)
my_set.discard(1)
print(my_set)