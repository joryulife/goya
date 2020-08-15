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
    tweets = search.searchmain("TODO~",twitter)
    if (tweets == None):
        return None
    elif(len(tweets["status"]) == 0):
        return None
    else:
        #if "end","finish""start"がない時DBにタスクを渡す
            reply.reply(twitter,tweet[u'id_str'],"受け取ったタスク" +  "\nをタスクに追加だね！\n報告しないと責めるよ！")
            #if tweet[u'created_at']<12 DB1に
            #if tweet[u'created_at']>12 DB2に
        #else "end"~があるときDBにタスク削除を要請

def Rimindjob(DBNo):
    if(DBNo == 1):
        #DB1に照会、Falseに
        #reply.reply(twitter,tweetid,"終わってないよ！" + task)
    else:
        



schedule.every().day.at("15:00").do(job())
schedule.every().day.at("18:00").do(job())
schedule.every().hour.do(MonitarTL())


while True:
    schedule.run_pending()
    time.sleep(1)