def tweetpost(tw,txt):
    message = txt
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": message, "auto_populate_reply_metadata":True}

    res = tw.post(url, params=params)

    if res.status_code == 200:
        print("Success.")
    else:
        print("Failed.")
        print(" - Responce Status Code : {}".format(res.status_code))
        print(" - Error Code : {}".format(res.json()["errors"][0]["code"]))
        print(" - Error Message : {}".format(res.json()["errors"][0]["message"]))
        # {'errors': [{'code': 170, 'message': 'Missing required parameter: status.'}]}

def mentionpost(tw,txt,user):
    message = (user + "\n" + txt)
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": message, "auto_populate_reply_metadata":True}

    res = tw.post(url, params=params)

    if res.status_code == 200:
        print("Success.")
    else:
        print("Failed.")
        print(" - Responce Status Code : {}".format(res.status_code))
        print(" - Error Code : {}".format(res.json()["errors"][0]["code"]))
        print(" - Error Message : {}".format(res.json()["errors"][0]["message"]))
        # {'errors': [{'code': 170, 'message': 'Missing required parameter: status.'}]}
