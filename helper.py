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


