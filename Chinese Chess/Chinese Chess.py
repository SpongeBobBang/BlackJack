# CS3 Yuzhao Heng Stefan
def Intro():
    print("Welcome to Chinese Chess game!"
          "\nK stands for King which can move 1 unoccupied square horizontally or vertically within the 9 squares; the 2 kings can’t face each other. "
          "\nQ stands for Queen which can move 1 unoccupied square diagonally within the 9 squares; "
          "\nB stands for Bishop which can move 2 unoccupied squares diagonally within one’s side; "
          "\nD stands for dragon which can move diagonally in a 2*3 squares but can’t move so if there’s one chess piece next to it in the direction of “3”; "
          "\nR stands for rook which can move any number of unoccupied squares horizontally or vertically but can’t go across a piece; "
          "\nC stands for catapult which can move any number of unoccupied squares horizontally or vertically as long as there’s one chess piece between the move; "
          "\nP stands for pawn which can move forwards in one’s own side and can move both forwards and horizontally on the opposite sides. "
          "\nThe chess piece of one side is eaten when chess piece from the other side moves to its position."
          "\nPlayer on the red side starts first. Each player move their chess piece once. "
          "\nPlayer’s goal is to eat the opponent’s king, which decides the winner."
          "\nEach move is done by first inputting the row and column number of the location of a piece you want to move, then inputting desired location. "
          )

def SetBoard():
    global Board
    Board = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,"R2", "D2", "B2", "Q2", "K2", "Q2", "B2", "D2", "R2"], 
                [0,"__", "__", "__", "__", "__", "__", "__", "__", "__"], 
                [0,"__", "C2", "__", "__", "__", "__", "__", "C2", "__"],
                [0,"P2", "__", "P2", "__", "P2", "__", "P2", "__", "P2"], 
                [0,"__", "__", "__", "__", "__", "__", "__", "__", "__"], 
                [0,"__", "__", "__", "__", "__", "__", "__", "__", "__"], 
                [0,"P1", "__", "P1", "__", "P1", "__", "P1", "__", "P1"], 
                [0,"__", "C1", "__", "__", "__", "__", "__", "C1", "__"], 
                [0,"__", "__", "__", "__", "__", "__", "__", "__", "__"], 
                [0,"R1", "D1", "B1", "Q1", "K1", "Q1", "B2", "D2", "R2"]
                ]

def SetAccount():
    global ID1
    global ID2
    ID1 = str(input("Enter player red's name: "))
    ID2 = str(input("Enter player blue's name: "))

def PrintAccount():
    print("Player red's name is:",ID1,"\nPlayer blue's name is:",ID2)

def OutputBoard():
    for Row in range (1,11):
        for Column in range (1,10):
            print("[",Board[Row][Column],"]",end=" ")
        print()
        print()

def Main():
    Intro()
    SetBoard()
    SetAccount()
    PrintAccount()
    OutputBoard()

Main()

