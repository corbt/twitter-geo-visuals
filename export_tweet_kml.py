import os, sys, json
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

files = sorted([f for f in os.listdir("raw") if f.endswith(".json")])
tweetfile = open(os.path.join("raw",files[-1]))

kml = KML.kml(KML.Document(KML.Style(KML.LabelStyle(KML.scale(6)), id="big_label")))

print "Preparing for export"
for tweet in tweetfile:
    tweet = json.loads(tweet)
    coords = tweet['coordinates']['coordinates']

    kml.Document.append(
        KML.Placemark(
            KML.name(tweet["user"]["screen_name"]),
            KML.Point(
                KML.coordinates('{0},{1},0'.format(coords[0],coords[1])))))

with open('/media/sf_virtual_share/raw_tweets.kml', 'w') as f:
    f.write(etree.tostring(etree.ElementTree(kml),pretty_print=True))
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