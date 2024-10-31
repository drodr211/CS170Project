from copy import deepcopy
class Node:
    def __init__(self, state, gn):
        self.state = state
        self.gn = gn
        self.hn = None

def findZero(state):
    done = False
    i = 0
    j = 0
    for row in state:
        j = 0
        for item in row:
            if item == 0:
                done = True
                break
            j = j + 1
        if done: break
        i = i + 1

    return [i, j]


def moveUp(currState):
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i-1][j]
    newState[i - 1][j] = 0
    newState[i][j] = oldNum

    return newState

def moveDown(currState):
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i+1][j]
    newState[i + 1][j] = 0
    newState[i][j] = oldNum

    return newState

def moveLeft(currState):
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i][j-1]
    newState[i][j-1] = 0
    newState[i][j] = oldNum

    return newState

def moveRight(currState):

    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i][j+1]
    newState[i][j+1] = 0
    newState[i][j] = oldNum

    return newState


def expandNode(node, currGn):
    print("Expanding State: \n")
    print(*node.state[0])
    print(*node.state[1])
    print(*node.state[2])

    if 0 not in node.state[0]:
        nodeUp = Node(moveUp(node.state), currGn+1)
    if 0 not in node.state[2]:
        nodeDown = Node(moveDown(node.state), currGn+1)

    nodeLeft = Node(moveLeft(node.state), currGn+1)

    nodeRight = Node(moveRight(node.state), currGn+1)
    
    

    

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


