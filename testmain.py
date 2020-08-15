import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
import reply
import search
import datetime
import time
import schedule


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

POSTURL = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#reply.reply(twitter,1294500665134157825,"reply2")
#search.searchmain("#TODOリストゴーヤ",twitter)

def MonitarTL():
    tweets = search.searchmain("#TODOリストゴーヤ",twitter)
    if (tweets == None):
        print("line24")
        return None
    elif(len(tweets["statuses"]) == 0):
        print("line27")
        return None
    else:
        for tweet in tweets["statuses"]:
            reply.reply(twitter,tweet[u'id_str'],tweet[u"text"] +  "\nをタスクに追加だね！\n報告しないと責めるよ！")
    print("go-ya")

def job():
        print("DB1Goooooya!")




schedule.every().day.at("00:02").do(job)
schedule.every().day.at("00:03").do(job)
schedule.every(1).minutes.do(MonitarTL)


while True:
    schedule.run_pending()
    time.sleep(1)