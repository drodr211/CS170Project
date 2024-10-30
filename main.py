class State:
    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

class Node:
    def __init__(self, state, children):
        self.state = state
        self.children = children

class Tree:
    def __init__(self, root):
        self.root = root

def buildTree(rootNode):
    tree = Tree(rootNode)

    return tree


print("\nWelcome to drodr211's 8 puzzle solver.")
print("Type “1” to use a default puzzle, or “2” to enter your own puzzle. \n") #for later use

print("Using default puzzle: \n 103 \n 426 \n 758")

r1 = "103" #input("Enter row 1:")
r2 = "426" #input("Enter row 2:")
r3 = "758" #input("Enter row 3:")

startState = State(r1, r2, r3)
startNode = Node(startState, None)


fullTree = buildTree(startNode)

# 1) Uniform Cost Search1 ( g(n) + 0)
# 2) A* with the Misplaced Tile heuristic ( g(n) + h(n) (misplaced tiles))
# 3) A* with the Euclidean Distance heuristic( g(n) + h(n) (euclidean sum) )

