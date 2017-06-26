from __future__ import print_function
import numpy


wrong = 0
yay = 0
def dying(wrong):
    if wrong == 0:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("  __________     ")
        print("|        |     ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif wrong == 1:
        print("  __________     ")
        print("|        |     ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif wrong == 2:
        print(" ___________    ")
        print("|         |    ")
        print("|         O    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif wrong == 3:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|         |  ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif wrong == 4:
        print(" _________       ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif wrong == 5:

        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\  ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif wrong == 6:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\  ")
        print("|        /   ")
        print("|              ")
        print("|              ")
    elif wrong == 7:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\  ")
        print("|        / \  ")
        print("|              ")
        print("|              ")
    else:
        print("error")
easy_list = []
hard_list = ["gladiolus", "cerise", "abrogate", "knack", "luxuriance", "fracas", "foulard", "invulnerable", "torsion",
              "brethren", "intelligible", "eczema", "promiscuous", "sanitarium", "canonical", "therapy", "initials",
              "sacrilegious", "semaphore", "chlorophyll", "psychiatry", "dulcimer", "meticulosity", "insouciant"]
correct_letters = []

word = numpy.random.choice(hard_list)
length = len(word)
output = " "
lengthofword = "_ " * length

print(lengthofword)
print(word)
while yay == 0:
    dying(wrong)
    output = ' '
    letter = raw_input("What letter would you like to guess?")

    for i in word:
        if letter == i:
            correct_letters.append(letter)
        if i in correct_letters:
            output = output + i
        else:
            output = output + "_ "
    if letter not in correct_letters:
        wrong += 1
    if len(correct_letters) == length:
            yay = 1
            print(yay)
    if yay == 1:
        print("Congratulations!!")
        print("You have won absolutely nothing!")
        print("Do you want to play again?")
        print("The word was:")
    if wrong == 7:
        print("Sorry, the word was" + word)
        print("Try again.")
        break

    print(output)


