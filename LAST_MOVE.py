def Choosing_Symbol():
    player1=input("Enter a capital letter to represent player1(expect 'O'):")
    player1=player1.upper()
    while not player1.isalpha() or player1=="O" or len(player1)>1:
        print("Invalid Input.")
        player1=input("Enter a capital letter (expect 'O'):")
        player1=player1.upper()

    player2=input("Enter a capital letter to represent player1(expect 'O'and "+player1+"):")
    player2=player2.upper()
    while not player1.isalpha() or player2=="O" or player2==player1 or len(player2)>1:
        print("Invalid Input.")
        player2=input("Enter a capital letter (expect 'O'):")
        player2=player2.upper()
    return player1,player2

def take_number():
    Num=input("Enter the row/column number of the playing field(3,5,7):")
    while not Num in ["3","5","7"]:
        print("Invalid entry.Please enter a digit.")
        Num=input("Enter the row/column number of the playing field(3,5,7):") 
    return int(Num)
    
def Create_board(Num):
    board=[[' ' for _ in range(Num)] for _ in range(Num)]
    return board

def Choosing_direct(player):
    direct=input(f"\nPlayer {player} please enter the direction you want to move your big stone(N,S,E,W,NE,NW,SE,SW):")
    while not direct in ["N","S","E","W","NE","NW","SE","SW"]:
        print("Invalid Input!")
        direct=input(f"Player {player} please enter the direction you want to move your big stone(N,S,E,W,NE,NW,SE,SW):")
    return direct

def print_board(board,Num):
    columns=["A","B","C","D","E","F","G"]
    for x in range(Num):
        print(f"     {columns[x]}",end="")
    print("\n   ",'------'*Num)
    for y in range(Num):
        print(y+1,end="")
        for i in range(Num):
            print(f"   |{board[y][i]}|",end="")
        print("  ",y+1)
        print("   ","------"*Num)
    for j in range(Num):
        print(f"     {columns[j]}",end="")

def find_index(board,symbol,Num):
    for x in range(Num):
        for y in range(Num):
            if board[x][y]==symbol:
                return x,y

def Move_symbol(board,player,Num):
    cont=True
    directions={"W":-1,"S":1,"E":1,"N":-1,"NW":1,"NE":1,"SW":1,"SE":1}
    index_row,index_column=find_index(board,player,Num)
    while cont==True:
        direct=Choosing_direct(player)
        next_move=directions[direct]
        if direct in "EWNS":
            if direct in "NS":
                try:
                    if not check(board,index_row+next_move,index_column):
                        print("You can not move your stone.")
                    else:
                        if index_row+next_move>=0:
                            board[index_row+next_move][index_column]=player
                            board[index_row][index_column]=" "
                            cont=False
                except IndexError:
                    print(f"You can not move to direction {direct}!")
            else:
                try:
                    if not check(board,index_row,index_column+next_move):
                        print("You can not move your stone.")
                    else:
                        if index_column+next_move>0:
                            board[index_row][index_column+next_move]=player
                            board[index_row][index_column]=" "
                            cont=False
                except IndexError:
                    print(f"You can not move to direction {direct}!")

        elif direct=='SE':
            try:
                if not check(board,index_row+next_move,index_column+next_move):
                    print("You can not move your stone.")
                else:
                    if index_row+next_move>=0 and index_column+next_move>=0:
                        board[index_row+next_move][index_column+next_move]=player
                        board[index_row][index_column]=" "
                        cont=False
            except IndexError:
                print(f"You can not move to direction {direct}!")
        
        elif direct=='SW':
            try:
                if not check(board,index_row+next_move,index_column-next_move):
                    print("You can not move your stone.")
                else:
                    if index_row+next_move>=0 and index_column-next_move>=0:
                        board[index_row+next_move][index_column-next_move]=player
                        board[index_row][index_column]=" "
                        cont=False
            except IndexError:
                print(f"You can not move to directon {direct}!")
        
        elif direct=='NW':
            try:
                if not check(board,index_row-next_move,index_column-next_move):
                    print("You can not move your stone.")
                else:
                    if index_row-next_move>=0 and index_column-next_move>=0:
                        board[index_row-next_move][index_column-next_move]=player
                        board[index_row][index_column]=" "
                        cont=False
            except IndexError:
                print(f"You can not move to directon {direct}!")
        
        else:
            try:
                if not check(board,index_row-next_move,index_column+next_move):
                    print("You can not move your stone.")
                else:
                    if index_row-next_move>=0 and index_column+next_move>=0:
                        board[index_row-next_move][index_column+next_move]=player
                        board[index_row][index_column]=" "
                        cont=False
            except IndexError:
                print(f"You can not move to directon{direct}")
    print_board(board,Num)

