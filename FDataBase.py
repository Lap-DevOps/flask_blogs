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
