my_dict = {'Marta':1987,'Mike':2005,'Sara':1983}
print(my_dict)
print(my_dict['Marta'])
print(my_dict.get('Alex', 'There is no date of birth'))
my_dict.update({'Garik':2023,
                'Veronka':1956})
print(my_dict['Marta'])
my_dict.pop('Marta')
print(my_dict)

my_set = {1,6,5,2,6,5,3,7,'apple','apple','banana',1.2,5.6,1.2,True,(1,2,1,2)}
print(my_set)
my_set.add('ananas')
print(my_set)
my_set.remove('banana')
print(my_set)