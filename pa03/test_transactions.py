# pytest tests for transactions.py
from transactions import Transactions

def db():
    return Transactions('test.db')

def test_add(db):
    # add a transaction
    db.add({'item #': 1, 'amount': 10.0, 'category': 'Food', 'date': '2022-03-26', 'description': 'Lunch'})
    # check if it was added
    rows = db.show_transactions()
    assert len(rows) == 1
    assert rows[0]['item #'] == 1
    assert rows[0]['amount'] == 10.0
    assert rows[0]['category'] == 'Food'
    assert rows[0]['date'] == '2022-03-26'
    assert rows[0]['description'] == 'Lunch'

def test_delete(db):
    # add a transaction
    db.add({'item #': 1, 'amount': 10.0, 'category': 'Food', 'date': '2022-03-26', 'description': 'Lunch'})
    # delete the transaction
    db.delete(1)
    # check if it was deleted
    rows = db.show_transactions()
    assert len(rows) == 0

def test_show_transactions(db):
    # add some transactions
    db.add({'item #': 1, 'amount': 10.0, 'category': 'Food', 'date': '2022-03-26', 'description': 'Lunch'})
    db.add({'item #': 2, 'amount': 5.0, 'category': 'Transport', 'date': '2022-03-26', 'description': 'Bus fare'})
    db.add({'item #': 3, 'amount': 20.0, 'category': 'Shopping', 'date': '2022-03-27', 'description': 'Groceries'})
    # check if all transactions are returned
    rows = db.show_transactions()
    assert len(rows) == 3
    assert rows[0]['item #'] == 1
    assert rows[1]['item #'] == 2
    assert rows[2]['item #'] == 3
