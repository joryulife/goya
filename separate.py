import re

def separate(text):
    text = re.sub('#TODOリストゴーヤ', '', text)
    text = text.replace("\n", "")
    todos = text.split('・')
    todos = todos[1:]
    return todos

def delhash(text,key):
    text = text.strip(key)
    return text


<<<<<<< HEAD
<<<<<<< HEAD
#テスト
"""
text = "・今日のご飯は何かな\n・今日はメモ帳を買うぞ\n・宿題をするぞ"
print(separate(text))
"""
=======
text = "・今日の昼ご飯を作る\n・今日はメモ帳を買うぞ\n・宿題をするぞ"
print(separate(text))
=======
# text = "・今日の昼ご飯を作る\n・今日はメモ帳を買うぞ\n・宿題をするぞ\n#TODOリストゴーヤ"
# print(separate(text))
>>>>>>> a08c86374c03b26af0b359ffeb102aeef5752f71

>>>>>>> 35c6e3f6bbc3acbfcf4f85fb17f7c7dd097eddfd
