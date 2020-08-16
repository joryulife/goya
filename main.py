import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
import reply
import search
import datetime
import time
import schedule
import separate
import db
import datetime


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

POSTURL = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#reply.reply(twitter,1294500665134157825,"reply2")
#search.searchmain("#TODOリストゴーヤ",twitter)

Lastid = "0"
oldtweet = None
searchKey = "#TODOリストゴーヤ"
key2 = "#finish"
key3 = "#start"

oldtweet = search.searchmain(searchKey,twitter,Lastid,"1")
Lastid = oldtweet["statuses"][0][u'id_str']

connAM, dbAM = db.initDBAM()
connPM, dbPM = db.initDBPM()

def MonitarTL():
    global connAM, dbAM, connPM, dbPM
    global Lastid
    global oldtweet
    global searchKey
    tweets = None
    tweets = search.searchmain(searchKey,twitter,Lastid,"20")
    if (tweets == None):
        print("line24")
        return None
    elif(len(tweets["statuses"]) == 0):
        print("line27")
        return None
    else:
        Lastid = tweets["statuses"][0][u'id_str']
        for tweet in tweets["statuses"]:
            try:
                if (key2 in tweet["text"] and key3 in tweet["text"]):
                    print("in")
                else :
                    print("tweet.text: ", tweet["text"])
                    todos = separate.separate(tweet["text"],searchKey,key2,key3)
                    reply.reply(twitter,tweet[u'id_str'],separate.delet(tweet["text"],searchKey,key2,key3) + "\nをタスクに追加だね！\n報告しないと責めるよ！")
                    now = datetime.datetime.now()
                    if(now.hour < 12):
                        db = dbAM
                        print("AM")
                    else:
                        db = dbPM
                        print("PM")
                    for todo in todos:
                        print("todo: " + todo)
                        db.execute("INSERT INTO tweets (todo, tweetId, userId) VALUES(?, ?, ?)", (todo, int(tweet["id"]), int(tweet["user"]["id"])))
            except Exception as e:
                print(e) 
        connAM.commit()
        connPM.commit()
        connAM.commit()
        connPM.commit()
            # #午前午後判定してDB格納

def job(DBNo):
    if (DBNo == 1):
        print("DB1Goooooya!")
        #DBAM　に参照要請、催促ツイート
    elif(DBNo == 2):
        print("DBGooooooya!")
        #DBOM に参照要請　催促ついーと



MonitarTL()
schedule.every().day.at("11:02").do(job,1)
schedule.every().day.at("11:03").do(job,2)
schedule.every(10).seconds.do(MonitarTL)


while True:
    schedule.run_pending()
    time.sleep(1)
