"""
    Fitness = Weight of the path
    Goal = Minimise the weight
"""

from random import choices, randint
from problem.chromosome import Chromosome

class GA:
    def __init__(self, param = None, problParam = None, better = lambda a, b: a.fitness < b.fitness):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        self.__better = better
        
    @property
    def population(self):
        return self.__population
    
    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
    
    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__problParam['network'])
            
    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (self.__better(c, best)):
                best = c
        return best
        
    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if (self.__better(worst, c)):
                worst = c
        return worst

    def selection(self):        
        # Purely Random
        """ pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if (self.__better(self.__population[pos1], self.__population[pos2]):
            return pos1
        else:
            return pos2 """

        # Proportional, based on rank
        indexChromoPairs = [(i, self.__population[i]) for i in range(self.__param['popSize'])]
        # sort the pairs => from worst to best
        # first, sort the chromosomes in ASC order, based on fitness
        indexChromoPairs.sort(key = lambda x : x[1].fitness)
        # if first chromo is better than the second, reverse the order (worst to best)
        if self.__better(indexChromoPairs[0][1], indexChromoPairs[1][1]):
            indexChromoPairs.reverse()
        # assign ranks
        ranks = [[0] for _ in range(self.__param['popSize'])]
        currentRank = 1
        for pair in indexChromoPairs:
            ranks[pair[0]] = currentRank
            currentRank += 1
        # select a random chromosome's index, proportional to the ranks
        choiceList = choices([i for i in range(self.__param['popSize'])], ranks, k = 1)
        return choiceList[0]

    
    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__param['probCrossover'])
            off.mutation(self.__param['probMutation'])
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__param['probCrossover'])
            off.mutation(self.__param['probMutation'])
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
        
    def oneGenerationSteadyState(self):
        """ for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__param['probCrossover'])
            off.mutation(self.__param['probMutation'])
            off.fitness = self.__problParam['function'](off.repres, self.__problParam['network'])
            worst = self.worstChromosome()
            if (off.fitness > worst.fitness):
                worst = off """
        bestOff = Chromosome(self.__problParam)
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__param['probCrossover'])
            off.mutation(self.__param['probMutation'])
            off.fitness = self.__problParam['function'](off.repres, self.__problParam['network'])
            if (self.__better(off, bestOff)):
                bestOff = off
        if self.__better(bestOff, self.worstChromosome()):
            self.__population.remove(self.worstChromosome())
            self.__population.append(bestOff)