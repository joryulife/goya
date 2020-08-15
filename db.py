import sqlite3

conn = sqlite3.connect('goya.db')

c = conn.cursor()

c.execute('CREATE TABLE tweets (id int, todo text, tweetId int, userId int)')