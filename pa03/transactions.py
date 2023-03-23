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