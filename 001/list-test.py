supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print('binders' in supplies)
print('binders' not in supplies)
print(supplies.index('binders'))

letters = ['1', '2', '3', '1', '1', '1', '1']
print(letters)
letters.remove('1')
print(letters)

while '1' in letters:
    letters.remove('1')

print(letters)
