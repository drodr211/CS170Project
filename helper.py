from copy import deepcopy
import sys

class Node:
    def __init__(self, state, gn, hn=None):
        self.state = state
        self.gn = gn
        self.hn = hn

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

def astar_mispTile(state):




    return None

def astar_eucDist(state):




    
    return None


def calcHn(state, algoChoice):
    if algoChoice == 1: return 0
    if algoChoice == 2: return astar_mispTile(state)
    if algoChoice == 3: return astar_eucDist(state)
    return None


def expandNode(node, currGn, algoChoice):
    print("Expanding State: \n")
    print(*node.state[0])
    print(*node.state[1])
    print(*node.state[2])

    if 0 not in node.state[0]:
        stateUp = moveUp(node.state)
        nodeUp = Node(stateUp, currGn+1, calcHn(stateUp, algoChoice))
    if 0 not in node.state[2]:
        stateDown = moveDown(node.state)
        nodeDown = Node(stateDown, currGn+1, calcHn(stateDown, algoChoice))

    

    #nodeLeft = Node(moveLeft(node.state), currGn+1)

    #nodeRight = Node(moveRight(node.state), currGn+1)
    
    

    

    return None #return list of children nodes


def search(startNode, algoChoice):
    frontier = expandNode(startNode, 0, algoChoice) #intialize frontier list

    while True:
        if not frontier:
                print("No solution found.")
                sys.exit()
        # choose next best node to expand, but 
        # first check if it is a goal state
            # if goal state, return solution or final whatever
        # add node to the explored list or hashmap or something
        # expand the node, add nodes to frontier if not yet explored before
        return None


