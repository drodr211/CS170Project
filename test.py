from helper import *
import helper
import time


state1 = [[1,2,3],[4,5,6],[7,0,8]]
state2 = [[0,1,2],[4,5,3],[7,8,6]]
state3 = []
state4 = [[2,3,4],[8,5,6],[7,1,0]]
state5 = []
state6 = [[7,2,8],[4,3,5],[1,6,0]]

states = [state1, state2,  state4,  state6]

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

#for s in states:
#    helper.nodes_expanded = 0
#    helper.explored = dict()
#
#    n = Node(s, 0)
#    print("##############################################")
#    print(" Using puzzle:")
#    print(" ", *n.state[0])
#    print(" ", *n.state[1])
#    print(" ", *n.state[2])
#    print(" Using ucs  ...", end = "")
#
#    st = time.time()
#    search(n, 1, 0)
#    end = time.time()
#
#    print("    Elapsed Time:    ",str(end - st)[:8], "s\n\n")





