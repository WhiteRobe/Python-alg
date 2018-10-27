from PriorityQueue import PriorityQueue
from structure import Graph


class DijkstraSP:
    # Notice : In this alg., p2p-distance should be great than zero!
    __distTo = []
    __edgeTo = []
    __start = None
    __graph = None
    __pq = None

    def __init__(self, graph: Graph):
        # V is the sum of point in graph
        # dependency: Graph.class
        self.__graph = graph

    def init(self):
        self.__distTo = [float('inf') for _ in range(0, self.__graph.getV())]
        self.__edgeTo = [None for _ in range(0, self.__graph.getV())]
        self.__pq = PriorityQueue()

    def set_start(self, start_point):
        self.init()
        self.__start = start_point
        self.__distTo[start_point[0]] = 0.0
        self.__pq.insert((start_point, 0.0))
        while self.__pq.size() != 0:
            self.__relax(self.__pq.pop()[0])

    def __relax(self, point):
        # $point should like (point_index, point_info)
        # print("--", point)
        for edge in self.__graph.adj(point):
            w = edge.to()
            # print(edge)
            if self.__distTo[w[0]] > (self.__distTo[point[0]] + edge.weight()):
                self.__distTo[w[0]] = self.__distTo[point[0]] + edge.weight()
                self.__edgeTo[w[0]] = edge
                new_point = (w, edge.weight())
                # print(new_point, self.__pq.get_pq())
                if self.__pq.contains(w):
                    self.__pq.change(w, new_point)
                else:
                    self.__pq.insert(new_point)

    def have_path_to(self, target):
        # $target should like (point_index, point_info)
        return self.__distTo[target[0]] < float('inf')

    def path_to(self, target):
        # $target should like (point_index, point_info)
        paths = []
        if self.have_path_to(target):
            edge = self.__edgeTo[target[0]]
            paths.append(edge)
            while True:
                edge = self.__edgeTo[edge.fr()[0]]
                if edge is None:
                    break
                paths.append(edge)
        paths.reverse()
        return paths

    def min_dist_to(self, target):
        # $target should like (point_index, point_info)
        return self.__distTo[target[0]]


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. prepare dataset
    import datasets
    start, end, g_data, V = datasets.load_dijkstra_data()
    # 2. build DiGraph
    G = Graph(V=V)
    G.set_data(g_data)
    # 3. feed digraph into DijkstraSP
    S = DijkstraSP(G)
    # 4. set start-end point
    S.set_start(start)
    path = S.path_to(end)
    # 5. print shortest-paths and distance
    print("Min-distance is", S.min_dist_to(end))
    for p in path:
        print(p)

