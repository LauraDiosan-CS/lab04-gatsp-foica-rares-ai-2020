"""
    Fitness = Weight of the path
    Goal = Minimise the weight
"""

import math
from random import sample, random, randint
from utils.mathematical import permMultiply

class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__fitness = math.inf
        # start out with a random permutation of the nodes
        min = problParam["min"]
        max = problParam["max"]
        self.__repres = sample(range(min, max + 1), k = max - min + 1)


    def crossover(self, c, pc):
        offspring = Chromosome(c.__problParam)

        # if crossover fails, the offspring is identical to one of the parents
        if random() > pc:
            offspring.repres = self.repres[:]
            return offspring

        # else, multiply the permutations
        """ offspring.repres = permMultiply(self.repres, c.repres)
        return offspring """

        # else, "incrucisare ordonata"
        n = len(self.__repres)
        i = randint(0, n - 1)
        j = randint(0, n - 1)
        if i > j:
            i, j = j, i
        offspring.repres = [[-1] for _ in range(n)]
        # copiaza secventa i-j din parintele1
        for k in range(i, j + 1):
            offspring.repres[k] = self.__repres[k]
        # completeaza restul pozitiilor cu elemente din parintele2
        k = (j + 1) % n
        p2 = k
        while k != i:
            if c.__repres[p2] not in offspring.repres:
                offspring.repres[k] = c.__repres[p2]
                k = (k + 1) % n
            p2 = (p2 + 1) % n
        return offspring

    
    def mutation(self, pm):
        # swap mutation
        """ if random() <= pm:
            gene1 = randint(0, len(self.__repres) - 1)
            gene2 = randint(0, len(self.__repres) - 1)
            self.__repres[gene1], self.__repres[gene2] = self.__repres[gene2], self.__repres[gene1] """

        # scramble mutation
        # for each gene, swap it with another random gene; account for probability of mutation (pm)
        for gene1 in range(len(self.__repres)):
            if random() <= pm:
                gene2 = randint(0, len(self.__repres) - 1)
                self.__repres[gene1], self.__repres[gene2] = self.__repres[gene2], self.__repres[gene1]
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
        
    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness