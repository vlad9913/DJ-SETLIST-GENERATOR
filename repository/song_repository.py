# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:01:51 2021

@author: Vlad
"""
from sqlalchemy.orm import sessionmaker
class SongRepository:

    def getAll(self):
        from main import db
        from domain.song import Song
        Session = sessionmaker(db)
        session = Session()

        songs = session.query(Song)
        return songs
    
    def getAllFromId(self,songid):
        from main import db
        from domain.song import Song
        Session = sessionmaker(db)
        session = Session()
        songs = session.query(Song).filter(Song.id>songid).all()
        return songs

    def getOne(self,id):
        from main import db
        from domain.song import Song
        Session = sessionmaker(db)
        session = Session()
        songs = session.query(Song).get(id)
        return songs

    def getAllSongsForSetlistId(self,setlistid):
        from main import db
        from domain.song import Song
        Session = sessionmaker(db)
        session = Session()
        songs = session.query(Song).filter(Song.setlist_id==setlistid).all()
        return songs
    
    def add(self, song):
        from main import db
        Session = sessionmaker(db)
        session = Session()
        
        session.add(song)
        session.commit()
        return song
    
    def update(self,song):
        from main import db
        from domain.song import Song
        Session = sessionmaker(db)
        session = Session()
        searchedid = song.get_id()
        session.query(Song).filter_by(id=searchedid).update({"valence":song.valence})
        session.commit()

    def remove(self, song):
        from main import db
        Session = sessionmaker(db)
        session = Session()
        
        session.delete(song)
        session.commit()