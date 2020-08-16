import re

def separate(text):
    text = re.sub('#TODOリストゴーヤ', '', text)
    text = text.replace("\n", "")
    todos = text.split('・')
    todos = todos[1:]
    return todos


#テスト
# text = "・今日の昼ご飯を作る\n・今日はメモ帳を買うぞ\n・宿題をするぞ\n#TODOリストゴーヤ"
# print(separate(text))