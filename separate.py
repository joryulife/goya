import re

def separate(text,key1,key2,key3):
    text = re.sub(key1, '', text)
    text = re.sub(key2, '', text)
    text = re.sub(key3, '', text)
    text = text.replace("\n", "")
    todos = text.split('・')
    todos = todos[1:]
    return todos

def delet (text,key1,key2,key3):
    text = re.sub(key1, '', text)
    text = re.sub(key2, '', text)
    text = re.sub(key3, '', text)
    text = text.replace("\n", "")
    return text


#テスト
# text = "・今日の昼ご飯を作る\n・今日はメモ帳を買うぞ\n・宿題をするぞ\n#TODOリストゴーヤ"
# print(separate(text))