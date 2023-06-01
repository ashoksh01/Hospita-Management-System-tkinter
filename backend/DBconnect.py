import mysql.connector

class DBConnect:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost', username='root', password='Stha1234@@##', database='hospitalalgorithm')
        self.cur=self.con.cursor()


    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def select(self,query):
        self.cur.execute(query)
        rows=self.cur.fetchall()
        return rows

    def login(self,query,values):
        self.cur.execute(query,values)
        rows=self.cur.fetchall()
        return rows
    def Fetch(self,query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows