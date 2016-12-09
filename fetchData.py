import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('geoTweets2.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


def main():
    #set up auth
    consumer_key = 'IVm5S92fcZ4plOndhaCkDg75S'
    consumer_secret = 'f0AEyVnk9USLEOc5SxIsKC3yZOFd0IH806viYsvYsiicQV5iMp'
    access_token = '1849521458-X5ZeVo8m6acF5IY41yfgxnWjUxKECVVyg1tVH68'
    access_secret = '7CoFQxNhZ3hc394isbTvzxpTEBRNOCd3LlJxkto18b4D2'
     
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
     
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(locations=[-122.75,36.8,-121.75,37.8,
                                     -74.069824,40.477399,-73.700272,40.912475,
                                     -87.94,41.64,-87.52,42.02,
                                     -118.67,33.70,-118.16,34.3373,
                                     -71.19,42.29,-70.99,42.40,
                                     -122.46,47.49,-122.22,47.73])
##
if __name__ == "__main__":
    main()

