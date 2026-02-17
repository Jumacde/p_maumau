import random

class Maumau():
    def __init__(self, numOfPlayers, name, cards, hands):
        self.cards = cards
        self.hands = hands
        self.numOfPlayers = numOfPlayers
        self.name = name

        setNumOfPlayers()
        inputName(numOfPlayers)

# input number of players
def setNumOfPlayers():
    numOfPlayers = int(input("input number of players(2-4):"))
    if 2 <= numOfPlayers <= 4:
        print("player number is " + str(numOfPlayers))
        return numOfPlayers
    else:
        print("error: number of players must be between 2 and 4")   
        return setNumOfPlayers()

# input number of players.
def inputName(numOfPlayers):
    nameList = []
    for i in range(numOfPlayers):
        name = input("player" + str(i + 1)  + ": ")
        nameList.append(name)
    return nameList

def createHands(numOfPlayers, nameList):
    hand = []
    for i in range(numOfPlayers):
        if numOfPlayers == 2:
            

# create cards and deal it to each player.
def createCards(numOfPlayers, nameList):
    # 1. create cards.
    card = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] 
    # 2. create deck.
    deck = card * 4
    # 3. shuffle deck.
    random.shuffle(deck)
    # to check cards and deck
    #print("deck has " + str(len(deck)) + " cards.")
    #print(deck)
    return deck


def main():
    print("")
    print("welcome to maumau")
    numOfPlayers = setNumOfPlayers()
    nameList = inputName(numOfPlayers)
    print(nameList)
    dealCards(numOfPlayers, nameList)

if __name__ == "__main__":    
    main()