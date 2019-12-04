# import gmplot package
import gmplot
import csv
from math import sin, cos, sqrt, atan2, radians
R = 6373.0



park_x = []
park_y = []
container_x = []
container_y = []
lat=[]
lat1=[]
lat2=[]
lat3=[]
long=[]
long1=[]
long2=[]
long3=[]
par_lat=[]
park_long=[]


with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Park_o.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       park_long.append(float(row[0]))
       park_y.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Park_L.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       par_lat.append(float(row[0]))
       park_x.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Latitude_12.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       lat.append(float(row[0]))
       container_x.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Longitude_12.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       long.append(float(row[0]))
       container_y.append(float(row[0]))

with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Latitude_13.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       lat1.append(float(row[0]))
       container_x.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Longitude_13.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       long1.append(float(row[0]))
       container_y.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Latitude_14.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       lat2.append(float(row[0]))
       container_x.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Longitude_14.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       long2.append(float(row[0]))
       container_y.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Latitude_15.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       lat3.append(float(row[0]))
       container_x.append(float(row[0]))
with open('C:\\Users\Shashi Suman\Desktop\Data Analytics\Longitude_15.csv','rt') as l:
    data=csv.reader(l)
    for row in data:
       long3.append(float(row[0]))
       container_y.append(float(row[0]))


gmp = gmplot.GoogleMapPlotter(44.2312,-76.4860, 13)


park_away_x = []
park_away_y = []

for i in range(len(park_x)):
   count = 0
   for j in range(len(container_x)):
      lat_1 = radians(float(park_x[i]))
      lon_1 = radians(float(park_y[i]))
      lat_2 = radians(float(container_x[j]))
      lon_2 = radians(float(container_y[j]))

      dlon = lon_2 - lon_1
      dlat = lat_2 - lat_1

      a = sin(dlat / 2)**2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2)**2
      c = 2 * atan2(sqrt(a), sqrt(1 - a))
      distance = R*c
      if(distance>=1):
         count += 1
   if(count==len(container_x)):
      park_away_x.append(park_x[i])
      park_away_y.append(park_y[i])
      count = 0
# scatter method of map object
# scatter points on the google map
gmp.scatter(lat, long, '# FF0000',size=40, marker=False)
gmp.scatter(lat1, long1, '# 0F0000',size=40, marker=False)
gmp.scatter(lat2, long2, '# AF0450',size=40, marker=False)
gmp.scatter(lat3, long3, '# BE1050',size=40, marker=False)
gmp.scatter(par_lat, park_long, 'pink',size=80, marker=False)
gmp.scatter(park_away_x, park_away_y, 'blue', size=150, marker=False)
#gmp.apikey='AIzaSyDKk5l3CWWil7QKSmO5n4eD7xLvywmAr8E'

# Plot method Draw a line in
# between given coordinates

gmp.plot(lat, long,'orange', edge_width=2.5)
gmp.plot(lat1, long1,'red', edge_width=2.5)
gmp.plot(lat2, long2,'blue', edge_width=2.5)
gmp.plot(lat3, long3,'yellow', edge_width=2.5)


gmp.draw("C:\\Users\Shashi Suman\Desktop\Data Analytics\Kingston - Google Maps14-17_park.html")
