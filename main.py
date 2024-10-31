class Node:
    def __init__(self, state, gn):
        self.state = state
        self.gn = gn
        self.hn = None

def moveUp(node):
    state = None
    return state

def moveDown(node):
    state = None
    return state

def moveLeft(node):
    state = None
    return state

def moveRight(node):
    state = None
    return state


def expandNode(startNode, currGn):
    print("Expanding State: \n")
    print(*startNode.state[0])
    print(*startNode.state[1])
    print(*startNode.state[2])

    return None #return list of children nodes


def search(startNode, algoChoice):
    frontier = expandNode(startNode, 0) #intialize frontier list

    while True:
        # if frontier empty 
        #       return failure
        # choose next best node to expand, but 
        # first check if it is a goal state
            # if goal state, return solution or final whatever
        # add node to the explored list or hashmap or something
        # expand the node, add nodes to frontier if not yet explored before
        return None




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
        print("\nUsing Uniform Cost Search")
    case 2: 
        print("\nUsing A* with misplaced tile search")
    case 3: 
        print("\nUsing A* with euclidean distance search")
    case _: exit(1)
    
search(startNode, algoChoice)


# 1) Uniform Cost Search1 ( g(n) + 0)
# 2) A* with the Misplaced Tile heuristic ( g(n) + h(n) (misplaced tiles))
# 3) A* with the Euclidean Distance heuristic( g(n) + h(n) (euclidean sum) )