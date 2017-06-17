import numpy

dictionary = ["hello", "bye", "joey"]
letters = ''
word = numpy.random.choice(dictionary)
wrong = 0
length = len(word)
answer = "     "
print word

for i in range(0, len(word)):
    letters = letters + " _ "
print letters

letter = raw_input("Type in letter below")
if type(letter) == str and len(letter) == 1:
    for i in range(0, len(word)):
        if letter == word[i]:
            print " " * (i *3 +` 1) + letter
            print " _ " * (i + 1)            print i

elif type(letter) == int:
    print"Please only provide letters, not numbers. Try again"
elif len(letter) > 1:
    print "Please only type one letter at a time. Try again"
elif len(letter) == 0:
    print "Please type a letter and try again"






