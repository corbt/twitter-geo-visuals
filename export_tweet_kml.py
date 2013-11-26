import os, sys, json
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

files = sorted([f for f in os.listdir("raw") if f.endswith(".json")])
tweetfile = open(files[-1])

kml = KML.kml(KML.Document(KML.Style(KML.LabelStyle(KML.scale(6)), id="big_label")))

for tweet in tweetfile:
    tweet = json.loads(tweet)
    print tweet

# incidents = requests.get("http://corbt.com/478/sf").json()

# for incident in incidents:
#     kml.Document.append(
#         KML.Placemark(
#             # KML.name(incident['incidentId']),
#             KML.Point(
#                 KML.coordinates('{lon},{lat},0'.format(
#                     lon=incident['point']['coordinates'][1],
#                     lat=incident['point']['coordinates'][0])))))

# with open("export.kml", "w") as output:
#     output.write(etree.tostring(etree.ElementTree(kml),pretty_print=True))

# print etree.tostring(etree.ElementTree(kml),pretty_print=True)