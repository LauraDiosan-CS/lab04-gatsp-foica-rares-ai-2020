class WeightedGraph:

    # constructor based on weight matrix
    # assumes the graph is complete
    def __init__(self, weightMat):
        self.__weightMat = weightMat
        self.__noNodes = len(weightMat)

    def weight(self, u, v):
        return self.__weightMat[u][v]

    @property
    def weightMat(self): return self.__weightMat

    @property
    def noNodes(self): return self.__noNodes
