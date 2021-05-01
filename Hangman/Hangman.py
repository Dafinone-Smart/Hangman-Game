import random as r

wordList = ["accept", "abhorrent", "adverse", "aggravate", "ambiguous", "amicable", "amuse", "breach", "brooch", "callous", "compose",
            "connote", "denote", "correlation", "discreet", "envelop", "exercise", "phase", "gambit", "grisly", "hero", "elon", "musk"]
shapeList = []
pickWord = r.choice(wordList)
newWordList = []
Player = 1
chances = 0


def requestWord():
    for word in pickWord:
        newWordList.append(word)


# def requestWord():
#     global Player
#     pickWord = input(f"Player {Player}: Please pick a word\n")

#     Player += 1

#     for word in pickWord:
#         wordList.append(word)


def stageForWord(neededWord="", counterCounter=0):
    shape = "_"
    for length in range(len(newWordList)):
        if length == len(newWordList) - 1:
            if neededWord == "":
                shapeList.append(shape)
                print(shape, end="")
            else:
                if length == counterCounter:
                    shapeList[counterCounter] = neededWord
        else:
            if neededWord == "":
                shapeList.append(shape)
                print(shape, "", end="")
            else:
                if length == counterCounter:
                    shapeList[counterCounter] = neededWord


def printStage(failed=6):
    print(chr(27) + "[2J")

    print("   "+"_"*4)
    for h in range(7):
        if h > 0:
            print("  |")
        else:
            print("  |    |")
            if failed == 0:
                print("  |    0")
            elif failed == 1:
                print("  |    0")
                print("  |    |")
            elif failed == 2:
                print("  |    0")
                print("  |    |")
                print("  |    |")
            elif failed == 3:
                print("  |    0")
                print("  |    |")
                print("  |    |")
                print("  |    /")
            elif failed == 4:
                print("  |    0")
                print("  |    |")
                print("  |    |")
                print("  |    /|")
            elif failed == 5:
                print("  |    0")
                print("  |   /|")
                print("  |    |")
                print("  |    /|")

    print("_"*8)

    print("\n")
    print("\n")
    print("\n")
    print("\n")

    if failed == 6:
        stageForWord()


def mainFunction():
    global chances
    while(True):
        print("\n")

        guessWord = input("Guess a letter of the word: \n")

        print(chr(27) + "[2J")

        if guessWord not in newWordList:
            counter = 0
            if chances == 5:
                printStage(chances)
                print("\n")
                print("You have failed the challenge!")
                exit()
            else:
                print(f"Wrong Word! This is your {chances+1} chance!!")
                printStage(chances)
                chances += 1
                counter += 1
                continue

        if guessWord in newWordList:
            counter = 0
            for word in newWordList:
                if word == guessWord:
                    stageForWord(guessWord, counter)
                    for shape in shapeList:
                        print(shape, end=" ")
                    print("\n")
                    if shapeList == newWordList:
                        print("\n")
                        print("You have won the game!")
                        exit()
                    counter += 1
                else:
                    counter += 1
                    print("\n")
                    continue


if __name__ == "__main__":
    requestWord()
    printStage()
    mainFunction()
