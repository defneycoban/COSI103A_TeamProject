'''this class is responsible for the transaction database and its operations'''
import sqlite3

#created by Defne
def to_dict(trans):
    ''' t is a tuple that gets converted to a dictionary'''
    transaction = {
    'id': trans[0],
    'amount': trans[1],
    'date': trans[2],
    'description': trans[3]
    }
    return transaction

# All sql commands should be done in this class. Print statements go in tracker.py
class Transactions():
    ''' methods for obtaining transaction data '''
    # created by Zev
    def __init__(self, path):
        ''' initialize the database '''
        self.path = path
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                      (amount int, date text, description text)''', ())

    # created by Eliora
    def sort(self, arg):
        ''' return the transactions sorted by the given argument '''
        if len(arg)==2:
            return self.run_query("""SELECT rowid,* from transactions where substr(date,6,2)=(?)
                                  ORDER BY date DESC""",(arg,))
        if len(arg)==4:
            return self.run_query("""SELECT rowid,* from transactions where substr(date,1,4)=(?)
                                  ORDER BY date DESC""",(arg,))
        return self.run_query("SELECT rowid,* from transactions ORDER BY date DESC",())

    # created by Madina
    def show_transactions(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.run_query("SELECT rowid,* from transactions",())

    # created by Madina
    def add(self,item):
        ''' create a transaction with all the fields needed and add it to the transactions table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?)"
                              ,(item['amount'],item['date'],item['description']))

    # created by Madina
    def delete(self,rowid):
        ''' delete a transaction '''
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)",(rowid,))

   # created by Defne
    def run_query(self, query, args):
        '''execute a SQLite command and return the result as a list of dictionaries'''
        # con= sqlite3.connect(os.getenv('HOME')+'/tracker.db')
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        cur.execute(query, args)
        rows = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(row) for row in rows]
    