#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Created on Wed Jul 22 09:02:47 2020
#author: Michael

# %% ------------------------------------------------
# import packages

import csv
import simplekml

# %% ------------------------------------------------
# create Newcastle KML
inputfile = csv.reader(open('/Users/Michael/Documents/Projects/Python_Google_map/Newcastle_locations.csv','r'))

kml=simplekml.Kml()

n = 0
for row in inputfile:
    n = n+1  
    if n< 6:
        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])        
        pnt.style.iconstyle.color = simplekml.Color.white
        pnt.style.labelstyle.scale = 1 
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/donut.png'
    if n >= 6 and n < 8:
        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])              
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.style.labelstyle.scale = 1 
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'  
    if n >= 8 and n < 16:
        a = 1
    if n >= 16:
        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])              
        pnt.style.labelstyle.scale = 2 
        pnt.style.iconstyle.color = simplekml.Color.red
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_square.png'         
        


  
#kml.save('/Users/Michael/Documents/Projects/Python_Google_map/Newcastle_assets.kml')

# %% ------------------------------------------------
# create Newcastle glider KML

inputfile = csv.reader(open('/Users/Michael/Documents/Projects/Python_Google_map/glider_tracks_2020_0101-0107.csv','r'))

#kml=simplekml.Kml()
n = 0
for row in inputfile:
    n = n+1      
    if n % 1000 == 0:
        pnt = kml.newpoint(name='', coords=[(row[1],row[0])])    
        pnt.style.labelstyle.color = simplekml.Color.coral
        pnt.style.labelstyle.scale = 1 
        pnt.style.iconstyle.scale = 0.5
        pnt.style.iconstyle.color = simplekml.Color.coral
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'    
    
  
#kml.save('/Users/Michael/Documents/Projects/Python_Google_map/Glider_tracks.kml')    

kml.save('/Users/Michael/Documents/Projects/Python_Google_map/Newcastle_assets.kml')