class Maumau():
    def __init__(self):
        pass

# input number of players
def setNumOfPlayers():
    numOfPlayers = int(input("input number of players(2-4):"))
    if numOfPlayers <= 4:
        print("player number is " + str())
        return numOfPlayers
    else:
        print("error: number of players must be between 2 and 4")   
        return setNumOfPlayers()


def main():
    setNumOfPlayers()

if __name__ == "__main__":    
    main()