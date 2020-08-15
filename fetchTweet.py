import tweepy
import datetime

dt_now = datetime.datetime.now()


#key
CONSUMER_KEY='wh0mHJxRQRNSJC198snWQcclj'
CONSUMER_SECRET='JVGpK0sJqp6maNrWW2Tf5hmTQy5KZJpKt3tJyxGj2yl2Zy0zs7'
ACCESS_TOKEN='1293934617595060225-SjIiaNZ90eRwaiSqGEG0MrO5Iuuo6Q'
ACCESS_SECRET='HgRa3SVpShjxn7eTjpEbR0jWxJw6NhRUG6LkFom7s55jG'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweet_data = []#データの格納

# for tweet in api.search(q="TODOリスト⚡️  exclude:retweets",tweet_mode='extended',count=10):
#     try:
#         tweet_data.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count])
#     except Exception as e:
#         print(e)
for tweet in api.search(q="#TODOリストゴーヤ  exclude:retweets",since = datetime.date.today(), tweet_mode='extended',count=10):
    try:
        tweet_data.append([tweet.full_text.replace('\n',''), tweet.user.screen_name])
    except Exception as e:
        print(e)
print(tweet_data)


