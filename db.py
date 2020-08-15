import sqlite3

connAM = sqlite3.connect('am.db')
connPM = sqlite3.connect('pm.db')

cA = connAM.cursor()
cB = connPM.cursor()

cA.execute('CREATE TABLE tweets (id int, todo text, tweetId int, userId int)')
cB.execute('CREATE TABLE tweets (id int, todo text, tweetId int, userId int)')

