# All sql commands should be done in this class. Print statements go in tracker.py

class Transactions():
    ''' methods for obtaining transaction data '''
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
                      (item int, amount int, date text, description text))''', ())