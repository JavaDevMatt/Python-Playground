#--------------------
#if test
b = 'web'
if b == True:
    print('True')
else:
    print('False')


#--------------------
#while test
i = 1

while i < 10:
    print(i)
    i += 1
    if(i == 6):
        break

print('Outside of while')


#--------------------
#for ragne test
print()
print('range test: ')
for i in range(10):
    print(i)

print('range test2: ')
for i in range(5, 10):
    print(i)

