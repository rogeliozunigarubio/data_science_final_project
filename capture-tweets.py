from __future__ import print_function
import sys

from TwitterSearch import *

out = open('test-kingston-tweets.txt', 'ab')

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['beach','trash'])
    tso.set_geocode(18.0180869,-76.8708689,100,True) #Kingston Jamaica Test
    tso.set_language('en')
    tso.set_include_entities(False)

    ts = TwitterSearch(
        consumer_key = 'FnrBL5aEee3HVWNz6cyZFbFWn',
        consumer_secret = "ApRZXcUrn0RSRTRYuNEKCnT1u7M3q4AF1HLOE4EIlZwra5Vxi4",
        access_token = '252839559-mX10HRG7gRnUzkFMtJp4xK76KO6mtiREBC5BzVsi',
        access_token_secret = 'ML3kxVxra6PJ0VDrPuHhehNHzIh2iGi1OJzNXXPqTfNXo'
     )


    for tweet in ts.search_tweets_iterable(tso):
        out.write( tweet['text'].encode('utf-8')  + "\n" )
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    print(ts.get_statistics())

except TwitterSearchException as e: 
    print(e)
