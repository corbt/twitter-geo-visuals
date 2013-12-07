import tweepy, json, time

in_file = "24h_5k_users"

secrets = json.loads(open("./secrets.json").read())

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_secret'])

api = tweepy.API(auth)

# print api.get_user('kylecorb')

with open("processed/"+in_file+".json") as in_f:
	with open("processed/"+in_file+"_followers.json", 'w') as out_f:
		for i,line in enumerate(in_f):
			print "Retrieving followers for user "+str(i)
			user = json.loads(line)
			if 'followers' not in user or len(followers) == 0:
				user['followers'] = []
				try:
					time.sleep(40)
					followers = api.followers(user['screen_name'])
					for follower in followers:
						rep = {}
						for attr in ['lang', 'location', 'screen_name', 'followers_count', 'time_zone']:
							rep[attr] = getattr(follower, attr)
						user['followers'].append(rep)
				except:
					print "\tfollowers retrieval failed"

			out_f.write(json.dumps(user)+'\n')
