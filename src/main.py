class Maumau():
    def __init__(self, numOfPlayers, name):
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

# input number of players
def inputName(numOfPlayers):
    nameList = []
    for i in range(numOfPlayers):
        name = input("player" + str(i + 1)  + ": ")
        nameList.append(name)
    return nameList

def main():
    print("")
    print("welcome to maumau")
    numOfPlayers = setNumOfPlayers()
    nameList = inputName(numOfPlayers)
    print(nameList)

if __name__ == "__main__":    
    main()