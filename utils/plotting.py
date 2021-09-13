# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:22:02 2021

@author: Vlad
"""


class Plotting:
    def __init__(self):
        pass
  
    def plot_missing_tracks_locations(self):
        from service.setlist_service import SetlistService
        from repository.setlist_repository import SetlistRepository
        import matplotlib.pyplot as plt
        import matplotlib
        import numpy as np 
        import re
        setlist_repo = SetlistRepository()
        setlist_service = SetlistService(setlist_repo)
        
        #labels = ['Start','End']
        setlists = setlist_service.getAll()
        #x_boundary=np.array([0,1])
        #y_boundary=np.array([1,1])
        #plt.scatter(x_boundary,y_boundary,color='hotpink')
        #for i,txt in enumerate(labels):
        #plt.annotate(txt,(x_boundary[i],y_boundary[i]))
        
        
        good_songs = []
        unknown_songs = []
        full_array=[]
        i=0;
        for setlist in setlists:
            i+=1;
            songs = setlist.get_songs()
            
            songs_len = len(songs)
            
            step = 1/songs_len
            
            for index,song in enumerate(songs):
                splitted = song.split('-')
                
                if (len(splitted)==1):
                    unknown_songs.append(index*step)
                    full_array.append([index*step,"?"])
                elif (splitted[-1].isspace()):
                    unknown_songs.append(index*step)
                    full_array.append([index*step,"?"])
                else:
                    good_songs.append(index*step)
                    full_array.append([index*step,song])

        #x_good = np.array(good_songs)
        #x_bad = np.array(unknown_songs)
        #y_good = np.array([1]*len(good_songs))
        #y_bad = np.array([1]*len(unknown_songs))
        #plt.scatter(x_good,y_good,color='green')
        #plt.scatter(x_bad,y_bad,color='red') 
        
        
        full_array.sort()
        
            
        return full_array
            
        #plt.show()

        
    def plot_setlist_features_trend(self,name,features,xvalues):
        #features - dictionary
        #xvalues - array of xvalues
        import matplotlib.pyplot as plt
        import numpy as np 
        x = np.array(xvalues)
        y = np.array(features)
        plt.grid()
        plt.plot(x,y)
                
    def plot_poly(self,name,features,xvalues):
        import matplotlib.pyplot as plt
        import numpy as np 
        x=[]
        y=[]        
        for index,val in enumerate(features):
            if not (np.isnan(val)):
                x.append(xvalues[index])    
                y.append(features[index])
        x_np = np.array(x)
        y_np = np.array(y)
        
        pol = np.polyfit(x_np,y_np,len(x_np)-1)
        #xx = np.linspace(min(x_np),max(x_np))
        yy=np.polyval(pol,x_np)
        plt.plot(x_np, yy, '-',x_np, y_np, 'ro')
        plt.show()

    '''
    Method that plots a set of songs ordered by their 
    original setlist positions by the desired attribute.
    
    input: songs = array of Song objects, desired_attribute = String
    
    output: plot
    '''
    def simple_plot_setlist_trend(self,songs,desired_attribute,title):
        import matplotlib.pyplot as plt
        import numpy as np
        unknown_songs = 0
        attrs=[]
        for x in songs:
            if x.get(desired_attribute)!=-999:
                attrs.append(x.get(desired_attribute))
            else:
                attrs.append(np.nan)
                unknown_songs += 1
        y_vals = np.array(attrs)
        x_vals = np.array([y.relative_position for y in songs])
        plt.grid()
        plt.plot(x_vals,y_vals,'ro')
        title = title + " T:" + str(songs[0].setlist_length) + " U:" + str(unknown_songs)
        plt.title(title)
        plt.show()           
    
    
    def get_lq_poly_function(self,songs,desired_attribute):
        import numpy as np
        x,y,unknown_songs=self.remove_nan_values(songs,desired_attribute)
                               
        y_vals = np.array(y)
        x_vals = np.array(x)
        pol = np.polyfit(x_vals,y_vals,len(x_vals)-1)
        return pol,x[0],x[len(x)-1]
        
    def get_median_function(self,pols):
        import numpy as np
        median = np.poly1d([0])
        for pol in pols:
            pol_obj = np.poly1d(pol)
            median = np.polyadd(median,pol_obj)
        print( median)
        median  = median/len(pols)
        print("AFTER DIVISION")
        print( median)
        return median 
    
    
    def plot_function(self,pol,title,first_x,last_x):
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(first_x,last_x,100) 
        print(first_x,last_x)
        #y = np.polyval(pol,x)
        y =pol(x) 
        plt.plot(x,y,'-')
        
        #plt.plot(x,pol,'-')
        
        plt.title(title)
        plt.show()
        
        
    def poly_plot_setlist_trend(self,songs,desired_attribute,title):
        import matplotlib.pyplot as plt
        import numpy as np
        import numpy.polynomial.polynomial as poly
        x,y,unknown_songs=self.remove_nan_values(songs,desired_attribute)
        y_vals = np.array(y)
        x_vals = np.array(x)
        pol = np.polyfit(x_vals,y_vals,len(x_vals)-1)
        yy = np.polyval(pol,x_vals)
        
        plt.plot(x_vals, yy, '-',x_vals, y_vals, 'ro')
        title = title + " T:" + str(songs[0].setlist_length) + " U:" + str(unknown_songs)
        plt.title(title)
        plt.show()
        
        
    def poly1d_plot_setlist_trend(self,songs,desired_attribute,title):
        import matplotlib.pyplot as plt
        import numpy as np
        from scipy import interpolate
        x,y,unknown_songs=self.remove_nan_values(songs,desired_attribute)
                
        x_vals = np.array(x)
        y_vals = np.array(y)
     
        
        pol = np.polyfit(x_vals,y_vals,len(x_vals)-1)
        
        plt.scatter(x_vals,y_vals)   
        
        yy = np.poly1d(pol)
        
        xx = np.linspace(x[0],x[len(x)-1],100)
     
    
        
        plt.plot(xx,yy(xx))
        title = title + " T:" + str(songs[0].setlist_length) + " U:" + str(unknown_songs)
        plt.title(title)
        plt.show()
        
        
    def spline_plot_setlist_trend(self,songs,desired_attribute,title):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import interpolate
        x,y,unknown_songs=self.remove_nan_values(songs,desired_attribute)
        x_vals = np.array(x)
        y_vals = np.array(y)
        tck = interpolate.splrep(x_vals,y_vals)
        xnew = np.linspace(x[0],x[len(x)-1],100)
        ynew = interpolate.splev(xnew,tck)
        
        plt.plot(x,y,'x',xnew,ynew)
        title = title + " T:" + str(songs[0].setlist_length) + " U:" + str(unknown_songs)
        plt.title(title)
        plt.show()
   
    
    def oned_inter_plot_setlist_trend(self,songs,desired_attribute,title):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.interpolate import interp1d
        x,y,unknown_songs=self.remove_nan_values(songs,desired_attribute)
        x_vals = np.array(x)
        y_vals = np.array(y)
        
        f = interp1d(x_vals,y_vals,kind='cubic')
        xnew = np.linspace(x_vals[0],x_vals[len(x)-1],100)
        

        plt.plot(x,y,'x',xnew,f(xnew))
        title = title + " T:" + str(songs[0].setlist_length) + " U:" + str(unknown_songs)
        plt.title(title)
        plt.show()
    
    
    def get_1d_interpolation(self,songs,desired_attribute):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.interpolate import interp1d
        x,y,unknown_songs=self.remove_nan_values(songs,desired_attribute)
        x_vals = np.array(x)
        y_vals = np.array(y)
        try:
            f = interp1d(x_vals,y_vals,kind='cubic')
            #print(f)
            return f,x_vals[0],x_vals[len(x)-1]
        except ValueError:
            return None,None,None
    
    def matrix_mean_calculation(self,functions,first_x,last_x,title):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.interpolate import interp1d
        from scipy.integrate import quad
        x_all = np.linspace(0,0.99,100)
        f_all =[]
        for f in functions:
            this_f=[]
            for x in x_all:
                try:
                    this_f.append(f(x))
                except ValueError:
                    this_f.append(0)
            f_all.append(np.array(this_f))
        
        
        #f_all = [f(x_all) for f in functions]
        data_collection = np.vstack(f_all)
        
        f_avg = np.average(data_collection,axis=0,weights=data_collection.astype(bool))
        f = interp1d(x_all,f_avg,kind='cubic')
        print(f_avg)
        #plt.plot(x_all,f_avg)     
        plt.plot(x_all,f(x_all))

        plt.title(title)
        plt.show()
        y_count = []
        for i in range(0,100):
            this_column_count = 0
            for j in range(0,809):
                if data_collection[j][i] != 0 :
                    this_column_count+=1
            y_count.append(this_column_count)
                
        
        plt.hist(x=x_all,bins = 100,weights=y_count,rwidth = .5)
        plt.show()
        
        
        return f
    
    def plot_chromosome(self,chromosome,desired_attribute,function):
        import numpy as np
       # import matplotlib.pyplot as plt
       
        from scipy.interpolate import interp1d
        
        y_vals=[]
        
        for song in chromosome.get_repres():
            y_vals.append(song[desired_attribute])
        
        y = np.array(y_vals)
        x = np.array([0.1+index*(0.8/chromosome.get_length()) for index,song in enumerate(chromosome.get_repres())])
        
        f = interp1d(x,y,kind='cubic')
    
        '''
        plt.plot(x,f(x),'r')
        plt.title('Generated setlist '+ desired_attribute)
        plt.show()
        plt.plot(x,function(x))
        plt.title('Original '+ desired_attribute)
        plt.show()
        '''
        return x,f(x),function(x)
        
        
        
    def remove_nan_values(self,songs,desired_attribute):
        import numpy as np
        import matplotlib.pyplot as plt
        unknown_songs = 0
        attrs=[]
        for x in songs:
            if x.get(desired_attribute)!=-999:
                attrs.append(x.get(desired_attribute))
            else:
                attrs.append(np.nan)
                unknown_songs += 1
        xvalues = [x.relative_position for x in songs]
        x=[]
        y=[]        
        for index,val in enumerate(attrs):
            if not (np.isnan(val)):
                x.append(xvalues[index])    
                y.append(attrs[index])
        return x,y,unknown_songs
        

        
            
            
            
            
    