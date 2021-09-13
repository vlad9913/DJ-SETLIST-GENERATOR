# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:37:06 2021

@author: Vlad
"""

'''
input: n - chromosome length (number of songs)
       tracks - array of dictionaries representing songs, from where we choose
                our atoms

'''

def generate_a_random_chromosome(n,tracks):
    import random
    repres = []
    minenergy = [1,0]
    maxenergy = [0,0]
    mindance = [1,0]
    maxdance = [0,0]
    minvalence = [1,0]
    maxvalence = [0,0]
    for i in range(n):
        choice = random.choice(tracks)
        repres.append(choice)
        
        if float(choice['energy']) < minenergy[0]:
            minenergy = [float(choice['energy']),i]
        if float(choice['energy']) > maxenergy[0]:
            maxenergy = [float(choice['energy']),i]
        
        if float(choice['danceability']) < mindance[0]:
            mindance = [float(choice['danceability']),i]
        if float(choice['danceability']) > maxdance[0]:
            maxdance =[float(choice['danceability']),i]
        
        if float(choice['valence'])<minvalence[0]:
            minvalence = [float(choice['valence']),i]
        if float(choice['valence'])>maxvalence[0]:
            maxvalence = [float(choice['valence']),i]
    
    return repres,minenergy,maxenergy,mindance,maxdance,minvalence,maxvalence

class Chromosome:
    def __init__(self,n,tracks,option):
        self.__repres = []
        self.min_energy = [1,0]
        self.max_energy = [0,0]
        self.min_dance = [1,0]
        self.max_dance = [0,0]
        self.min_valence = [1,0]
        self.max_valence = [0,0]
        if option==1:
            self.__repres,self.min_energy,self.max_energy,self.min_dance,self.max_dance, self.min_valence,self.max_valence = generate_a_random_chromosome(n,tracks)
        self.__fitness = 0.0
        self.__length = n
        self.__tracks = tracks
                 
   
    def get_repres(self):
        return self.__repres
    
    def get_fitness(self):
        return self.__fitness

    def set_repres(self, l):
        self.__repres = l

    def set_fitness(self, fit):
        self.__fitness = fit
    
    def get_length(self):
        return self.__length
    
    def get_min_dance(self):
        return self.min_dance
    
    def set_min_dance(self, d):
        self.min_dance = d
        
    def get_max_dance(self):
        return self.max_dance
    
    def set_max_dance(self,d):
        self.max_dance = d
        
    def get_min_energy(self):
        return self.min_energy
    
    def set_min_energy(self,e):
        self.min_energy = e
        
    def get_max_energy(self):
        return self.max_energy
    
    def set_max_energy(self,e):
        self.max_energy = e
    
    def get_min_valence(self):
        return self.min_valence
    
    def set_min_valence(self,v):
        self.min_valence = v
    
    def get_max_valence(self):
        return self.max_valence
    
    def set_max_valence(self,v):
        self.max_valence = v

    def get(self,attrname):
        return getattr(self,attrname)

   
    def crossover(self,c):
        #Two cutting points
        import random
        pos1 = random.randint(1,self.__length-2)
        pos2 = random.randint(1,self.__length-2)
    #    pos2=self.__length-2
        
        if (pos2<pos1):
            pos1,pos2 = pos2,pos1
        
        '''
        newrepres = self.__repres[pos1:pos2]
    
        
        for el in c.get_repres()[pos2:] + c.get_repres()[:pos2]:
                if(len(newrepres) < self.__length):
                    newrepres.append(el)
                
        ''' 
        max_en1 = max_en2 = max_da1 = max_da2 = max_va1 = max_va2 = [0,0]
        min_en1 = min_en2 = min_da1 = min_da2 = min_va1 = min_va2 = [1,0]
        
        #First Chromosome's extremes
        if self.max_energy[1] < pos1 or self.max_energy[1] > pos2:
            max_en1 = self.max_energy
        if self.min_energy[1] < pos1 or self.min_energy[1] > pos2:
            min_en1 = self.min_energy
        if self.max_dance[1] < pos1 or self.max_dance[1] > pos2:
            max_da1 = self.max_dance
        if self.min_dance[1] < pos1 or self.min_dance[1] > pos2:
            min_da1 = self.min_dance
        if self.max_valence[1] < pos1 or self.max_valence[1] > pos2:
            max_va1 = self.max_valence
        if self.min_valence[1] < pos1 or self.min_valence[1] > pos2:
            min_va1 = self.min_valence
        
        
        #Second Chromosome's extremes
        if c.get_max_energy()[1]>=pos1 and c.get_max_energy()[1] <= pos2:
            max_en2 =  c.get_max_energy()
        if c.get_min_energy()[1]>=pos1 and c.get_min_energy()[1] <= pos2:
            min_en2 =  c.get_min_energy()
        if c.get_max_dance()[1]>=pos1 and c.get_max_dance()[1] <= pos2:
            max_da2 =  c.get_max_dance()
        if c.get_min_dance()[1]>=pos1 and c.get_min_dance()[1] <= pos2:
            min_da2 =  c.get_min_dance()
        if c.get_max_valence()[1]>=pos1 and c.get_max_valence()[1] <= pos2:
            max_va2 =  c.get_max_valence()
        if c.get_min_valence()[1]>=pos1 and c.get_min_valence()[1] <= pos2:
            min_va2 =  c.get_min_valence()
        
        
        
        
                 
        newrepres = self.get_repres()[:pos1]
        for atom in c.get_repres()[pos1:pos2]:
            if atom not in newrepres:
                newrepres.append(atom)
            else:
                newrepres.append(random.choice(self.__tracks))
       
        for atom in self.get_repres()[pos2:]:
            if atom not in newrepres:
                newrepres.append(atom)
            else:
                newrepres.append(random.choice(self.__tracks))
        
        
        if max_en1[0]>max_en2[0]:
            max_en = max_en1
        else:
            max_en = max_en2
            
        if max_da1[0]>max_da2[0]:
            max_da = max_da1
        else:
            max_da = max_da2    
            
        if max_va1[0]>max_va2[0]:
            max_va = max_va1
        else:
            max_va = max_va2
            
        if min_en1[0]<min_en2[0]:
            min_en = min_en1
        else:
            min_en = min_en2
            
        if min_da1[0]<min_da2[0]:
            min_da = min_da1
        else:
            min_da = min_da2
        
        if min_va1[0]<min_va2[0]:
            min_va = min_va1
        else:
            min_va = min_va2
            
            
        offspring = Chromosome(self.__length,self.__tracks,0)
        offspring.set_repres(newrepres)
        offspring.set_min_energy(min_en)
        offspring.set_max_energy(max_en)
        offspring.set_min_dance(min_da)
        offspring.set_max_dance(max_da)
        offspring.set_min_valence(min_va)
        offspring.set_max_valence(max_va)

        return offspring

    def mutation(self):
        #insert mutation
        import random
        
        strings_max = ['max_energy','max_dance','max_valence']
        strings_min = ['min_energy','min_dance','min_valence']
        x=random.randint(0,9)
        if x<3:
            for i in range(round(self.__length/15)):
                pos = random.randint(0,self.__length-1)
                pos2 = random.randint(0,self.__length-1)
                for atr in strings_max+strings_min:
                    poz=-1
                    if self.get(atr)[1]==pos:
                        poz = pos
                    if self.get(atr)[1]==pos2:
                        poz = pos2 
                    if poz!=-1:
                        setattr(self,atr,[getattr(self,atr)[0],poz])    
                        
                self.__repres[pos],self.__repres[pos2]=self.__repres[pos2],self.__repres[pos]
                
            
        #x = random.randint(0,self.__length)
        #if x<=self.__length/4: 
        for position in range(self.__length):
            if (random.randint(0,self.__length-1)==1):
                #position = random.randint(0,self.__length-1)
                self.__repres[position] = random.choice(self.__tracks)
                en = self.__repres[position]['energy']
                da = self.__repres[position]['danceability']
                va = self.__repres[position]['valence']
                
                if float(en) > self.max_energy[0]:
                    self.max_energy = [float(en),position]
                else:
                    if float(en) < self.min_energy[0]:
                        self.min_energy = [float(en),position]
                
                if float(da) > self.max_dance[0]:
                    self.max_dance = [float(da),position]
                else:
                    if float(da) < self.min_dance[0]:
                        self.min_dance = [float(da),position]
                
                if float(va) > self.max_valence[0]:
                    self.max_valence = [float(va),position]
                else:
                    if float(va) < self.min_valence[0]:
                        self.min_valence = [float(va),position]
                         
            

    def __str__(self):
        return "\nChromo: " + str([x['name'] for x in self.__repres]) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness_repres and self.__fitness == c.__fitness