# Gets N randomly-selected lines without replacement from the input file and saves them to the output file

import os, random, json

in_file = "raw/2013-11-27-05.11.56.569021.json"
out_file = "processed/24h_5k.json"
num_selected = 5000

lines_with_location = []
with open(in_file) as f:
    for i,line in enumerate(f):
        tweet = json.loads(line)
        if tweet['user'] and tweet['user']['location'] and len(tweet['user']['location']) > 0:
            lines_with_location.append(i)

random.shuffle(lines_with_location)

print "{0} entries with location discovered".format(len(lines_with_location))

lines_selected = set(lines_with_location[0:num_selected])

with open(in_file) as i_f:
    with open(out_file, 'w') as o_f:
        for i,line in enumerate(i_f):
            if i in lines_selected:
                o_f.write(line)