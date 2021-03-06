"""
stringjumble.py
Author: Daniel Wilson
Credit: Payton Sterns

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string = str(input("Please enter a string of text (the bigger the better): "))
b = (int(len(string)))
print('You entered "'+ string + '". Now jumble it:') 
l = list(string)
sost = string.split(' ')

print()
for y in range(1, b+1) :
    print(string[-y],end="")
print()
print()

f = list(reversed(sost))
for word in f :
    print(word, end=" ")
print("")
print()

for words in sost:
    g=0
    while g < len(words) :
        r = (str(words[len(words)-g-1]))
        print("{0}".format(r), end="")
        g=g+1
    print(" ", end=" ")
