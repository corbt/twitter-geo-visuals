import json, time, datetime, os
import tweepy

secrets = json.loads(open("./secrets.json").read())

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_secret'])



class RecordingListener(tweepy.streaming.StreamListener):
    """Saves the tweet data to a log file"""

    def on_connect(self):
        self.log_file = open(os.path.join("raw","{0}.json".format(datetime.datetime.now()).replace(":",".").replace(" ","-")),'w')
        self.log_file.write('[\n')

    def on_data(self, data):
        self.log_file.write('  '+data.strip()+",\n")
        time.sleep(0.5)
        return True

    def on_error(self, status):
        print status

    def on_timeout(self):
        print "Timeout at "+datetime.datetime.now()
        sleep(60)

stream = tweepy.Stream(auth, RecordingListener())
stream.sample()
