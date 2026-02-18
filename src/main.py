import random

class Maumau():
    def __init__(self, numOfPlayers, name, cards, hands, playerList, deck):
        self.cards = cards
        self.hands = hands
        self.numOfPlayers = numOfPlayers
        self.name = name
        self.playerList = playerList
        self.deck = deck

        setNumOfPlayers() # initialize this method to use this number for other methods.
        inputName(numOfPlayers) # initialize this method to use  names for other methods.
        createCards() # initialize this method to use cards for other methods.
        dealCard(deck, playerList, numOfPlayers)

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
    playerList = []
    for i in range(numOfPlayers):
        name = input("player" + str(i + 1)  + ": ")
        playerList.append(name)
    return playerList


# create cards and deal it to each player.
def createCards():
    # 1. create cards for maumau.
    num = ["7", "8", "9", "10", "J", "Q", "K", "A"] 
    sym = ["heart", "diamond", "club", "spade"]
    # 2. create deck and shuffle it.
    deck = [] # first leer.
    for i in range(len(num)):
        for j in range(len(sym)):
            deck.append(num[i] + " : " + sym[j])
    random.shuffle(deck)
    # to check cards and deck
    print("deck has " + str(len(deck)) + " cards.")
    print(deck)
    # deal cards to each player. playerlist is used as players hand.
    return deck
"""
def dealCard(deck, playerList, numOfPlayers):
    # deal cards if already a rondom card is on the playground.
    if len(deck) == 31:
        for i in range(numOfPlayers):
            playerList[i] 
    pass
"""



def main():
    print("")
    print("welcome to maumau")
    numOfPlayers = setNumOfPlayers()
    playerList = inputName(numOfPlayers)
    print(playerList)
    createCards()
    #dealCard(deck, playerList, numOfPlayers)

if __name__ == "__main__":    
    main()