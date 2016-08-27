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
print("Len test: ")
print(len(inputTest))

from imported import *
foo(2, 2)
