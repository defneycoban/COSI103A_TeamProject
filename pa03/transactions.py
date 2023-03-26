import sqlite3

# All sql commands should be done in this class. Print statements go in tracker.py
class Transactions():
    ''' methods for obtaining transaction data '''

    def __init__(self):
        ''' initialize the database '''
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
                      (item int, amount int, date text, description text))''', ())
    
    def sort(self, arg):
        ''' return the transactions sorted by the given argument '''
        return self.runQuery(f"SELECT rowid,* from dictName ORDER BY {arg} DESC",())   #change dictName when implemented
    
    def show_transactions(self):
        ''' printing the transactions '''
        self.c.execute("SELECT * FROM transactions")
        transactions = self.c.fetchall()
        for transaction in transactions:
            print(transaction)

    def add_transaction(self, item, amount, category, date, description):
        '''adding a new transaction with all the required fields'''
        self.c.execute("INSERT INTO transactions (item, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (item, amount, category, date, description))
        self.conn.commit()
        print("Transaction added successfully!")

    def delete_transaction(self, item):
        '''deleting an existing transactions'''
        self.c.execute("DELETE FROM transactions WHERE item=?", (item,))
        self.conn.commit()
        print("Transaction deleted successfully!")


   

    