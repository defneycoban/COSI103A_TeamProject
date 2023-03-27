import sqlite3
import os

#created by Defne
def toDict(t):
    ''' t is a tuple that gets converted to a dictionary'''
    transaction = {
    'item': t[0],
    'amount': t[1],
    'category': t[2],
    'date': t[3],
    'description': t[4]
    }
    return transaction

# All sql commands should be done in this class. Print statements go in tracker.py
class Transactions():
    ''' methods for obtaining transaction data '''
    # created by Zev
    def __init__(self):
        ''' initialize the database '''
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
                      (item int, amount int, date text, description text)''', ())
    
    # created by Eliora
    def sort(self, arg):
        ''' return the transactions sorted by the given argument '''
        if(arg=='month'):
            return self.runQuery(f"SELECT rowid,* from transactions where substr(date,6,2)={arg} DESC",())   #change dictName when implemented
        if(arg=='year'):
            return self.runQuery(f"SELECT rowid,* from transactions where substr(date,1,4)={arg} DESC",())
        else:
            return self.runQuery(f"SELECT rowid,* from transactions where date={arg} DESC",())
        # if(arg=='month'):
        #     arg = arg[5:7]
        # if(arg=='year'):
        #     arg = arg[0:4]
        # return self.runQuery(f"SELECT rowid,* from dictName ORDER BY {arg} DESC",())   #change dictName when implemented
    
    # created by Madina
    def show_transactions(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transactions",())
    
    # created by Madina
    def add(self,item):
        ''' create a transaction with all the fields needed and add it to the transactions table '''
        return self.runQuery("INSERT INTO TRANSACTIONS VALUES(?,?,?)",(item['item #'],item['amount'],item['category'],item['date'],item['description']))

    # created by Madina
    def delete(self,rowid):
        ''' delete a transaction '''
        return self.runQuery("DELETE FROM TRANSACTIONS WHERE rowid=(?)",(rowid,))

   # created by Defne
    def runQuery(self, query, tuple):
        '''execute a SQLite command and return the result as a list of dictionaries'''
        con= sqlite3.connect(os.getenv('HOME')+'/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        rows = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(row) for row in rows]
    
   

    