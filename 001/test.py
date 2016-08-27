# Comment test

print ("----------------------------")
print ("Strting test script")
print ("----------------------------")
print ("")

text = open("file.txt").read()
print(text)
print ("----------------------------")

print ("Input test:")
inputTest = input()
print("Priting input test: " + inputTest)
print("Len test: " + str(len(inputTest)))
print(len(inputTest))

from imported import *
foo(2, 2)
print(float('3.14'))
print(int('3'))

import random
print(random.randint(1, 100))
