from requests_oauthlib import OAuth1Session
import json

def searchmain(search_word,twitter,id,Co):
    tweets = tweet_search(search_word, twitter,id,Co)
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id']
        tweet_idstr = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        print ("tweet_id:", tweet_id)
        print ("tweet_idstr", tweet_idstr)
        print ("text:", text)
        print ("created_at:", created_at)
        print ("user_id:", user_id)
        print ("user_desc:", user_description)
        print ("screen_name:", screen_name)
        print ("user_name:", user_name)
        print("  ")
    return tweets

def tweet_search(search_word, twitter,id,Co):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    if (id != "0"):
        params = {
            "q": search_word,
            "lang": "ja",
            "result_type": "recent",
            "count": Co,
            "since_id": id
            }
    else:
        params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": Co
        }
    responce = twitter.get(url, params = params)
    if responce.status_code != 200:
        print ("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets