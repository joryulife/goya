def separate(text):
    text = text.lstrip()
    text = text.replace("\n", "")
    return text.split('・')

def delhash(text,key):
    text = text.strip(key)
    return text


#テスト
"""
text = "・今日のご飯は何かな\n・今日はメモ帳を買うぞ\n・宿題をするぞ"
print(separate(text))
"""
