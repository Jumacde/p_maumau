
import random

class Maumau():
    def __init__(self, numOfPlayers, name, cards, hands, playerList, playground, hand, winnerLsit):
        self.cards = cards
        self.hands = hands
        self.numOfPlayers = numOfPlayers
        self.name = name
        self.playerList = playerList
        self.playground = playground
        self.hand = hand
        self.winnerList = winnerLsit

        # initialize methods to use the result of this for other methods.
        setNumOfPlayers() 
        inputName(numOfPlayers) 
        createCards() 
        dealCard(cards, playerList, numOfPlayers)
        doPlay(cards, playerList, numOfPlayers, hand, playground)
        determinateWinner(playerList, hand, playground, numOfPlayers, cards)

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
    #print("- rest cards: " + str(cards))
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
    return hand, playground

# method: play game.
def doPlay(cards, playerList, hand, playground):
    # repeat player plays maumau until all player end the playpahse.
    for i in range(len(playerList)):
        currentPlayer = playerList[i] # player who play at this turn
        currentHand = hand[currentPlayer] # current hand of the player who play at this turn.
        topCard = playground[-1] # top card on the playground.

        # check current hand and play.
        for index, card in enumerate(currentHand):
            cardIndex = currentHand[index]
            # [0] is number, [1] is symbol.
            # check whether a card players has same symbol or number with the one of the top card on the playground.
            if cardIndex[0] == topCard[0] or cardIndex[-1] == topCard[-1]:
                # remove the card.
                removedCard = currentHand.pop(index)
                # add the removed card on the playground.
                playground.append(removedCard)
                print("-" + currentPlayer + " set " + removedCard + "on the playground.")
                print("- current playable card: " + playground[-1])            
                break
    return hand, playground

def determinateWinner(playerList, hand, playground, numOfPlayers, cards):
    # to show winner ranking after the game ends.
    winnerList = {}
    
    while len(playerList) > 1:
        # repeat doplay method until one of players win the game.
        hand, playground = doPlay(cards, playerList,  hand, playground)
        for name in playerList:
            if len(hand[name]) == 0:
                rank = len(winnerList) + 1 # to show the winner ranking.
                winnerList[name] = rank
                print("- " + name + " wins!")
                playerList.remove(name) # remove the winner from playerlist to end the game.

    # the last player is added to winnerlist.
    lastplayer = playerList[0]
    winnerList[len(winnerList) + 1] = lastplayer
    print("- " + lastplayer + " is the last player.")
    return winnerList


def main():
    print("")
    print("<< welcome to maumau >>")
    # execute each methods and use the returned values for next methods.
    numOfPlayers = setNumOfPlayers()
    playerList = inputName(numOfPlayers)
    cards = createCards()
    hand, playground = dealCard(cards, playerList, numOfPlayers)
    #print(playerList)
    #doPlay(cards, playerList, numOfPlayers, hand, playground) # to check this method.
    determinateWinner(playerList, hand, playground, numOfPlayers, cards)

if __name__ == "__main__":    
    main()