import sqlite3

con= sqlite3.connect('tracker.db')
cur = con.cursor()

# All sql commands should be done in this class. Print statements go in tracker.py
class Transactions():
    ''' methods for obtaining transaction data '''
    # created by Zev
    def __init__(self):
        ''' initialize the database '''
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
                      (item int, amount int, date text, description text))''', ())
    
    def sort(self, arg):
        ''' return the transactions sorted by the given argument '''
        return self.runQuery(f"SELECT rowid,* from dictName ORDER BY {arg} DESC",())   #change dictName when implemented
    

    # created by Madina
    def show_transactions(self):
        ''' printing the transactions '''
        string = ""
        self.c.execute("SELECT * FROM transactions")
        transactions = self.c.fetchall()
        transaction = [f"Item: {t[0]}, Amount: {t[1]}, Category: {t[2]}, Date: {t[3]}, Description: {t[4]}" for t in transactions]
        return '\n'.join(transaction)

    # created by Madina
    def add_transaction(self, item, amount, category, date, description):
        '''adding a new transaction with all the required fields'''
        self.c.execute("INSERT INTO transactions (item, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (item, amount, category, date, description))
        self.conn.commit()

    # created by Madina
    def delete_transaction(self, item):
        '''deleting an existing transactions'''
        self.c.execute("DELETE FROM transactions WHERE item=?", (item,))
        self.conn.commit()

# and finally we commit our changes and close the connection
con.commit()
con.close()
   

    