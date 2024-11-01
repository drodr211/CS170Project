from copy import deepcopy
import sys
import math

goal_state = [[1,2,3],[4,5,6],[7,8,0]]
goalCoords = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1)]
nodes_expanded = 0
explored = dict()

class Node:
    """Node object: state, G(n) and H(n) data members"""
    def __init__(self, state, gn, hn=-1):
        self.state = state
        self.gn = gn
        self.hn = hn
    def __repr__(self):
        return f"  {self.state[0][0]} {self.state[0][1]} {self.state[0][2]}\n  {self.state[1][0]} {self.state[1][1]} {self.state[1][2]}\n  {self.state[2][0]} {self.state[2][1]} {self.state[2][2]}\n  G(n): {str(self.gn)}\n  H(n): {str(self.hn)}"


def findZero(state): 
    """returns x,y coordinates of where the 0 is in the puzzle """
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
    """Returns distance between 2 coordinates"""
    return math.sqrt(((c1[0] - c2[0]) ** 2) + ((c1[1] - c2[1]) ** 2))

def moveUp(currState):
    """Return the state if the 0 was moved up"""
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i-1][j]
    newState[i - 1][j] = 0
    newState[i][j] = oldNum

    return newState

def moveDown(currState):
    """Return the state if the 0 was moved down"""
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i+1][j]
    newState[i + 1][j] = 0
    newState[i][j] = oldNum

    return newState

def moveLeft(currState):
    """Return the state if the 0 was moved left"""
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i][j-1]
    newState[i][j-1] = 0
    newState[i][j] = oldNum

    return newState

def moveRight(currState):
    """Return the state if the 0 was moved right"""
    zeroPos = findZero(currState)
    i = zeroPos[0]
    j = zeroPos[1]

    newState = deepcopy(currState)

    oldNum = newState[i][j+1]
    newState[i][j+1] = 0
    newState[i][j] = oldNum

    return newState

def astar_mispTile(state):
    """Returns the number of misplaced tiles (for misplace hueristic)"""
    hn = 0
    for r in range(0, 3) :
        for c in range(0, 3):
            if state[r][c] == 0:
                continue
            elif state[r][c] != goal_state[r][c]: 
                hn += 1
    return hn

def astar_eucDist(state):
    """Returns the sum of euclidean distance (for eucliedan hueristic)"""
    hn = 0
    for r in range(0, 3):
        for c in range(0, 3):
            if state[r][c] == goal_state[r][c] or state[r][c] == 0:
                continue
            else: 
                dist = distance(goalCoords[state[r][c] - 1], [r,c])
                hn += dist
    return hn

def calcHn(state, algoChoice):
    """Helper function to call correct algorithm to calculate H(n)"""
    if algoChoice == 1: return 0
    if algoChoice == 2: return astar_mispTile(state)
    if algoChoice == 3: return astar_eucDist(state)
    return None

def getHashKey(state):
    """Flattens the state and return this state's hash key"""
    st = ""
    for row in state:
        for column in row:
            st += str(column)
    return st

def solFound(max_queue_size, gn):
    """Helper function to display info when a solution is found"""
    print("\n\nSolution found! ")
    print(f"    Nodes expanded:   {nodes_expanded}")
    print(f"    Max queue length: {max_queue_size}")
    print(f"    Solution depth:   {gn}")

    return 1

def expandNode(node, algoChoice):
    """Expands the node and returns all possible children"""
    children = []
    global nodes_expanded 
    nodes_expanded += 1

    if 0 not in node.state[0]:
        stateUp = moveUp(node.state)
        if(getHashKey(stateUp) not in explored):
            nodeUp = Node(stateUp, node.gn + 1, calcHn(stateUp, algoChoice))
            explored[getHashKey(stateUp)] = True
            children.append(nodeUp)
    if 0 not in node.state[2]:
        stateDown = moveDown(node.state)
        if(getHashKey(stateDown) not in explored):
            nodeDown = Node(stateDown, node.gn + 1, calcHn(stateDown, algoChoice))
            explored[getHashKey(stateDown)] = True
            children.append(nodeDown)
    if node.state[0][0] != 0 and node.state[1][0] != 0 and node.state[2][0] != 0:
        stateLeft = moveLeft(node.state)
        if(getHashKey(stateLeft) not in explored):
            nodeLeft = Node(stateLeft, node.gn + 1, calcHn(stateLeft, algoChoice))
            explored[getHashKey(stateLeft)] = True
            children.append(nodeLeft)
    if node.state[0][2] != 0 and node.state[1][2] != 0 and node.state[2][2] != 0:
        stateRight = moveRight(node.state)
        if(getHashKey(stateRight) not in explored):
            nodeRight = Node(stateRight, node.gn + 1, calcHn(stateRight, algoChoice))
            explored[getHashKey(stateRight)] = True
            children.append(nodeRight)
        
    return deepcopy(children) #return list of children nodes

def search(startNode, algoChoice, trace):
    """main search function"""
    gn = 0
    max_queue_size = 0

    explored[getHashKey(startNode.state)] = True

    #check if initial state is solution
    if startNode.state == goal_state: return solFound(max_queue_size, gn) 

    #intialize frontier list and max queue size
    frontier = expandNode(startNode, algoChoice) 
    frontier = sorted(frontier, key=lambda x:(-(x.gn + x.hn), -x.hn))
    max_queue_size = len(frontier)

    while True:
        #if queue empty, no solution
        if not frontier:                
                print("\nNo solution found.")
                return 1
        
        # pop next best node to expand, display it 
        top_node = frontier.pop()
        if trace: 
            print("The best state is: \n")
            print(top_node)
        
        # and check for goal state
        if top_node.state == goal_state: return solFound(max_queue_size, top_node.gn)


        # add to explored map
        key = getHashKey(top_node.state)
        explored[key] = True


        #increment g counter, expand nodes, append to frontier, sort
        gn += 1
        newNodes = expandNode(top_node, algoChoice)
        if trace: print(" Expanding State......... \n")
        for node in newNodes:
            frontier.append(node)
        frontier = sorted(frontier, key=lambda x:(-(x.gn + x.hn), -x.hn))
        
        # update max queue size in case it changed
        max_queue_size = max(max_queue_size, len(frontier))