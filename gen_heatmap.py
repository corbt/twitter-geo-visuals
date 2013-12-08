import random, json
import heatmap

input_file = "2013-11-27-05.11.56.569021"

hm = heatmap.Heatmap()
points = []

with open("raw/"+input_file+".json") as in_f:
    for line in in_f:
        tweet = json.loads(line)
        coords = tweet['coordinates']['coordinates']
        points.append(tuple(coords))


img = hm.heatmap(points, dotsize=5, opacity=255, area=((-180,-90),(180,90)))
# img.save("maps/"+input_file+".png")
hm.saveKML("maps/"+input_file+".kml")
