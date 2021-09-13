# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:48:57 2021

@author: Vlad
"""

class Utils:
    def __init__(self, initialUrl,service):
        self._initialUrl = initialUrl
        self.__service = service


    def get_html_of_url(self,url):     
        from urllib.request import urlopen
        from bs4 import BeautifulSoup
        
       #url = "https://www.mixesdb.com/w/MixesDB:Hottest_mixes"     
        page = urlopen(url)
        
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html,"html.parser")
        return soup,html

    
    def get_setlist_links_and_next_page(self,url):       
        soup,html = self.get_html_of_url(url)
        mixesLinks=[]
        nextPageLink=""
        for a in soup.find_all('a',href=True):
            posLink = str(a['href'])
            if (len(a.contents)>0):
                if (str(a.contents[0]) =='next 100'):
                    nextPageLink = "https:" + posLink #Next 100 page link  
            if (posLink.startswith(("/w/2","/w/1"))):
                mixesLinks.append("https://www.mixesdb.com"+posLink) #List of links of each setlist
                
        return mixesLinks,nextPageLink
    

    
    def access_setlist_link(self,url):       
        import re
        soup,html = self.get_html_of_url(url)
        print("Setlist accessed!!")
        tracks=[]
        artist=""
        date=""
        #FIND AND GET DATE
        div = soup.find("div",{"id": "mw-normal-catlinks"})
        ul = div.find("ul")
        date_li = ul.find_all("li")[0]
        date = str(date_li.text)
        
        #FIND AND GET ARTIST
        artist_li = ul.find_all("li")[1]
        artist = str(artist_li.text)
        
            
        #FIND AND GET TRACKS
        h2 = soup.find('h2',text='Tracklist')
        good_format=True;
        try:
            for sibling in h2.find_next_siblings():
                if (sibling.name == "h2"):
                    break;
                       
                for li in sibling.find_all('li'):
         
                        track = self.remove_unnecessary_characters(str(li.contents[0]))                        
                        for child_a in li.find_all('a'):
                            track= track + self.remove_unnecessary_characters(child_a.contents[0])
                        #print(track)
                        tracks.append(track)
                        
                if (len(tracks)==0):
                        for li in sibling.find_all('div',{"class":"list-track"}):
                            track = self.remove_unnecessary_characters(str(li.contents[0]))
                            #print(track)
                            tracks.append(track)


        except:
            good_format = False;
            print("Weird format for "+ url)
            print("Skipping...")   
   
                
        #print("Nr. of songs: "+str(len(tracks)))
        extra_unknown=0
        for track in tracks:
            if not (len(track.split('-'))>1):
                extra_unknown+=1
         
        count,maxcombo = self.get_unknown_tracks_count(tracks)
        #print("Nr. of unknown tracks: " + str(count))
        if (self.validate_setlist(tracks,extra_unknown)==False):
            return None,None,None
        
        return artist,date,tracks
        
    
    def validate_setlist(self,setlist,extra_unknown):
        count,maxcombo = self.get_unknown_tracks_count(setlist)
        count = count+extra_unknown
        if (len(setlist)<13):
            return False
        if (count>=len(setlist)/ 1.5):
            return False
        return True

    
    def get_unknown_tracks_count(self,setlist):
        import re
        qpattern = '[?+]'
        count=0
        combo=0
        maxcombo=0
        for t in setlist:
            if re.search(qpattern,t) is not None:
                count+=1
                combo+=1;
                if (combo>maxcombo):
                    maxcombo = combo;
            else:
                combo=0
        return count,maxcombo
        
    
    def remove_unnecessary_characters(self,input_string):
        import re
        pattern1 = r'\[.*?\]'
        pattern2 = r'\(.*?\)'
        first = re.sub(pattern1,'',input_string)
        return re.sub(pattern2,'',first)
        
        
    def lcm(self,a,b):
        from fractions import gcd
        return a*b//gcd(a,b)

    def access_pages(self,nr_of_pages):
        from domain.setlist import Setlist
        import re
        lcm=1
        total_tracks=0
        setlist_tracks_array=[]
        page=1
        mixesLinks,nextPage = self.get_setlist_links_and_next_page(self._initialUrl)
        print("We're on page ",page)
        for setlink in mixesLinks:
            current_tracks=[]
            current_artist = ""
            current_date = ""
            current_artist,current_date,current_tracks = self.access_setlist_link(setlink)
            
            if current_artist is not None:
                if re.match(r'^(19|20)\d{2}$',current_date) is None:
                    s = Setlist(0000,current_artist,current_tracks)
                else:
                    s = Setlist(current_date,current_artist,current_tracks)
                try:
                    self.__service.add(s)
                    total_tracks+=len(current_tracks)
                    print("Setlist by "+s.get_dj()+" added!") 
                    print("Total tracks: "+ str(total_tracks))   
                except:
                    print("Error!")
                         
        for i in range(nr_of_pages): #100 setlists per page
            page+=1
            print("We're on page ",page)
            mixesLinks,nextPageTemp = self.get_setlist_links_and_next_page(nextPage)
            for setlink in mixesLinks:
                current_tracks=[]
                
                current_artist = ""
                current_date = ""
               
                current_artist,current_date,current_tracks = self.access_setlist_link(setlink)
                if current_artist is not None:
                    if re.match(r'^(19|20)\d{2}$',current_date) is None:
                        s = Setlist(0000,current_artist,current_tracks)
                    else:
                        s = Setlist(current_date,current_artist,current_tracks)
                    try:
                         self.__service.add(s)
                         total_tracks+=len(current_tracks)
                         print("Setlist by "+s.get_dj()+" added!")
                         print("Total tracks: "+ str(total_tracks))  
                         
                    except:
                         print("Error!")
                         
            nextPage= nextPageTemp
        return setlist_tracks_array
    
    
    
    def plot_number_of_tracks(self,median_value,setlist_tracks_array):
        import matplotlib.pyplot as plt
        plt.plot(setlist_tracks_array)
        plt.hlines(median_value,0,len(setlist_tracks_array))
        
        
        
    def get_median_nr_of_songs(self,total_number_of_songs,setlist_tracks_array):
        return total_number_of_songs/len(setlist_tracks_array)
        
        
    
    def start_script(self,nr_of_pages):
        setlist_tracks_array = self.access_pages(nr_of_pages)
        #median_value = self.get_median_nr_of_songs(total_number_of_songs,setlist_tracks_array)
        #self.plot_number_of_tracks(median_value,setlist_tracks_array)
        
        
       

#utils = Utils('https://www.mixesdb.com/w/MixesDB:Hottest_mixes')


#utils.start_script()

#utils.access_setlist_link("https://www.mixesdb.com/w/2020-04-25_-_Jamie_xx_-_Essential_Mix")




































