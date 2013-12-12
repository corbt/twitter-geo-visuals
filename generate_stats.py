from __future__ import division
import json
from collections import defaultdict
import operator

input_file = "24h_5k_users_followers_countries"

relationships = defaultdict(int)
countries = defaultdict(int)
total_relationships = 0
international_relationships = 0

for line in open("processed/"+input_file+".json"):
    user = json.loads(line)
    countries[user['country']] += 1
    for follower in user['followers']:
        total_relationships += 1
        countries[follower['country']] += 1
        if user['country'] != follower['country']:
            relationships[user['country']+"->"+follower['country']] += 1
            international_relationships += 1


print "{0}% relationships international".format(international_relationships/total_relationships*100)

for country, count in sorted(countries.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]:
    print country.encode('utf-8')

for country, count in sorted(relationships.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]:
    print country.encode('utf-8')