from __future__ import print_function
import sys

from TwitterSearch import *

out = open('test-captured-tweets.txt', 'ab')

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['beach','trash']) # let's define all words we would like to have a look for
    #tso.set_geocode(18.471215,-77.9398878,100,True) # we want to see German tweets only
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'FnrBL5aEee3HVWNz6cyZFbFWn',
        consumer_secret = "ApRZXcUrn0RSRTRYuNEKCnT1u7M3q4AF1HLOE4EIlZwra5Vxi4",
        access_token = '252839559-mX10HRG7gRnUzkFMtJp4xK76KO6mtiREBC5BzVsi',
        access_token_secret = 'ML3kxVxra6PJ0VDrPuHhehNHzIh2iGi1OJzNXXPqTfNXo'
     )


    for tweet in ts.search_tweets_iterable(tso):
        #out.write( (str(tweet['text']) + "\n" ).encode('utf-8') )
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    print(ts.get_statistics())

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
