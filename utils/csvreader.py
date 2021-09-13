# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:30:07 2021

@author: Vlad
"""
import csv


class CSVReader():
    
    def __init__(self,filename,genres):
        self.__filename = filename
        self.__genres = genres
        
    def readCsv(self):
        array=[] #array of dicts
        with open(self.__filename,'r',encoding = "utf-8") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                if row['genre'] in self.__genres:
                    array.append(row)
        return array
                
            
    def eliminate_unhelpful_tracks(self,min_energy,min_danceability):
        with open(self.__filename,'r',encoding = "utf-8") as first_file, open ('../resources/goodtracks.csv','w',encoding = "utf-8") as output:
            csv_file = csv.DictReader(first_file)
            first_row = next(csv_file)
            w = csv.DictWriter(output,first_row.keys())
            w.writeheader()
            for row in csv_file:
                if ((float(row['danceability'])>=min_danceability) and (float(row['energy'])>=min_energy)):
                        w.writerow(row)
                    
        print("Done!")
            