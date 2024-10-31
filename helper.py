from copy import deepcopy
import sys
import math

goal_state = [[1,2,3],[4,5,6],[7,8,0]]
goalCoords = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1)]

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

def distance(c1, c2):
    return math.sqrt(((c1[0] - c2[0]) ** 2) + ((c1[1] - c2[1]) ** 2))

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
    hn = 0
    for r in range(0, 3) :
        for c in range(0, 3):
            if state[r][c] == 0:
                continue
            elif state[r][c] != goal_state[r][c]: 
                hn += 1
    return hn

def astar_eucDist(state):
    hn = 0

    for r in range(0, 3):
        for c in range(0, 3):
            if state[r][c] == goal_state[r][c] or state[r][c] == 0:
                continue
            
            else: 
                dist = distance(goalCoords[state[r][c] - 1], [r,c])
                print(dist)
                hn += dist

    return hn

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


