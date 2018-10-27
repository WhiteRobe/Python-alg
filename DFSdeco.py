from structure import Graph


# start_point=$ needed
# {$start_point} will be put into chain
def deco_search():
    def wrapper(func):
        def inner_wrapper(*arg, **kwargs):
            self = arg[0]
            self.init()
            points = self._graph.points()
            start_point = kwargs['start_point']
            if len(points) == 0:
                raise Exception("图为空或未启用Graph.insert(*, save_points=True)")
            if start_point is None:
                for p in self._graph.points():
                    if not self._marked[p[0]]:
                        kwargs['start_point'] = p
                        func(*arg, **kwargs)
            else:
                # kwargs['start_point'] = start_point
                func(*arg, **kwargs)
        return inner_wrapper
    return wrapper


# point=$ needed
# {$point, $point_next} will be put into chain
def deco_dfs():
    def wrapper(func):
        def inner_wrapper(*arg, **kwargs):
            point = kwargs['point']
            self = arg[0]
            self._marked[point[0]] = True
            for edge in self._graph.adj(point):
                p = edge.fr() if point == edge.to() else edge.to()
                kwargs.update({"point_next": p})
                func(*arg, **kwargs)
        return inner_wrapper
    return wrapper


class DFS:
    _graph = None
    _marked = None

    def __init__(self, graph: Graph):
        # dependency: Graph.class
        self._graph = graph

    def init(self):
        self._marked = [False for _ in range(0, self._graph.getV())]

    @deco_search()
    def search(self, *arg, start_point=None, **kwargs):
        # when start_pint is None, DFS the whole graph
        self._dfs(self, *arg, point=start_point, **kwargs)

    @deco_dfs()
    def _dfs(self, *arg, point=None, **kwargs):
        p = kwargs["point_next"]
        if not self._marked[p[0]]:
            self._dfs(self, *arg, point=p, **kwargs)

    def get_marked(self):
        return self._marked


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. prepare dataset
    import datasets
    start, g_data, V = datasets.load_dfs_cycle_data()
    # 2. build DiGraph
    G = Graph(V=V)
    G.set_data(g_data, save_points=True)
    # 3. feed graph into DFS
    S = DFS(G)
    # 4. set start point
    S.search(start_point=start)
    # 5. get result
    print(S.get_marked())

'''
There are two more samples shows how to use dfs-decoration
'''


# There is a demo that how to decoration your DFS-alg:
# DFSCycle used to search a cycle in the graph
class DFSCycle(DFS):
    __hasCircle = False
    __circles = 0

    def __init__(self, graph: Graph):
        # dependency: Graph.class
        super().__init__(graph)

    def init(self):
        super().init()
        self.__hasCircle = False
        self.__circles = 0

    @deco_search()
    def search(self, *arg, start_point=None, **kwargs):
        kwargs.update({"pre": start_point})
        self._dfs(*arg, point=start_point, **kwargs)

    @deco_dfs()
    def _dfs(self, *arg, point=None, **kwargs):
        pre = kwargs['pre']
        p = kwargs['point_next']
        if not self._marked[p[0]]:
            kwargs['pre'] = point
            self._dfs(*arg, point=p, **kwargs)
        elif p != pre:
            self.__hasCircle = True
            self.__circles += 1

    def has_circle(self):
        return self.__hasCircle

    def sum_circle(self):
        return self.__circles // 2


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. prepare dataset
    import datasets
    start2, g_data2, V2 = datasets.load_dfs_cycle_data()
    # 2. build DiGraph
    G2 = Graph(V=V2)
    G2.set_data(g_data2, save_points=True)
    # 3. feed graph into DFSCycle
    S2 = DFSCycle(G2)
    # 4. set start point
    S2.search(start_point=None)
    # 5. get result
    print(S2.has_circle(), S2.sum_circle())


# There is another demo that how to decoration your DFS-alg:
# DFSBinary used to estimate the graph is a binary-graph or not
class DFSBinary(DFS):
    __isBinary = True
    __color = []

    def __init__(self, graph: Graph):
        # dependency: Graph.class
        super().__init__(graph)

    def init(self):
        super().init()
        self.__isBinary = True
        self.__color = [False for _ in range(0, self._graph.getV())]

    @deco_search()
    def search(self, *arg, start_point=None, **kwargs):
        self._dfs(self, *arg, point=start_point, **kwargs)

    @deco_dfs()
    def _dfs(self, *arg, point=None, **kwargs):
        p = kwargs["point_next"]
        if not self._marked[p[0]]:
            self.__color[p[0]] = not self.__color[point[0]]
            self._dfs(self, *arg, point=p, **kwargs)
        elif self.__color[p[0]] == self.__color[point[0]]:
            self.__isBinary = False

    def is_binary(self):
        return self.__isBinary


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. prepare dataset
    import datasets
    start3, g_data3, V3 = datasets.load_dfs_nocycle_data()
    # 2. build DiGraph
    G3 = Graph(V=V3)
    G3.set_data(g_data3, save_points=True)
    # 3. feed graph into DFSCycle
    S3 = DFSBinary(G3)
    # 4. set start point
    S3.search(start_point=None)
    # 5. get result
    print(S3.is_binary())
