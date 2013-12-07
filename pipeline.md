The rough pipeline used to create this data is:

1. Run ```pull_sample.py``` as long as necessary to get the data I needed (I got about 100k tweets in 24 hours)
2. Run ```get_subset.py``` to extract a random subset of the tweets collecting using a specific filtering criteria if desired (selected 5k randomly)
3. Run ```extract_users.py``` to re-format tweets as users
4. Run ```get_followers.py``` to get the followers of each user.  There is a 40s delay between requests because of Twitter's rate limiting, so I ran this on my server and left it alone several days.
5. Run ```get_countries.py```.  This uses the Bing Maps reverse-geocoding API to associate a country with each user and follower based on their "location" tag.  This is very probabilistic and errors definitely were introduced here. 