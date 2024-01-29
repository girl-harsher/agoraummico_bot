import tweepy

api_key = 'bGqeieN1OperdV5JMbzEXFMy5'
api_secret = '8ZqLgazwOao8bKj11W2WP9ETJA9Jt7GH8Urdope6Qihq4lrClI'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMWFsAEAAAAACQWV%2FExOBZVndyZClsXOr0EoGNo%3DWMbXAOWoEkQtFtegCFd6RDb9v7kJlcxbesQAV2mMBKjyI0Uf7u'
access_token = '1751786706687213568-1bIU1BhFMvBxEPCHZlLUn3UIrYQLtg'
access_token_secret = 'jMQwck2sEIPB2wmua2KWoDVyo7J2Qm3uWhDCh2GaiJzLa'

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)
            
        except Exception as error:
            print(error)
        

stream = MyStream(bearer_token=bearer_token)

rule = tweepy.StreamRule("(mico OR micoso OR micosa) (-is:retweet -is:reply)")

stream.add_rules(rule)

stream.filter()