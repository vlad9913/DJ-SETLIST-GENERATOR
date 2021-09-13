# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:27:32 2021

@author: Vlad
"""
from GA.chromosome import Chromosome
class GeneticAlgorithm():
    def __init__(self,setlistSize,nrGens,popLength,csvreader,energy_function,dance_function
                 ,valence_function,dance_diff,energy_diff,valence_diff):
        self.__setlistSize = setlistSize
        self.__nrGens = nrGens
        self.__popLength = popLength
        self.__tracks = csvreader.readCsv()
        self.__energyFunction = energy_function
        self.__danceFunction = dance_function
        self.__valenceFunction = valence_function
        self.__dance_diff = dance_diff
        self.__energy_diff = energy_diff
        self.__valence_diff = valence_diff
    
    
    def fitness_evaluation_old(self,chromosome):
        energy_sum = 0
        dance_sum = 0
        valence_sum = 0
        for index,atom in enumerate(chromosome.get_repres()):
            relative_position = 0.1 + index * (0.8 / self.__setlistSize)
            energy_sum += (abs(float(self.__energyFunction(relative_position))- float(atom['energy'])) + 0.000001)
            dance_sum += (abs(float(self.__danceFunction(relative_position))- float(atom['danceability'])) + 0.000001)
            valence_sum += (abs(float(self.__valenceFunction(relative_position))- float(atom['valence'])) + 0.000001)
        
        
        #the bigger it is, the worse the fitness, so we flip it
        
        
        return 1/(energy_sum+dance_sum+valence_sum)
    

    def fitness_evaluation(self,chromosome):
        energy_sum = 0
        dance_sum = 0
        valence_sum = 0
        
        chr_dance_diff = chromosome.get_max_dance()[0] - chromosome.get_min_dance()[0]
        dance_rate = chr_dance_diff / self.__dance_diff
        
        chr_energy_diff = chromosome.get_max_energy()[0] - chromosome.get_min_energy()[0]
        energy_rate = chr_energy_diff / self.__energy_diff
        
        chr_valence_diff = chromosome.get_max_valence()[0] - chromosome.get_min_valence()[0]
        valence_rate = chr_valence_diff / self.__valence_diff
        
        chromo = chromosome.get_repres()
        
        for i in range(len(chromo[:-1])):            
            relative_position = 0.1 + i * (0.8 / self.__setlistSize)
            relative_position_next =  0.1 + (i+1) * (0.8 / self.__setlistSize)
       
            best_dance = dance_rate * (float(self.__danceFunction(relative_position_next)) - float(self.__danceFunction(relative_position)))
            actual_dance = float(chromo[i+1]['danceability']) - float(chromo[i]['danceability']) 
            dance_score = self.evaluate_rate(actual_dance,best_dance) / self.__setlistSize
            dance_sum += dance_score 
            
            best_energy = energy_rate * (float(self.__energyFunction(relative_position_next)) - float(self.__energyFunction(relative_position)))
            actual_energy = float(chromo[i+1]['energy']) - float(chromo[i]['energy']) 
            energy_score = self.evaluate_rate(actual_energy,best_energy) / self.__setlistSize
            energy_sum += energy_score
            
            best_valence = valence_rate * (float(self.__valenceFunction(relative_position_next)) - float(self.__valenceFunction(relative_position)))
            actual_valence = float(chromo[i+1]['valence']) - float(chromo[i]['valence']) 
            valence_score = self.evaluate_rate(actual_valence,best_valence) / self.__setlistSize
            valence_sum += valence_score
            
        return (dance_sum+energy_sum+valence_sum)/3
            
    '''
    actual = actual difference between current point and the next
    best = best difference 
    
    output : float value representing the score, best possibile score being 1
    '''   
    def evaluate_rate(self,actual,best):
        import numpy as np
        evaluation = 0
        if np.sign(actual)!=np.sign(best):
            return evaluation
        # return 0 if the actual difference has a diff sign that the best 
        # difference : it means that the trend has the opposite direction than
        # the trend we want to achieve, so we give it the worst possible score: 0
        evaluation = self.my_quadratic_formula(best,best-actual)
        return evaluation    
            
        
    def my_quadratic_formula(self,denominator,x):   
        value = -(x/(denominator+0.000000001))**2 + 1
        if value >=0:
            return value
        return 0
    
    

    def evolution(self):
        import random
        import numpy.random as npr
        population = []
        maxFitness = 0

        i=0
        
        while i < self.__popLength-1:
            c = Chromosome(self.__setlistSize,self.__tracks,1)
            c.fitness = self.fitness_evaluation(c)
            if c.fitness > 0:
                population.append(c)
                
                if c.fitness > maxFitness:
                    maxFitness = c.fitness
                    bestChromosome = c
                
                i+=1
        
        for i in range(self.__nrGens):
            
            newPopulation = []
            newPopulation.append(bestChromosome)
            
            max = sum([c.get_fitness() for c in population])
            if max !=0 :
                selection_probs = [c.get_fitness()/max for c in population]
            else: 
                selection_probs = [1/len(population) for c in population]
            
            for j in range(self.__popLength-1):

                
                mother1 = population[npr.choice(len(population), p = selection_probs)]
                father1 = population[npr.choice(len(population), p = selection_probs)]
                
                mother2 = population[npr.choice(len(population), p = selection_probs)]
                father2 = population[npr.choice(len(population), p = selection_probs)]
                
                if mother1.get_fitness() > mother2.get_fitness():
                    mother = mother1
                else:
                    mother = mother2
                    
                if father1.get_fitness() > father2.get_fitness():
                    father = father1
                else:
                    father = father2
               
                
                c1 = mother.crossover(father)   
                
                c1.mutation()
                c1.set_fitness(self.fitness_evaluation(c1))
               
                c2 = father.crossover(mother)
                
                c2.mutation()
                c2.set_fitness(self.fitness_evaluation(c2))
                
                if c1.get_fitness() > c2.get_fitness():
                    child = c1
                else:
                    child = c2        
                    
                newPopulation.append(child)
                
                if maxFitness < child.get_fitness():
                    maxFitness = child.get_fitness()
                    bestChromosome = child

            print("Generation "+ str(i+1) +"'s best fit: "+str(bestChromosome.get_fitness()))
            population = newPopulation
                
                
        return bestChromosome
                
                
                
                
                
                
                
                
                