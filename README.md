# p_maumau
try cording mau-mau by python
<<game-flow>>:
1. set number of players maumau (2-4).
2. give name each player.
3. a top-card of deck is set on the playground.
4. deal 5 cards to each player.
5. beginn game. player1 who has index0 on playerlist(you) plays 1st turn.

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