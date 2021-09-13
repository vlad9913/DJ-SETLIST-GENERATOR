# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:11:55 2021

@author: Vlad
"""

from dbinit import base
from sqlalchemy import Column, String,Integer,ARRAY 
class Setlist(base):
    __tablename__ = 'setlist'
    __table_args__ = {'extend_existing': True} 
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    date = Column('date',Integer)
    dj = Column('dj',String)
    songs = Column('songs',ARRAY(String))
    
    def __init__(self,date,dj,songs):
        self.date = date
        self.dj = dj
        self.songs = songs
       
    def get_id(self):
        return self.id
    
    def get_date(self):
        return self.date
    
    def get_dj(self):
        return self.dj
    
    def get_songs(self):
        return self.songs
    
    def set_id(self,value):
        self.id = value
        
    def set_date(self,value):
        self.date = value
        
    def set_dj(self,value):
        self.dj = value
        
    def set_songs(self,value):
        self.songs = value
        
    def __str__(self):
        return (str(self.id)+ " | " + str(self.date) + " | " + str(self.dj) 
                + " | " + str(self.songs))
        
#base.metadata.create_all(db)