import os, json

input_file = '24h_5k'

with open('processed/'+input_file+'.json') as in_file:
    data = json.loads(in_file.readline())
    print json.dumps(data, indent=2)

with open('processed/'+input_file+'.json') as in_file:
    with open('processed/'+input_file+'_users.json', 'w') as out_file:
        for index,line in enumerate(in_file):
            try:
                tweet = json.loads(line)
                out_file.write(json.dumps(tweet['user'])+'\n')
            except Exception:
                print "Tweet {0} failed to parse".format(index)

