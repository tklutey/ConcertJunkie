#
# Calls Bandsintown API to return dict of concert results
# Takes artist name and current location as inputs
# Returns proximity of closest show(s)
#

# from urllib2 import urlopen
import urllib2
from urllib2 import urlopen
import json
import sys
import pprint
import datetime
import time

class FindShows:


    def __init__(self, artist, location):
        # self.artist = artist
        self.artist = artist.encode("utf-8")
        self.location = location
        self.artist_shows = self.load_result(self.artist)
        # pprint.pprint(self.artist_shows)

    def load_result(self, name):

        # name = unicode(name, "utf-8")
        # print "here"
        # name = name.decode("utf-8")
        # print type(name)
        # try:
            if " " in name:
                name = "%20". join(name.split())
            url = "http://api.bandsintown.com/artists/" + name + "/events.json?app_id=GOTCHA"
            sample = urlopen(url)
            response = sample.read()
            return json.loads(response)
        # except urllib2.HTTPError:
        #     sys.exit("error connecting to API")




    def get_show(self):

        shows = []

        for x in range(len(self.artist_shows)):
            if self.artist_shows[x]["venue"]["city"] == self.location:
                shows.append(self.artist_shows[x])
            # print self.artist_shows[any]["venue"]["city"]
        #
        # for y in shows:
        #     pprint.pprint(y)
        #
        # if len(shows) == 0 and len(self.artist) > 0:
        #     print "this artist is on tour but not to your city"
        # elif len(shows) == 0 and len(self.artist) == 0:
        #     print "this artist is not on tour"

        for x in range(len(shows)):
            venue = shows[x]["venue"]["name"]
            t = shows[x]["datetime"]
            # date = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
            # date = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
            # datestring = time.strptime()

            # print self.artist

            # str = self.artist.decode("utf-8") + " is playing at " + venue + " on " + t

            str = self.artist.decode("utf-8") + " is playing at " + venue + " on " + t

            print str





