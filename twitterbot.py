import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('key', 'secret')

api = tweepy.API(auth)
user = api.me()
print(user.name)
def limit_handle(cursor):
   try:
        while True:
            yield cursor.next()
   except tweepy.RateLimitError:
       time.sleep(1000)

Genrous Bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 1:
        follower.follow()
         break

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
