# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:38:28 2021

@author: Vlad
"""
from repository.setlist_repository import SetlistRepository
from repository.song_repository import SongRepository
from service.song_service import SongService
from service.setlist_service import SetlistService
from utils.utils import Utils
from domain.setlist import Setlist


setlist_repo = SetlistRepository()
setlist_service = SetlistService(setlist_repo)
song_repo = SongRepository()
song_service = SongService(song_repo)
scores_array=[]


def populate_database_with_setlists_script():
    
    utils = Utils('https://www.mixesdb.com/w/MixesDB:Hottest_mixes',setlist_service)
    utils.start_script(9)
    #artist,date,tracks = utils.access_setlist_link("https://www.mixesdb.com/w/1995-11-18_-_Daft_Punk_@_Le_Priv%C3%A9,_Avignon,_France")
    #print(artist,date,tracks)
    #print(utils.get_unknown_tracks_count(tracks))
    
def test_database():
    #setlist_test = Setlist("2021-01-18","TestDJ",["Song1","Song2","Song3"])
    #print(setlist_service.add(setlist_test))
    setlists = setlist_service.getAll()
    for setlist in setlists:
        print(setlist)
    print(len(setlists))
    
def build_unknown_songs_plot():
    from utils.plotting import Plotting
    plotting = Plotting()
    full_array = plotting.plot_missing_tracks_locations()
    f = open("utils/xvalues.txt","w",encoding="utf-8")
    for value,song in full_array:
        f.write(str(value) + " -|||- " + song + "\n")
    f.close()
    
    
def plot_setlist(setlist):
    from utils.plotting import Plotting
    from utils.spotify_engine import SpotifyEngine
    import numpy as np
    plotting = Plotting()    
    spotify_engine = SpotifyEngine()
    danceability=[]
    valence=[]
    energy=[]
    tempo=[]
    
    
    for song in setlist.get_songs():
        features = spotify_engine.get_song_features(song)
        try:
            danceability.append(features['danceability'])
            valence.append(features['valence'])
            energy.append(features['energy'])
            tempo.append(features['tempo'])
        except:
            danceability.append(np.nan)
            valence.append(np.nan)
            energy.append(np.nan)
            tempo.append(np.nan)
    
    xvalues = [x*(1/len(setlist.get_songs())) for x,val in enumerate(setlist.get_songs())]
        
    #plotting.plot_setlist_features_trend('Danceability',danceability, xvalues)
    #plotting.plot_setlist_features_trend('Valence',valence, xvalues)
    plotting.plot_setlist_features_trend('Energy',energy, xvalues)
    #plotting.plot_setlist_features_trend('Tempo',tempo, xvalues)
    #plotting.plot_lagrange('Energy',energy, xvalues)
    return danceability,valence,energy,tempo
    

def populate_database_with_songs():
    from utils.spotify_engine import SpotifyEngine
    spotify_engine = SpotifyEngine()
    setlist_array = setlist_service.getAll()
    spotify_engine.start_engine(setlist_array, song_service)
    
def plot_setlist_by_attribute(setlist_id,desired_attribute):
    from utils.plotting import Plotting
    plotting = Plotting()
    title = setlist_service.getOne(setlist_id).get_dj() 
    songs = sorted(song_service.getAllSongsForSetlistId(setlist_id),key=lambda x: x.pos_in_setlist,reverse=False)
    plotting.simple_plot_setlist_trend(songs, desired_attribute,title)
    plotting.poly_plot_setlist_trend(songs,desired_attribute,title)
    plotting.poly1d_plot_setlist_trend(songs,desired_attribute,title)
    plotting.spline_plot_setlist_trend(songs, desired_attribute,title)
    plotting.oned_inter_plot_setlist_trend(songs,desired_attribute,title)
    
def plot_median_function(starting_id,final_id,desired_attribute):
    from utils.plotting import Plotting
    import numpy as np
    plotting = Plotting()
    title = 'Median Function'
    pols = []
    first_x = 1
    last_x = 0
    for i in range(starting_id,final_id):      
        songs = sorted(song_service.getAllSongsForSetlistId(i),key=lambda x: x.pos_in_setlist,reverse=False)
        aux,aux_first_x,aux_last_x = plotting.get_lq_poly_function(songs, desired_attribute)
        if aux_first_x < first_x : first_x = aux_first_x 
        if aux_last_x > last_x : last_x = aux_last_x
        pols.append(aux)
    median_pol = np.poly1d([0])    
    median_pol = plotting.get_median_function(pols)
    plotting.plot_function(median_pol,title,first_x,last_x)
    
    
def plot_median_interpolation(starting_id,final_id,desired_attribute):
    from utils.plotting import Plotting
    import numpy as np
    plotting = Plotting()
    title = 'Median Function for ' + desired_attribute
    functions = []
    first_x = 1
    last_x = 0
    for i in range(starting_id,final_id):      
        songs = sorted(song_service.getAllSongsForSetlistId(i),key=lambda x: x.pos_in_setlist,reverse=False)
        aux,aux_first_x,aux_last_x = plotting.get_1d_interpolation(songs, desired_attribute)
        if aux!=None:
            if aux_first_x < first_x : first_x = aux_first_x 
            if aux_last_x > last_x : last_x = aux_last_x
            functions.append(aux)
    print(len(functions))
    return plotting.matrix_mean_calculation(functions, first_x, last_x,title)



def set_valence_values(service):
    from utils.spotify_engine import SpotifyEngine
    spotify = SpotifyEngine()
    spotify.assign_valence_to_song(service)

def write_song_name_to_csv():
    from csv import writer
    from csv import reader
    from utils.spotify_engine import SpotifyEngine
    spotify_engine = SpotifyEngine()

    with open("D:/Programming/Licenta/resources/edmtracks.csv", 'r',encoding="utf-8") as read_obj, \
         open("D:/Programming/Licenta/resources/edmtrackstest.csv", 'w', newline='',encoding="utf-8") as write_obj:
    # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        a = 0
    # Read each row of the input csv file as list13
        for row in csv_reader:
        # Append the default text in the row / list
           if a == 0 :
               row.append("full_string")
           else:
               row.append(spotify_engine.get_song_name_for_id(row[13]))
           a = 1    
        # Add the updated row / list to the output file
           csv_writer.writerow(row)


def generate_setlist(nrGens,popLength,setSize,genres):
    from utils.plotting import Plotting
    from utils.csvreader import CSVReader
    from GA.geneticalgorithm import GeneticAlgorithm
    from scipy.interpolate import interp1d
    import numpy as np

    x_all = np.linspace(0.1,0.9,100)
    csvreader = CSVReader("resources/edmtracks.csv",genres)
    
    
    fd = open("resources/danceability100.txt")
    yd = np.array(fd.read().split())
    dance_diff = float(max(yd)) - float(min(yd))
    print(dance_diff)
    fd.close()
    
    fe = open("resources/energy100.txt")
    ye = np.array(fe.read().split())
    energy_diff = float(max(ye)) - float(min(ye))
    print(energy_diff)
    fe.close()
    
    fv = open("resources/valence100.txt")
    yv = np.array(fv.read().split())
    valence_diff = float(max(yv)) - float(min(yv))
    print(valence_diff)
    fv.close()
    
       
    dance_f = interp1d(x_all,yd)
    energy_f = interp1d(x_all,ye)
    valence_f = interp1d(x_all,yv)
    
    
    ga = GeneticAlgorithm(setSize, nrGens, popLength, csvreader, energy_f, dance_f, valence_f,
                          dance_diff,energy_diff,valence_diff)
    
    best_setlist = ga.evolution()
    
    
    output = []
    for song in best_setlist.get_repres():
   #     print(song['artists'].replace("[","").replace("]","").replace("'","") + " - " + song['name'])
   #      print(spotify_engine.get_song_name_for_id(song['id']))
        output.append(song['full_string'])  
    
    plotting = Plotting()
    
    xenergy,yenergy,yenergyorg = plotting.plot_chromosome(best_setlist, 'energy', energy_f)
    xdance,ydance,ydanceorg =  plotting.plot_chromosome(best_setlist, 'danceability', dance_f)
    xvalence,yvalence,yvalenceorg = plotting.plot_chromosome(best_setlist, 'valence', valence_f)

    
    return output,xenergy,yenergy,yenergyorg,xdance,ydance,ydanceorg,xvalence,yvalence,yvalenceorg



#for i in range(2030,2040):       
#    plot_setlist_by_attribute(i,'energy')
#plot_median_interpolation(2031,2846,'energy')

#set_valence_values(song_service)

#plot_setlist_by_attribute(2130, 'energy')
    
#utils =  Utils('https://www.mixesdb.com/w/MixesDB:Hottest_mixes',setlist_service)
#artist,date,tracks = utils.access_setlist_link('https://www.mixesdb.com/w/2015-01-02_-_Floating_Points_%26_Four_Tet_@_Plastic_People_Closing_Party,_London')
#fpoints_setlist = Setlist(date,artist,tracks)
#for s in setlist_service.getAll():
#danceability,valence,energy,tempo = plot_setlist(setlist_service.getOne(2035)) 
        
#test_database()
#setlist_test = Setlist("2021","TestDJ",["Song1","Song2","Song3"])
#setlist_service.add(setlist_test)

#populate_database_with_setlists_script()
#742867534588197850963075164817396800

#for song in setlist_service.getOne(2630).get_year():
#    print(song)
#print(' Daft Punk - '.split()[-1])

#build_unknown_songs_plot()