def set_stone(board,player,Num):
    try:
        columns={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
        location=input(f"\nplayer {player},please enter the location where you want to place a small stone (like 1A):")
        while not location[1] in columns or not int(location[0]) in [x for x in range(1,Num+1)] or len(location)>2:
            print("Invalid Input.")
            location=input(f"player {player},please enter the location where you want to place a small stone (like 1A):")
        while not check(board,int(location[0])-1,columns[location[1]]):
            location=input(f"player {player},please enter the location where you want to place a small stone (like 1A):")
        board[int(location[0])-1][columns[location[1]]]="O"
        print_board(board,Num)
    except ValueError:
        print("Invalid entry.")
        set_stone(board,player,Num)
    except IndexError:
        print("Invalid entry.")
        set_stone(board,player,Num)

def is_finished(board,player,Num):
    row_index,column_index=find_index(board,player,Num)
    if column_index==0 and row_index==0:
        if board[row_index+1][column_index]!=" " and board[row_index+1][column_index+1]!=" " and board[row_index][column_index+1]!=" ":
            return True
        else:
            return False
        
    elif row_index==Num-1 and column_index==0:
        if board[row_index][column_index+1]!=" " and board[row_index-1][column_index+1]!=" " and board[row_index-1][column_index]!=0:
            return True
        else:
            return False
    
    elif row_index==Num-1 and column_index==Num-1:
        if board[row_index-1][column_index]!=" " and board[row_index-1][column_index-1]!=" " and board[row_index][column_index-1]!=" ":
            return True
        else:
            return False
    
    elif row_index==0 and column_index==Num-1:
        if board[row_index][column_index-1]!=" " and board[row_index+1][column_index]!=" " and board[row_index+1][column_index-1]!=" ":
            return True
        else:
            return False
    
    elif row_index==0:
        if board[row_index][column_index-1]!=" " and board[row_index+1][column_index-1]!=" " and board[row_index+1][column_index]!=" " and board[row_index+1][column_index+1]!=" " and board[row_index][column_index+1]!=" ":
            return True
        else:
            return False
    
    elif column_index==0:
        if board[row_index-1][column_index]!=" " and board[row_index-1][column_index+1]!=" " and board[row_index][column_index+1]!=" " and board[row_index+1][column_index+1]!=" " and board[row_index+1][column_index]!=" ":
            return True
        else:
            return False
    
    elif row_index==Num-1:
        if board[row_index][column_index-1]!=" " and board[row_index-1][column_index-1]!=" " and board[row_index-1][column_index]!=" " and board[row_index-1][column_index+1]!=" " and board[row_index][column_index+1]!=" ":
            return True
        else:
            return False

    elif column_index==Num-1:
        if board[row_index+1][column_index]!=" " and board[row_index+1][column_index-1]!=" " and board[row_index][column_index-1]!=" " and board[row_index-1][column_index-1]!=" " and board[row_index-1][column_index]!=" ":
            return True
        else:
            return False
    
    else:
        if board[row_index-1][column_index]!=" " and board[row_index-1][column_index-1]!=" " and board[row_index][column_index-1]!=" " and board[row_index+1][column_index-1]!=" " and board[row_index+1][column_index]!=" " and board[row_index+1][column_index+1]!=" " and board[row_index][column_index+1]!=" " and  board[row_index-1][column_index+1]!=" ":
            return True
        else:
            return False
    
def check(board,row,column):
    if board[row][column]==" ":
        return True
    else:
        return False

def main():
    cont="Y"
    while cont=="Y":
        player1,player2=Choosing_Symbol()
        Num=take_number()
        board=Create_board(Num)
        board[Num-1][Num//2]=player1
        board[0][Num//2]=player2
        print_board(board,Num)
        cont="Y"
        while True:
            Move_symbol(board,player1,Num)
            if is_finished(board,player2,Num):
                print(f"\nPlayer {player1} won the game.")
                break
            set_stone(board,player1,Num)
            if is_finished(board,player2,Num):
                print(f"\nPlayer {player1} won the game.")
                break
            Move_symbol(board,player2,Num)
            if is_finished(board,player1,Num):
                print(f"\nPlayer {player2} won the game.")
                break
            set_stone(board,player2,Num)
            if is_finished(board,player1,Num):
                print(f"\nPlayer {player2} won the game.")
                break
        cont=input("Would you like to play again(Y/N):")
        while not cont in "YyNn":
            cont=input("Would you like to play again(Y/N):")  
        cont=cont.upper()

main()

    
