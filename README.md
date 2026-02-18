# p_maumau
try cording mau-mau by python
<<win-rule>>
each player set a card which has same number or symbol like the top card on the playground.
who has no card on their hand is the winner. 

<<game-flow>>:
1. set number of players maumau (2-4).
2. give name each player.
3. a top-card of deck is set on the playground.
4. deal 5 cards to each player.
5. beginn game. player1 who has index0 on playerlist(you) plays 1st turn. 
 5.1. the player1 set a card which has same symbol or number like the card from phase 3 on the desk.
 5.2. if you has no card to set on the desk draw a card from the deck.
 5.3. repat this phase 5 each player until a player has no card on thier hand.

----------------
<<about methods>>
1. method: setNumOfPlayers():
you can input a number between 2 and 4.
if you int other number show a error message and you must input number of player again.
2. method: inputName():
you must input name each player.
3. method: createCards():
create card than a list(cards-List). 
 3.1. each number and symbol is created than a list(num- and sym-List).
 3.2. the both-list is mixed and its inserted in a list(cards).
 3.3. shuffle the cards-list
4.  dealCards():
 a top of card is set on the playground and 5 cards are dealt to each player.
 
 - playgound(desk), deck, card, hand are created as list or dictionaly.
    set a card on the playground == remove a card from hand and add it on the playground-list.
    draw a card == the top card is removed from the deck and it added on the hand.

 - a leer dictionaly is used here to connect dealt card and player.
    1. create a leer dictionaly
    hand = {} 
    2. connect each player and diealt cards and do deal.
    for name in playerList:
            - connect player by name and the dictionaly.
            hand[name] = [] 
            - deal 5 cards once to each player. == add 5 cards in each players list in the dictionaly.
            for j in range(5): # deal cards 5 times.
                hand[name].append(cards.pop(0)) # the top cards is removed from the deck and it is added on each players hand.
 -
