# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:00:12 2021

@author: Vlad
"""


class SetlistService:
    def __init__(self, __repo):
        self.__repo = __repo


    def add(self, setlist):
        setlistfound = self.__repo.getOne(setlist.get_id())
        if (setlistfound != None):
            raise ValueError("A setlist with given ID already exists.")
        return self.__repo.add(setlist)


    def getAll(self):
        setlists = self.__repo.getAll()
        return setlists


    def getOne(self, id):
        setlist = self.__repo.getOne(id)
        if (setlist == None):
            raise ValueError("Setlist with given id does not exist.")
        return setlist


    def remove(self, id):
        setlist = self.__repo.getOne(id)
        if (setlist == None):
            raise ValueError("Setlist with given id does not exist.")
        self.__repo.remove(setlist)