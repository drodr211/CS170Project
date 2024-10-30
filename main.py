class State:
    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

class Node:
    def __init__(self, state, childrenNodes):
        self.state = state       # state object
        self.children = childrenNodes # set of children nodes

class Tree:
    def __init__(self, rootNode):
        self.root = rootNode         # node object

def buildTree(rootNode):
    tree = Tree(rootNode)
    return tree                  # return a tree object

def UCS():
    return None

def ASMT()
    return None

def ASED()
    return None


##############  PROGRAM STARTS HERE  ################

print("\nWelcome to drodr211's 8 puzzle solver.")

puzzleChoice = 1
puzzleChoice = int(input("Type “1” to use a default puzzle, or “2” to enter your own puzzle. \n\n >>> ")) #for later use

match puzzleChoice:
    case 1: #use default puzzle
        r1 = "103" 
        r2 = "426" 
        r3 = "758" 
        print("\nUsing default puzzle: \n 103 \n 426 \n 758 \n")
    case 2: #use user puzzle
        r1 = input("\nEnter row 1:")
        r2 = input("Enter row 2:")
        r3 = input("Enter row 3:")
        print("\nUsing puzzle: \n" + r1 + "\n" + r2 +  "\n" + r3 + "\n")
    case _:
        exit(1)


startState = State(r1, r2, r3)
startNode = Node(startState, None)
fullTree = buildTree(startNode)

algoChoice = 1
algoChoice = int(input("Enter your choice of algorithm: \n1. Uniform Cost Search \n2. A* with the Misplaced Tile heuristic. \n3. A* with the Euclidean distance heuristic.\n\n >>> "))

match algoChoice:
    case 1:
        # run uc
        print("\nUsing Uniform Cost Search")
        UCS(fullTree)
    case 2:
        #A* with 
        print("\nUsing A* with misplaced tile search")
        ASMT(fullTree)
    case 3:
        #euclidean 
        print("\nUsing A* with euclidean distance search")
        ASED(fullTree)
    case _:
        exit(1)


# 1) Uniform Cost Search1 ( g(n) + 0)
# 2) A* with the Misplaced Tile heuristic ( g(n) + h(n) (misplaced tiles))
# 3) A* with the Euclidean Distance heuristic( g(n) + h(n) (euclidean sum) )

