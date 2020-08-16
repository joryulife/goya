import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
import reply
import search
import datetime
import time
import schedule
import separate


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
searchKey = "#TODOlistゴーヤ"

oldtweet = search.searchmain(searchKey,twitter,Lastid,"1")
Lastid = oldtweet["statuses"][0][u'id_str']

def MonitarTL():
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
            text = separate.delhash(tweet[u'text'],searchKey)
            #if タスクの宣言なら
            reply.reply(twitter,tweet[u'id_str'],text + "\nをタスクに追加だね！\n報告しないと責めるよ！")
            #午前午後判定してDB格納
            #ifel "#searchKey" + "#finish"or"#start" + "タスク"ならDBに変更要請

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
schedule.every(1).minutes.do(MonitarTL)


while True:
    schedule.run_pending()
    time.sleep(1)
