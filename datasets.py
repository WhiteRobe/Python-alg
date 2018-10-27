from structure import *


def load_dijkstra_data():
    #  Graph : [point] (distance)
    #
    #        [1]  -  (0.31) -  [5]
    #      /  |  \          /   |
    #  (0.4) (1)  (2)   (1.1)  (2)
    #    /    |    \   /        |
    # [2] - (0.5) - [3]  -(1)- [7] - (9) - [8]
    #   \     |     /  \        |
    #   (2)  (1) (0.5)  (1)   (0.2)
    #     \   |  /         \    |
    #        [0]  -  (0.4)  -  [6]
    #
    start_, end_, V_ = ((2, "2"), (8, "This is the Demo"), 9)
    g_data_ = [WeightedEdge(((0, "0"), (2, "2"), 2)),
               WeightedEdge(((0, "0"), (3, "3"), 1)),
               WeightedEdge(((0, "0"), (4, "4"), 0.5)),
               WeightedEdge(((1, "1"), (2, "2"), 0.4)),
               WeightedEdge(((1, "1"), (3, "3"), 1)),
               WeightedEdge(((1, "1"), (4, "4"), 2)),
               WeightedEdge(((2, "2"), (3, "3"), 0.5)),
               WeightedEdge(((1, "1"), (5, "5"), 0.31)),
               WeightedEdge(((4, "4"), (5, "5"), 1.1)),
               WeightedEdge(((7, "7"), (5, "5"), 2)),
               WeightedEdge(((7, "7"), (4, "4"), 1)),
               WeightedEdge(((7, "7"), (6, "6"), 0.2)),
               WeightedEdge(((4, "4"), (6, "6"), 1)),
               WeightedEdge(((7, "7"), (8, "This is the Demo"), 9)),
               WeightedEdge(((0, "0"), (6, "6"), 0.4))]
    return start_, end_, g_data_, V_


def load_dfs_cycle_data():
    #  Graph : [point] (distance)
    #  Graph : [point] (distance)
    #
    #        [0]     [8] - [9]
    #      /  |  \
    #    [1]-[2]-[3] - [5]
    #      \  |  /    /   \
    #        [4]  - [6] - [7]
    #
    start_ = (0, "0")
    g_data_ = [DirectedEdge(((0, "0"), (1, "1"))),
               DirectedEdge(((0, "0"), (2, "2"))),
               DirectedEdge(((0, "0"), (3, "3"))),
               DirectedEdge(((4, "4"), (1, "1"))),
               DirectedEdge(((4, "4"), (2, "2"))),
               DirectedEdge(((4, "4"), (3, "3"))),
               DirectedEdge(((2, "2"), (1, "1"))),
               DirectedEdge(((2, "2"), (3, "3"))),
               DirectedEdge(((5, "5"), (7, "7"))),
               DirectedEdge(((6, "6"), (7, "7"))),
               DirectedEdge(((5, "5"), (6, "6"))),
               DirectedEdge(((8, "8"), (9, "9"))),
               DirectedEdge(((3, "3"), (5, "5"))),
               DirectedEdge(((4, "4"), (6, "6")))]
    V_ = 10
    return start_, g_data_, V_


def load_dfs_nocycle_data():
    #  Graph : [point] (distance)
    #
    #        [0]    [5] - [6]
    #      /  |  \
    #    [0] [1] [3] - [4]
    #
    start_ = (0, "0")
    g_data_ = [DirectedEdge(((0, "0"), (1, "1"))),
               DirectedEdge(((0, "0"), (2, "2"))),
               DirectedEdge(((0, "0"), (3, "3"))),
               DirectedEdge(((4, "4"), (3, "3"))),
               DirectedEdge(((5, "5"), (6, "6")))]
    V_ = 7
    return start_, g_data_, V_
