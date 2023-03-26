# pytest tests for transactions.py
from transactions import Transactions

t = Transactions('test.db')

def test_show_transactions(self):
    # Add some transactions to the database
    t.add({'title': 'Transaction 1', 'desc': 'Description 1', 'completed': False})
    t.add({'title': 'Transaction 2', 'desc': 'Description 2', 'completed': True})
    t.add({'title': 'Transaction 3', 'desc': 'Description 3', 'completed': False})
    transactions = t.show_transactions()

    assert len(transactions) == 3
    assert transactions[0]['title'] == 'Transaction 1'
    assert transactions[0]['desc'] == 'Description 1'
    assert transactions[0]['completed'] == False
    assert transactions[1]['title'] == 'Transaction 2'
    assert transactions[1]['desc'] == 'Description 2'
    assert transactions[1]['completed'] == True
    assert transactions[2]['title'] == 'Transaction 3'
    assert transactions[2]['desc'] == 'Description 3'
    assert transactions[2]['completed'] == False

    t.delete(1)
    t.delete(2)
    t.delete(3)
    
def test_add(self):
    # Add a transaction to the database
    t.add({'title': 'Transaction 1', 'desc': 'Description 1', 'completed': False})
    # Get the list of transactions
    transactions = t.show_transactions() 
    # Verify that the transaction was added correctly
    assert len(transactions) == 1
    assert transactions[0]['title'] == 'Transaction 1'
    assert transactions[0]['desc'] == 'Description 1'
    assert transactions[0]['completed'] == False
    
    # Delete the transaction from the database
    t.delete(1)
    
def test_delete(self):
    # Add a transaction to the database
    t.add({'title': 'Transaction 1', 'desc': 'Description 1', 'completed': False})
    
    # Delete the transaction from the database
    t.delete(1)
    
    # Get the list of transactions
    transactions = t.show_transactions()
    
    # Verify that the transaction was deleted correctly
    assert len(transactions) == 0
