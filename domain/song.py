# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:10:48 2021

@author: Vlad
"""


from domain.setlist import base
from dbinit import db
from sqlalchemy import Column, String,Integer,Float,ForeignKey

class Song(base):
    __tablename__ = 'song'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    setlist_id = Column('setlist_id',Integer,ForeignKey('setlist.id')) #setlist fkey
    full_string = Column('full_string',String)
    search_string = Column('search_string',String)
    artist = Column('artist',String)
    name = Column('name',String)
    pos_in_setlist=Column('pos_in_setlist',Integer)
    setlist_length=Column('setlist_length',Integer)
    relative_position=Column('relative_position',Float)
    acousticness=Column('acousticness',Float)
    danceability=Column('danceability',Float)
    duration_ms=Column('duration_ms',Integer)
    energy=Column('energy',Float)
    instrumentalness=Column('instrumentalness',Float)
    key=Column('key',Integer)
    tempo=Column('tempo',Float)
    liveness=Column('liveness',Float)
    loudness=Column('loudness',Float)
    valence=Column('valence',Float)
    
    def __init__(self,setlist_id,full_string,search_string,artist,name,
                 pos_in_setlist,setlist_length,relative_position,acousticness,
                 danceability,duration_ms,energy,instrumentalness,key,tempo,
                 liveness,loudness):
       
        self.setlist_id = setlist_id
        self.full_string = full_string
        self.search_string = search_string
        self.artist = artist
        self.name = name
        self.pos_in_setlist = pos_in_setlist
        self.setlist_length = setlist_length
        self.relative_position = relative_position
        self.acousticness = acousticness
        self.danceability = danceability
        self.duration_ms = duration_ms
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.key = key
        self.tempo = tempo
        self.liveness = liveness
        self.loudness = loudness
        
        
    def get(self,attrname):
        return getattr(self,attrname)
    
    def get_id(self):
        return self.id
    
    def set_id(self,id):
        self.id = id
    
    def set_valence(self,val):
        self.valence = val
        
    def __str__(self):
        return (str(self.pos_in_setlist) + " | " + str(self.artist) + " | " + str(self.name))
    
    
    
    
    