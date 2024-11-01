from helper import *
import helper
import time

state1 = [[0,1,2],[4,5,3],[7,8,6]] #trivial depth = 4
state2 = [[6,2,0],[1,7,4],[5,8,3]] #depth 16 66/50
state3 = [[0,2,4],[6,1,7],[5,8,3]] #depth 20 321/195
state4 = [[3,7,6],[8,1,5],[4,2,0]] #depth 22 980/576
state5 = [[3,2,1],[8,7,6],[0,4,5]] # depth 22 1416/837


states = [state1, state2,  state3, state4, state5]


# euclidean distance on all test cases
for s in states:
    helper.nodes_expanded = 0
    helper.explored = dict()

    n = Node(s, 0)
    print("##############################################")
    print(" Using puzzle:")
    print(" ", *n.state[0])
    print(" ", *n.state[1])
    print(" ", *n.state[2])
    print(" Using euclidean  ...", end = "")

    st = time.time()
    search(n, 3, 0)
    end = time.time()
    print("    Elapsed Time:    ",str(end - st)[:8], "s\n\n")


# misplaced tile on all test cases
for s in states:
    helper.nodes_expanded = 0
    helper.explored = dict()

    n = Node(s, 0)
    print("##############################################")
    print(" Using puzzle:")
    print(" ", *n.state[0])
    print(" ", *n.state[1])
    print(" ", *n.state[2])
    print(" Using misplaced tile heuristic...", end = "")

    st = time.time()
    search(n, 2, 0)
    end = time.time()
    print("    Elapsed Time:    ",str(end - st)[:8], "s\n\n")


# ucs on all test cases
for s in states:
    helper.nodes_expanded = 0
    helper.explored = dict()

    n = Node(s, 0)
    print("##############################################")
    print(" Using puzzle:")
    print(" ", *n.state[0])
    print(" ", *n.state[1])
    print(" ", *n.state[2])
    print(" Using ucs...", end = "")

    st = time.time()
    search(n, 1, 0)
    end = time.time()
    print("    Elapsed Time:    ",str(end - st)[:8], "s\n\n")