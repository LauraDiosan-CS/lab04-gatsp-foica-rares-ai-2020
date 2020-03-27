# from networkx import read_gml
from model.graph import WeightedGraph
from math import sqrt

class Reader:
    def __init__(self, fileLocation):
        self.__fileLocation = fileLocation

    def readWeigtedGraph(self):
        """
        parses the file; assumes following format:
        >> line 1: nr_of_nodes (n)
        >> line 2: weights_between_node_1_and_all_the_other_nodes (n real values)
        >> ...
        >> line n+1: weights_between_node_n_and_all_the_other_nodes (n real values)
        output: a Weighted Graph 
        """
        with open(self.__fileLocation, "r") as f:
            # read nr_of_nodes
            n = int(f.readline())
            # allocate the matrix
            weightMat = [[[0] for _ in range(n)] for _ in range(n)]
            # read and interpret the lines
            for i in range(n):
                weights = f.readline().split(",")
                for j in range(n):
                    weightMat[i][j] = int(weights[j])
            # return the Weighted Graph build with the parsed matrix
            return WeightedGraph(weightMat)

    def readEil(self):
        with open(self.__fileLocation, "r") as f:
            # first 6 lines
            for _ in range(6):
                f.readline()
            # nodes until EOF
            coords = []
            n = 0
            x = f.readline()
            while x != 'EOF':
                n += 1
                x = x.split(' ')
                pair = (int(x[1]), int(x[2]))
                coords.append(pair)
                x = f.readline()
            # allocate the matrix
            weightMat = [[[0] for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    xi = coords[i][0]
                    yi = coords[i][1]
                    xj = coords[j][0]
                    yj = coords[j][1]
                    dist = (xj-xi)**2 + (yj-yi)**2
                    weightMat[i][j] = sqrt(dist)

            return WeightedGraph(weightMat)

    def getFile(self):
        return self.__fileLocation

    # def readGMLNetwork(self):
    #     return read_gml(self.__fileLocation, label='id')