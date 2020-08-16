import sqlite3


def initDBAM():
    connAM = sqlite3.connect('am.db')

    dbAM = connAM.cursor()

    dbAM.execute('DROP TABLE IF EXISTS tweets')

    dbAM.execute('''CREATE TABLE IF NOT EXISTS tweets (id INTEGER PRIMARY KEY, todo text, tweetId int, userId int)''')
    return connAM, dbAM

def initDBPM():
    connPM = sqlite3.connect('pm.db')

    dbPM = connPM.cursor()
    dbPM.execute('DROP TABLE IF EXISTS tweets')
    dbPM.execute('''CREATE TABLE IF NOT EXISTS tweets (id INTEGER PRIMARY KEY, todo text, tweetId int, userId int)''')
    return connPM, dbPM


