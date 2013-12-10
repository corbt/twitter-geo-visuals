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
                
with open("processed/"+input_file+".json") as in_f:
    with open("processed/"+input_file+"_countries.json", 'w') as out_f:
        for i,line in enumerate(in_f):
            print "Finding country for user {0}".format(i)
            try:
                user = json.loads(line)
                user['country'] = get_country(user['location'])
                if user['country'] != None:
                    followers = []
                    for follower in user['followers']:
                        try:
                            if len(followers) < max_followers_to_process:
                                follower['country'] = get_country(follower['location'])
                                if follower['country'] != None:
                                    followers.append(follower)
                        except:
                            print "\tOne follower failed"
                    user['followers'] = followers
                    out_f.write(json.dumps(user)+'\n')
            except:
                print "\tWhole process failed"
