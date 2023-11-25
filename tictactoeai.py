tictactoe = {
    1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''
}

def game(tictactoe):
    print(tictactoe[1] + ' ! '+tictactoe[2]+' ! '+tictactoe[3] + ' ! ')
    print('--+--+--+--')
    print(tictactoe[4] + ' ! '+tictactoe[5] + ' ! '+tictactoe[6] + ' ! ')
    print('--+--+--+--')
    print(tictactoe[7] + ' ! '+tictactoe[8] + ' ! '+tictactoe[9] + ' ! ')
    print('--+--+--+--')
    print("\n")
    
game(tictactoe)
#checking if the position givem by the user is empty or not
def checkemptyspace(place):
    if tictactoe[place] == '':
        return True
    else:
        return False
#function to check draw condition 
def draw():
    for key in tictactoe.keys():
        if tictactoe[key] == '':
            return False
    return True
#inserting the value to the position if it is free 
def win():
    if (tictactoe[1] == tictactoe[2] == tictactoe[3] != ""):
        return True
    elif (tictactoe[4] == tictactoe[5] == tictactoe[6] != ""):
        return True
    elif (tictactoe[7] == tictactoe[8] == tictactoe[9]  != ""):
        return True
    elif (tictactoe[1] == tictactoe[4] == tictactoe[7]  != ""):
        return True
    elif (tictactoe[2] == tictactoe[5] == tictactoe[8]  != ""):
        return True
    elif (tictactoe[3] == tictactoe[6] == tictactoe[9]  != ""):
        return True
    elif (tictactoe[1] == tictactoe[5] == tictactoe[9]  != ""):
        return True
    elif (tictactoe[7] == tictactoe[5] == tictactoe[3]  != ""):
        return True
    else:
        return False
#function to check the condition for wining the game
def winscore(mark):
    if (tictactoe[1] == tictactoe[2] == tictactoe[3] != mark):
        return True
    elif (tictactoe[4] == tictactoe[5] == tictactoe[6]  != mark):
        return True
    elif (tictactoe[7] == tictactoe[8] == tictactoe[9] != mark ):
        return True
    elif (tictactoe[1] == tictactoe[4] == tictactoe[7] != mark ):
        return True
    elif (tictactoe[2] == tictactoe[5] == tictactoe[8]  != mark ):
        return True
    elif (tictactoe[3] == tictactoe[6] == tictactoe[9]  != mark ):
        return True
    elif (tictactoe[1] == tictactoe[5] == tictactoe[9] != mark ):
        return True
    elif (tictactoe[7] == tictactoe[5] == tictactoe[3]  != mark ):
        return True
    else:
        return False
#function to insert the value in the position
def insertvalue(value,place):
    if checkemptyspace(place):
        tictactoe[place] = value
        game(tictactoe)
        #to check whether it is draw
        if draw():
            print("The game is draw!")
            exit()
        #to check whether it wins
        if win():
            if value == 'X':
                print("AI wins")
                exit()
            else:
                print("You win!")
                exit()
        return
    else:
        print("Unable to insert the value in the game")
        place=int(input("Enter the place where the value needs to be inserted"))
        insertvalue(value,place)
        return
   



player1='O'
bot='X'

def player():
    place = int(input("Enter the place for player 'O':"))
    insertvalue(player1,place)
    return
# for computer to have as 'X'
def computer():
    score = -1000
    move = 0
    #to check for the possible outcomes
    for key in tictactoe.keys():
        if tictactoe[key] == '':
            tictactoe[key] = bot
            score1 = minimax(tictactoe,0,False)
            tictactoe[key] = ''
            #implementing minimax algorithm
            if score1 > score:
                score = score1
                move = key
    insertvalue(bot,move)
    return
#function minimax
def minimax(tictactoe,depth,max):
    if winscore(bot):
        return 1
    elif winscore(player1):
        return -1
    elif draw():
        return 0
    if max:
        score = -800
        for key in tictactoe.keys():
            if tictactoe[key] == '':
                tictactoe[key] = bot
                score1 = minimax(tictactoe,0,False)
                tictactoe[key] = ''
                if score1 > score:
                    score=score1
        return score
    else:
        score=800
        for key in tictactoe.keys():
            if tictactoe[key] == '':
                tictactoe[key] = player1
                score1 = minimax(tictactoe,0,True)
                tictactoe[key] = ''
                if score1 < score:
                    score=score1
        return score
while True:
    player() 
    if win():
        print("You wins")
        break
    if draw():
        print("The game is draw!")
        break
    computer()
    if win():
        print("AI wins")
        break
    if draw():
        print("The game becomes draw")
        break
