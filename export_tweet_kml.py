import os, sys, json
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

files = sorted([f for f in os.listdir("raw") if f.endswith(".json")])
tweetfile = open(os.path.join("raw",files[-1]))

kml = KML.kml(KML.Document(KML.Style(KML.LabelStyle(KML.scale(6)), id="big_label")))

count = 0
print "Preparing for export"
for tweet in tweetfile:
    try:
        tweet = json.loads(tweet)
        coords = tweet['coordinates']['coordinates']

        kml.Document.append(
            KML.Placemark(
                KML.name(tweet["user"]["screen_name"]),
                KML.Point(
                    KML.coordinates('{0},{1},0'.format(coords[0],coords[1])))))
        count += 1

    except Exception:
        pass
        # print "error processing tweet "+tweet

with open('/media/sf_virtual_share/raw_tweets.kml', 'w') as f:
    f.write(etree.tostring(etree.ElementTree(kml),pretty_print=True))

print "{0} tweets processed".format(count)