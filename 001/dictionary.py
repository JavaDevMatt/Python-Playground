myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud',
    'age' : 1
    }

print('-------------')

print(myCat['size'])
print(myCat['age'])
print('-------------')

for v in myCat.values():
    print(v)
print('-------------')

for k in myCat.keys():
    print(k)
print('-------------')

for i in myCat.items():
    print(i)
print('-------------')
