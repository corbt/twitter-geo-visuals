import json, time, datetime, os
import tweepy

secrets = json.loads(open("./secrets.json").read())

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_secret'])

class RecordingListener(tweepy.streaming.StreamListener):
    """Saves the tweet data to a log file"""

    def __init__(self, divisor):
        super
        self.log_file = open(os.path.join("raw","{0}.json".format(datetime.datetime.now()).replace(":",".").replace(" ","-")),'w')
        self.count = 0
        self.divisor = divisor
        self.tracker = 0

    def on_data(self, data):
        if self.tracker == 0:
            data = json.loads(data)
            if "created_at" in data and data["coordinates"] != None:
                self.log_file.write(json.dumps(data)+"\n")
                self.count += 1
                print self.count
        self.tracker = (self.tracker+1) % self.divisor
        return True

    def on_error(self, status):
        print str(datetime.datetime.now())+" Error: "+str(status)

    def on_timeout(self):
        print str(datetime.datetime.now())+"Timeout"
        sleep(60)

stream = tweepy.Stream(auth, RecordingListener(1))

print "Beginning streaming"
while True:
    try:
        stream.sample()
    except Exception:
        print "Exception, but keep collecting"
