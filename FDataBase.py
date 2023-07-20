import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = ''' SELECT * FROM mainmenu '''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                for x in res[1]:
                    print (x)
                return res
        except:
            print("Error load database !")
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?,?,?)', (title,text,tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print ("Error adding to database" + str(e))
            return False

        return True
