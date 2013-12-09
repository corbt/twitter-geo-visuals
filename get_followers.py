import tweepy, json, time
import os

input_file = "24h_5k_users"

secrets = json.loads(open("./secrets.json").read())

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_secret'])

api = tweepy.API(auth)

output_file = "processed/"+input_file+"_followers.json"

# Read in any processed followers so far and use them
num_unprocessed = 0
if os.path.isfile(output_file):
    with open("processed/"+input_file+".json") as in_f:
        with open(output_file) as out_f:
            with open("processed/tmp.json", 'w') as buffer_f:
                for line in out_f:
                    try:
                        processed = json.loads(line)
                        unprocessed = json.loads(in_f.readline())
                        # print unprocessed
                        if processed['screen_name'] == unprocessed['screen_name']:
                            buffer_f.write(json.dumps(processed)+'\n')
                        else:
                            print "what a disappointment"
                            num_unprocessed += 1
                            buffer_f.write(json.dumps(unprocessed)+'\n')
                    except:
                        print "end of input file reached"
                for line in in_f:
                    num_unprocessed += 1
                    buffer_f.write(line)

os.rename("processed/tmp.json", "processed/"+input_file+".json")

print "{0} users remaining to be processed".format(num_unprocessed)

failed = 0
with open("processed/"+input_file+".json") as in_f:
    with open(output_file, 'w') as out_f:
        for i,line in enumerate(in_f):
            print "Retrieving followers for user "+str(i)
            user = json.loads(line)
            if 'followers' not in user or len(user['followers']) == 0:
                user['followers'] = []
                try:
                    time.sleep(60)
                    followers = api.followers(user['id'])
                    for follower in followers:
                        rep = {}
                        for attr in ['lang', 'location', 'screen_name', 'followers_count', 'time_zone', 'id']:
                            rep[attr] = getattr(follower, attr)
                        user['followers'].append(rep)
                except:
                    failed += 1
                    print "\tfollowers retrieval failed"
            else:
                print "\tfollowers already found"

            out_f.write(json.dumps(user)+'\n')

print "Failed to process {0} users".format(failed)