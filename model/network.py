class Network:

    # constructor based on networkx graph
    def __init__(self, nxGraph):
        self.__noNodes = nxGraph.number_of_nodes()
        self.__noEdges = nxGraph.size()
        self.__degrees = []
        self.__mat = [[[0] for _ in range(nxGraph.number_of_nodes())] for _ in range(nxGraph.number_of_nodes())]
        
        # initialize degrees
        add = 1 # daca nodurile incep de la 1
        if nxGraph.has_node(0):
            add = 0 # daca nodurile incep de la 0
        for i in range(nxGraph.number_of_nodes()):
            self.__degrees.append(nxGraph.degree[i + add])
        
        # initialize adjacency matrix
        for i in range(nxGraph.number_of_nodes()):
            for j in range(nxGraph.number_of_nodes()):
                if nxGraph.has_edge(i + add, j + add):
                    self.__mat[i][j] = 1
                else:
                    self.__mat[i][j] = 0

    @property
    def noNodes(self): return self.__noNodes

    @property
    def noEdges(self): return self.__noEdges

    @property
    def degrees(self): return self.__degrees

    @property
    def mat(self): return self.__mat