import json, requests

input_file = "24h_5k_users_followers"
max_followers_to_process = 5


secrets = json.loads(open("./secrets.json").read())
key = secrets['bing_key']


def get_country(location):
	# return "United States"
	if location == None or len(location) < 2:
		return None

	data = requests.get("http://dev.virtualearth.net/REST/v1/Locations", params={'q': location, 'key': key})
	resources = data.json()['resourceSets'][0]['resources']
	
	if len(resources) > 0:
		return resources[0]['address']['countryRegion']
	else:
		return None

# print get_country("seattle")
# print get_country("alskdfj alsdkfj j;sldkj;lasdfkj;laksjd f;sd; w")

with open("processed/"+input_file+".json") as in_f:
	with open("processed/"+input_file+"_countries.json", 'w') as out_f:
		for line in in_f:
			user = json.loads(line)
			user['country'] = get_country(user['location'])
			if user['country'] != None:
				followers = []
				for follower in user['followers']:
					if len(followers) < max_followers_to_process:
						follower['country'] = get_country(follower['location'])
						if follower['country'] != None:
							followers.append(follower)
				user['followers'] = followers
				out_f.write(json.dumps(user)+'\n')

				# print json.dumps(user, indent=2)