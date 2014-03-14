Countries Of The World
======================

Grab the csv file from: TODO

Parse it into a comfortable format and create a static website that shows info about each country:

- ```(country_code).html```: country information + distance from Israel

- ```index.html```: the list of countries, as links

Calculate distance (from [stackoverflow.com/a/15737218/57952](http://stackoverflow.com/a/15737218/57952)):

	from math import radians, cos, sin, asin, sqrt
	def haversine(lon1, lat1, lon2, lat2):
	    """
	    Calculate the great circle distance between two points 
	    on the earth (specified in decimal degrees)
	    """
	    # convert decimal degrees to radians 
	    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	    # haversine formula 
	    dlon = lon2 - lon1 
	    dlat = lat2 - lat1 
	    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	    c = 2 * asin(sqrt(a)) 
	    km = 6367 * c
	    return km