from requests_oauthlib import OAuth1Session
import json


def searchmain(search_word,twitter):
    tweets = tweet_search(search_word, twitter)
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        print ("tweet_id:", tweet_id)
        print ("text:", text)
        print ("created_at:", created_at)
        print ("user_id:", user_id)
        print ("user_desc:", user_description)
        print ("screen_name:", screen_name)
        print ("user_name:", user_name)
        print("  ")
    return

def tweet_search(search_word, twitter):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": "15"
        }
    responce = twitter.get(url, params = params)
    if responce.status_code != 200:
        print ("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets