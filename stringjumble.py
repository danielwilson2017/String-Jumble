"""
stringjumble.py
Author: Daniel Wilson
Credit: 

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
print("You entered '" + string + "'. Now jumble it:") 
l = list(string)
sost = string.split(' ')

for y in range(1, b+1) :
    print(string[-y],end="")
print()

word = list(reversed(sost))
for word in l :
    print(word[::-1], end="")
print("")

for words in sost:
    g=0
    while g < len(words) :
        r = (str(words[len(words)-g-1]))
        print("{0 : <3} ".format(r), end="")
        g=g+1
print("")


for words in string:
    g=0
    while g < len(words) :
        r = (str(words[len(words)-g-1]))
        print("{0 : <3} ".format(r), end="")
        g=g+1



"""
z=0
while z<len(l) :
    s=[" "]
    a=""
    a=a+l[z]
    if l[z]==" " :
        s.insert(-1,a)
    z=z+1
s.remove(" ")
print(s)
"""
