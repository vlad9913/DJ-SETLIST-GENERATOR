# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:43:28 2021

@author: Vlad
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



class SpotifyEngine:
    def __init__(self):
        self.__spotify = spotipy.Spotify(client_credentials_manager=
                          SpotifyClientCredentials
                          ("",
                           ""))
        
    def search_song(self,song_text):
        #encoded_text = urllib.parse.quote(song_text,safe="")
        #print(encoded_text)
        if not (len(song_text.split('-'))>1): #Verify song integrity (artist - name)
            return None
        song_text = song_text.replace('- ','')
        try:
            out = self.__spotify.search(song_text,type="track")['tracks']['items'][0]['id']
        except:
            return None
            print("Didn't find "+ song_text)
        return out
    
    def get_song_features(self,song_text):
        try:
            rezultat = self.__spotify.audio_features(self.search_song(song_text))[0]
        except TypeError:
            return None
        return rezultat                     
    
    def assign_song_object_features(self,setlist,service):
        from domain.song import Song
        songs = setlist.get_songs()
        print(str(setlist.get_date()) + " | " + setlist.get_dj() + " | " + str(setlist.get_id()))
        for index,song_full_string in enumerate(songs):
            splitted = song_full_string.split(' - ')
            artist = splitted[0]
            name = ' '.join(splitted[1:])
            search_string = song_full_string.replace('- ','')
            
            features = self.get_song_features(song_full_string)
        
            try:
                s = Song(setlist.get_id(),song_full_string,search_string,artist,
                         name,index,len(songs),index*(1/len(songs)),features['acousticness'],
                         features['danceability'],features['duration_ms'],features['energy'],
                         features['instrumentalness'],features['key'],features['tempo'],
                         features['liveness'],features['loudness'])
            except TypeError:
                s = Song(setlist.get_id(),song_full_string,search_string,artist,
                         name,index,len(songs),index*(1/len(songs)),-999,
                         -999,-999,-999,
                         -999,-999,-999,
                         -999,-999)
            service.add(s)
            print(s.full_string + " added.")
        

    def start_engine(self,setlist_array,service):
        for setlist in setlist_array:
            self.assign_song_object_features(setlist,service)

    
    def assign_valence_to_song(self,service):
        #songz = service.getAll()
        songz = service.getAllFromId(30550)
        songs = sorted(songz,key=lambda x:x.id)
        for song in songs:
            features = self.get_song_features(song.full_string)
            
            try:
                val = features['valence']
            except TypeError:
                val = -999
            song.set_valence(val)
            service.update(song)
            print(song.full_string + " valence set to " + str(val) + "||" + str(song.id))
        
        
    
    def get_song_name_for_id(self,trackid):
        try:
            rezultat = self.__spotify.track(trackid)         
            name_string = rezultat['name']
            artists_string = ""
            for idx,artist in enumerate(rezultat['artists']):
                artists_string+=artist['name']
                if idx < len(rezultat['artists'])-1:
                    artists_string+=", "
            full_string = artists_string + " - " + name_string
            
            return full_string
        except TypeError:
            return ""
        
        
        
        

        
        
        
        
        
        
        