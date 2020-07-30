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
inputfile = csv.reader(open('/Users/Michael/Documents/Projects/Python_Google_map/IMOS_assets_map_creator/Newcastle_locations.csv','r'))

kml=simplekml.Kml()

n = 0
for row in inputfile:
    n = n+1  
    if n< 6:
        # ATF moorings
        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])        
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.style.labelstyle.scale = 1 
        pnt.iconstyle.scale = 0.5
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/donut.png'
    if n >= 6 and n < 8:
        # HF radar sites
        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])              
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.style.labelstyle.scale = 1 
        pnt.iconstyle.scale = 0.5        
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'  
    if n >= 8 and n < 16:
        a = 1
        # HF radar field
        #        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])              
        #        pnt.style.iconstyle.color = simplekml.Color.black
        #        pnt.style.labelstyle.scale = 1 
        #        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'  
    if n >= 16 and n < 19:
        # Proposed Newcastle moorings
        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])              
        pnt.style.labelstyle.scale = 1.5 
        pnt.style.labelstyle.color = simplekml.Color.white
        pnt.iconstyle.scale = 1       
        pnt.style.iconstyle.color = simplekml.Color.red
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_square.png'         
    if n >= 19 and n < 21: 
        # Proposed Sydney HF Radar sites
        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])   
        pnt.style.labelstyle.scale = 1.5 
        pnt.style.labelstyle.color = simplekml.Color.white          
        pnt.style.iconstyle.color = simplekml.Color.red
        pnt.iconstyle.scale = 1        
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'  
    if n >= 21 and n < 30:
        a = 1
        # Proposed Sydney HF radar field
        #        pnt = kml.newpoint(name=row[0], coords=[(row[2],row[1])])              
        #        pnt.style.iconstyle.color = simplekml.Color.black
        #        pnt.style.labelstyle.scale = 1 
        #        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'  
    if n >= 30 and n < 32:        
        # Coffs Harbour radar sites
        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])              
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.style.labelstyle.scale = 1 
        pnt.iconstyle.scale = 0.5        
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'          
    if n >= 32 and n < 39:
        a = 1
        # Coffs Harbour HF radar field
        #        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])              
        #        pnt.style.iconstyle.color = simplekml.Color.black
        #        pnt.style.labelstyle.scale = 1 
        #        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/target.png'          
    if n >= 40 and n < 49:
        # Other NSW Moorings
        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])              
        pnt.style.labelstyle.scale = 2 
        pnt.iconstyle.scale = 0.5        
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_square.png'     
    if n >= 49 and n < 52:
        # Other NSW Moorings
        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])              
        pnt.style.labelstyle.scale = 2 
        pnt.iconstyle.scale = 0.5        
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png' 
    if n >= 52 and n < 94:
        # ATF moorings
        pnt = kml.newpoint(name='', coords=[(row[2],row[1])])        
        pnt.style.iconstyle.color = simplekml.Color.green
        pnt.iconstyle.scale = 0.5        
        pnt.style.labelstyle.scale = 1 
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/donut.png'
          

  
#kml.save('/Users/Michael/Documents/Projects/Python_Google_map/Newcastle_assets.kml')

# %% ------------------------------------------------
# create Newcastle glider KML

#inputfile = csv.reader(open('/Users/Michael/Documents/Projects/Python_Google_map/IMOS_assets_map_creator/glider_tracks_2020_0101-0107.csv','r'))
#
##kml=simplekml.Kml()
#n = 0
#for row in inputfile:
#    n = n+1      
#    pnt = kml.newpoint(name='', coords=[(row[0],row[1])])    
#    pnt.style.labelstyle.color = simplekml.Color.gray
#    pnt.style.labelstyle.scale = 1 
#    pnt.style.iconstyle.scale = 0.2
#    pnt.style.iconstyle.color = simplekml.Color.greenyellow
#    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'    
    
#kml.save('/Users/Michael/Documents/Projects/Python_Google_map/Glider_tracks.kml')    

kml.save('/Users/Michael/Documents/Projects/Python_Google_map/IMOS_assets_map_creator/Newcastle_assets.kml')