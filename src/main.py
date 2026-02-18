import random

class Maumau():
    def __init__(self, numOfPlayers, name, cards, hands, playerList, playground):
        self.cards = cards
        self.hands = hands
        self.numOfPlayers = numOfPlayers
        self.name = name
        self.playerList = playerList
        self.playground = playground

        setNumOfPlayers() # initialize this method to use this number for other methods.
        inputName(numOfPlayers) # initialize this method to use  names for other methods.
        createCards() # initialize this method to use cards for other methods.
        dealCard(cards, playerList, numOfPlayers)

# input number of players
# if you input wrong number and error occurs, this method will be called again until you input right number.
def setNumOfPlayers():
    try:
        numOfPlayers = int(input("input number of players(2-4):"))
        if 2 <= numOfPlayers <= 4:
            print("player number is " + str(numOfPlayers))
            return numOfPlayers
        else:
            print("error: number of players must be between 2 and 4")   
            return setNumOfPlayers()
    except ValueError:
        print("error: input must be an integer")   
        return setNumOfPlayers()

# input number of players.
def inputName(numOfPlayers):
    playerList = []
    for i in range(numOfPlayers):
        name = input("player" + str(i + 1)  + ": ")
        playerList.append(name)
    return playerList


# create cards and deal it to eac2h player.
def createCards():
    # 1. create cards for maumau.
    num = ["7", "8", "9", "10", "J", "Q", "K", "A"] 
    sym = ["♥", "♦", "♣", "♠"]
    # 2. create deck and shuffle it.
    cards = [] # first leer.
    for i in range(len(num)):
        for j in range(len(sym)):
            cards.append(num[i] + " : " + sym[j])
    random.shuffle(cards)
    # to check cards and deck
    print("- deck has " + str(len(cards)) + " cards.")
    print("-" + str(cards))
    # deal cards to each player. playerlist is used as players hand.
    return cards

""" 
 deal card method:
  1. a top card is set on the playground
  2. 5 cards is dealt to each player.
"""
def dealCard(cards, playerList, numOfPlayers):
    playground = []
    # check index 0 one all cards
    print("- card index 0: " + cards[0])

    fistCard = cards.pop(0) 
    playground.append(fistCard) # the removed card is set on the playground.
    # check playgrround
    print("- playground: " + playground[0])
    print("- rest cards: " + str(cards))
    print( "- " + str(len(cards)) + "cards are there.")

    # deal 5 cards to each player.
    hand = {} # dict to connect playername and dealt cards on each player(hand).
    for name in playerList:
            hand[name] = [] # leer space to set dielt cards.
            for j in range(5): # set number of cards to deal. = 5 cards dieal.
                hand[name].append(cards.pop(0)) #  the removed card is set on each player.
            print("- " + name + "'s hand: " + str(hand[name]))
            print("- " + name + "'s hand length: " + str(len(hand[name])))
            # check rest cards after dealing.
    
    print("- rest cards: " + str(cards))
    print("- " + str(len(cards)) + "cards are there.")    
    return playground, hand


def main():
    print("")
    print("<< welcome to maumau >>")
    numOfPlayers = setNumOfPlayers()
    playerList = inputName(numOfPlayers)
    cards = createCards()

    #print(playerList)
    dealCard(cards, playerList, numOfPlayers)

if __name__ == "__main__":    
    main()