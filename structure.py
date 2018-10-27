class DirectedEdge:
    _edge = None

    def __init__(self, edge):
        # $edge should like :
        # ( (from_index, point_info), (to_index, point_info) )
        self._edge = edge

    def fr(self):
        return self._edge[0]

    def to(self):
        return self._edge[1]

    def revere(self):
        return WeightedEdge((self._edge[1], self._edge[0]))

    def __str__(self):
        return str(self._edge)


class WeightedEdge(DirectedEdge):

    def __init__(self, edge):
        # $edge should like :
        # ( (from_index, point_info), (to_index, point_info), weight )
        super().__init__(edge)

    def weight(self):
        return self._edge[2]

    def revere(self):
        return WeightedEdge((self._edge[1], self._edge[0], self._edge[2]))


class Graph:
    # dependency : DirectedEdge.Class
    __adj = []
    __points = []
    __edges = []
    __V = 0
    __E = 0

    def __init__(self, V):
        self.__V = V
        self.__adj = [[] for _ in range(0, self.__V)]
        self.__points = set()
        self.__edges = set()

    def set_data(self, data_list, save_points=False, save_edge=False):
        for _ in data_list:
            self.insert(_, save_points=save_points, save_edge=save_edge)

    # noinspection PyTypeChecker
    def insert(self, edge: DirectedEdge, save_points=False, save_edge=False):
        # $edge should be DirectedEdge.class
        # if not isinstance(edge, DirectedEdge):
        #     raise Exception("不是DirectedEdge.class", type(edge))
        self.__adj[edge.fr()[0]].append(edge)
        self.__adj[edge.to()[0]].append(edge.revere())
        if save_points:
            self.__points.add(edge.fr())
            self.__points.add(edge.to())
        if save_edge:
            self.__edges.add(edge)
            self.__edges.add(edge.revere())
        self.__E += 1

    def getV(self):
        return self.__V

    def getE(self):
        return self.__E

    def points(self):
        return  self.__points

    def edges(self):
        return self.__edges

    def adj(self, point):
        # $point should like (point_index, point_info)
        return self.__adj[point[0]]


class TreeNode:
    __left = None
    __right = None
    __value = None
    __father = None
    __other_info = None

    def __init__(self, value=None, left=None, right=None, father=None, **kwargs):
        self.__value = value
        self.__left = left
        self.__right = right
        self.__father = father
        self.__other_info = kwargs

    def set_val(self, value):
        self.__value = value

    def val(self):
        return self.__value

    def set_lc(self, node):
        self.__left = node

    def lc(self):
        return self.__left

    def set_rc(self, node):
        self.__right = node

    def rc(self):
        return self.__right

    def set_fc(self, node):
        self.__father = node

    def fc(self):
        return self.__father

    def other_info(self):
        return self.__other_info

    def copy(self, node):
        self.__left = node.lc()
        self.__right = node.rc()
        self.__value = node.val()
        self.__other_info = node.other_info()

    def __str__(self):
        return "{0}, {1}".format(self.val(), self.other_info())
