# import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from random import seed, choices
from infrastructure.reader import Reader
from infrastructure.writer import Writer
from model.network import Network
from problem.algorithm import GA
from problem.chromosome import Chromosome
from problem.problemutils import pathCost, translateNodes

def main():
    #seed(1)

    fname = "100p_fricker26.txt"
    dataIn = "data/" + fname
    dataOut = "data_out/out1_" + fname

    # read the graph from file
    reader = Reader(dataIn)
    net = reader.readWeigtedGraph()

    # initialise GA parameters
    gaParam = {'popSize' : 50, 'noGen' : 3000, 'probCrossover' : 0.8, 'probMutation' : 0.12}
    # initialise problem parameters
    problParam = {'min' : 0, 'max' : net.noNodes - 1, 'function' : pathCost, 'network' : net}

    allBestFitnesses = []
    allBestChromosomes = []
    overallBest = Chromosome(problParam)

    # simulate evolution
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    
    for g in range(gaParam['noGen']):
        # algorithm logic
        #ga.oneGeneration()
        #ga.oneGenerationElitism()
        ga.oneGenerationSteadyState()
        
        # gather statistics
        bestChromo = ga.bestChromosome()
        #print('Best solution in generation ' + str(g) + ' is: x = ' + str(translateNodes(bestChromo.repres, 1)) + ' f(x) = ' + str(bestChromo.fitness))
        print('Best solution in generation ' + str(g) + ' f(x) = ' + str(bestChromo.fitness))
        allBestFitnesses.append(bestChromo.fitness)
        allBestChromosomes.append(bestChromo)
        if bestChromo.fitness < overallBest.fitness:
            overallBest = bestChromo

    # output data to file
    writer = Writer(dataOut)
    writer.append(str(net.noNodes), '\n')
    stringNodes = ''
    for node in translateNodes(overallBest.repres, 1):
        stringNodes += str(node) + ','
    stringNodes = stringNodes[:-1]
    writer.append(stringNodes, '\n')
    writer.append(str(overallBest.fitness), '\n')

    # writer.append(str(communities(overallBest)), '\n')
    # simpleRepres = simplifyRepresentation(overallBest.repres)
    # for i in range(len(simpleRepres)):
    #     writer.append(str(i), " ", str(simpleRepres[i]), '\n')
    # i = 0
    # for chromo in generationsBest:
    #     writer.append("gen ", str(i), ": communities = ", str(communities(chromo)), " || fit = ", str(round(chromo.fitness, 3)), '\n')
    #     i += 1

    # visualize graph
    # plt.figure(figsize=(6, 6))  # image size
    # plt.figure(1)
    # #nx.draw(G)
    # A = np.matrix(net.mat)
    # G = nx.from_numpy_matrix(A)
    # pos = nx.spring_layout(G)  # compute graph layout
    # nx.draw_networkx_nodes(G, pos, node_size = 300, node_color = overallBest.repres, cmap = plt.cm.get_cmap(name='hsv'))
    # nx.draw_networkx_edges(G, pos, alpha = 0.3)

    # visualize progresss through generations
    plt.figure(1)
    plt.title("Progression - Fitness (Optimal path cost)")
    plt.xlabel("Generation")
    plt.ylabel("Path cost (Best)")
    plt.plot(allBestFitnesses)

    # plt.figure(2)
    # plt.title("Progression - Nr. of Communities")
    # plt.xlabel("Generation")
    # plt.ylabel("Communities (Best)")
    # plt.plot(allBestNrCommunities)

    plt.show()

if __name__ == "__main__":
    main()
