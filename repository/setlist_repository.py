# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:00:03 2021

@author: Vlad
"""
from sqlalchemy.orm import sessionmaker
class SetlistRepository:

    def getAll(self):
        from main import db
        from domain.setlist import Setlist
        Session = sessionmaker(db)
        session = Session()

        setlists = session.query(Setlist)
        return setlists

    def getOne(self,id):
        from main import db
        from domain.setlist import Setlist
        Session = sessionmaker(db)
        session = Session()

        setlists = session.query(Setlist).get(id)
        return setlists


    def add(self, setlist):
        from main import db
        Session = sessionmaker(db)
        session = Session()
        
        session.add(setlist)
        session.commit()
        return setlist

    def remove(self, setlist):
        from main import db
        Session = sessionmaker(db)
        session = Session()
        
        session.delete(setlist)
        session.commit()