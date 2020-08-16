def separate(text):
    text = text.lstrip()
    text = text.replace("\n", "")
    return text.split('・')

def delhash(text,key):
    text = text.strip(key)
    return text


<<<<<<< HEAD
#テスト
"""
text = "・今日のご飯は何かな\n・今日はメモ帳を買うぞ\n・宿題をするぞ"
print(separate(text))
"""
=======
text = "・今日の昼ご飯を作る\n・今日はメモ帳を買うぞ\n・宿題をするぞ"
print(separate(text))

>>>>>>> 35c6e3f6bbc3acbfcf4f85fb17f7c7dd097eddfd
