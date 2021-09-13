# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:03:47 2021

@author: Vlad
"""


class SongService:
    def __init__(self, __repo):
        self.__repo = __repo


    def add(self, song):
        songfound = self.__repo.getOne(song.get_id())
        if (songfound != None):
            raise ValueError("A song with given ID already exists.")
        return self.__repo.add(song)


    def getAll(self):
        songs = self.__repo.getAll()
        return songs

    def getAllSongsForSetlistId(self,setlistid):
        songs = self.__repo.getAllSongsForSetlistId(setlistid)
        return songs
    
    def getOne(self, id):
        song = self.__repo.getOne(id)
        if (song == None):
            raise ValueError("Song with given id does not exist.")
        return song
    
    def update(self,song):
        songverify = self.__repo.getOne(song.id)
        if (songverify == None):
            raise ValueError("Song with given id does not exist.")
        self.__repo.update(song)
        
    def remove(self, id):
        song = self.__repo.getOne(id)
        if (song == None):
            raise ValueError("Song with given id does not exist.")
        self.__repo.remove(song)
        
    def getAllFromId(self,songid):
        songs = self.__repo.getAllFromId(songid)
        return songs