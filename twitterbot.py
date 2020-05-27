import tweepy
import time

auth = tweepy.OAuthHandler('Pp8aIDN0ZHPMciWn8NBaCn0a9', 'bui7ENzqQ2SnFOZMoJyGTH4VpncEHHnS0lGNUoxrPmHfHL9K67')
auth.set_access_token('992028204381728768-49MlqozE4Zsz5oJWqg99w7B0psiX2eQ', '4W42CDrtSmHnntHO6Bxp6i9BPVn9TqvG3iaUPRGMuwy1W')

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