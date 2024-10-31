from helper import *

##############  PROGRAM STARTS HERE  ################

print("\nWelcome to drodr211's 8-puzzle solver.")

puzzleChoice = 1
puzzleChoice = int(input("Type “1” to use a default puzzle, or “2” to enter your own puzzle. \n\n >>> ")) #for later use

match puzzleChoice:
    case 1: #use default puzzle
        r1 = [1,0,3]
        r2 = [4,2,6]
        r3 = [7,5,8]
        print("\nUsing default puzzle: \n")
    case 2: #use user puzzle
        r1 = list(map(int, input("\nEnter row 1: ").split()))
        r2 = list(map(int, input("Enter row 2: ").split()))
        r3 = list(map(int, input("Enter row 3: ").split()))
        print("\nUsing puzzle: \n")
    case _:
        exit(1)

print(*r1) 
print(*r2) 
print(*r3)

state = [r1, r2, r3]
startNode = Node(state, 0)

algoChoice = 1
algoChoice = int(input("\nEnter your choice of algorithm: \n1. Uniform Cost Search \n2. A* with the Misplaced Tile heuristic. \n3. A* with the Euclidean distance heuristic.\n\n >>> "))

match algoChoice:
    case 1: 
        print("\nUsing Uniform Cost Search") # 1) Uniform Cost Search1 ( g(n) + 0)
    case 2: 
        print("\nUsing A* with misplaced tile search") # 2) A* with the Misplaced Tile heuristic ( g(n) + h(n) (misplaced tiles))
    case 3: 
        print("\nUsing A* with euclidean distance search") # 3) A* with the Euclidean Distance heuristic( g(n) + h(n) (euclidean sum) )
    case _: exit(1)
    
search(startNode, algoChoice)