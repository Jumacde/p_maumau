class Maumau():
    def __init__(self):
        self.setNumOfPlayers()
        self.inputName()

def setNumOfPlayers(self):
    self.numOfPlayers = int(input("how many players? 2-4: "))
    numOfPlayers = self.numOfPlayers

    if 2 < numOfPlayers <= 4:
        return numOfPlayers
    else:
        print("invalid number of players")
    return setNumOfPlayers(self)
   

def inputName(self):
    numOfPlayers = self.numOfPlayers
    name = self.playerNames
    name = []

    for i in range(numOfPlayers):
        name.append(input("player" + str(i + 1) + " is: "))
        return name

def main():
    setNumOfPlayers()
    inputName()
    

if __name__ == "main":    
    main()