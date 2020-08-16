import tweepy
import datetime
import separate
import db

dt_now = datetime.datetime.now()


#key
CONSUMER_KEY='wh0mHJxRQRNSJC198snWQcclj'
CONSUMER_SECRET='JVGpK0sJqp6maNrWW2Tf5hmTQy5KZJpKt3tJyxGj2yl2Zy0zs7'
ACCESS_TOKEN='1293934617595060225-SjIiaNZ90eRwaiSqGEG0MrO5Iuuo6Q'
ACCESS_SECRET='HgRa3SVpShjxn7eTjpEbR0jWxJw6NhRUG6LkFom7s55jG'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


connAM, dbAM = db.initDBAM()
connPM, dbPM = db.initDBPM()

for tweet in api.search(q="#TODOリストゴーヤ  exclude:retweets", tweet_mode='extended',count=10):

    try:
        todos = separate.separate(tweet.full_text)
        for todo in todos:
            print("todo: " + todo)
            print("%s" % todo)
            print("todo")
            dbAM.execute("INSERT INTO tweets (todo, tweetId, userId, done) VALUES(?, ?, ?, ?)", (todo, int(tweet.id), int(tweet.user.id), false))
    except Exception as e:
        print(e)

connAM.commit()
connPM.commit()
connAM.close()
connPM.close()

print(tweets)


