# Часть 1. Работа со списком:
a = [7, 10, 23, -19, 80]
a.sort()
print(a)
a.append(20)
a.append(21)
a.sort()
print(a[1::2])
print(a.count(20))
print(a.index(20))
a.insert(3, 19)



# Часть 2. Работа с кортежом:
a_2 = (1, 'Kostya', 25)
print(len(a_2))
print(a_2[0])
a_2 *=2



# Часть 3. Работа со словарём:
ad = ['man', 'wife']
family = {
        'name': 'kostya',
        'age': '25',
        'family_member': ['husband ', 'wife'],
        'profession': 'engineer',
}
print(family['name'])
family['profession'] = 'coder'
family['family_member'].append('son')
print(list(family))
family['gender'] = 'male'
value = family.pop('gender')
