# pytest tests for transactions.py
from transactions import Transactions
import pytest

@pytest.fixture
def path(tmp_path):
    yield tmp_path / 'todo.db'
    
# zev's test
@pytest.fixture(autouse = True)
def transactions(path): 
    db = Transactions(path)
    yield db
   
# tests creating database, add, and delete 
def test_init(transactions):
    db = transactions
    print(db)
    db.add({'amount': 1, 'date': '2022-02-26', 'description': 'Lunch'})
    results = db.show_transactions()
    assert len(results) == 1
    assert results[0]['amount'] == 1
    assert results[0]['date'] == '2022-02-26'
    db.delete(1)
    results = db.show_transactions()
    assert len(results) == 0

#Eliora's test
def test_sort(transactions):
    db = transactions
    # add some transactions
    db.add({'amount': 10.0, 'date': '2022-02-26', 'description': 'Lunch'})
    db.add({'amount': 5.0, 'date': '2022-03-24', 'description': 'Bus fare'})
    db.add({'amount': 20.0, 'date': '2023-01-27', 'description': 'Groceries'})
    # check original order
    rows = db.show_transactions()
    assert len(rows) == 3
    # assert rows[0]['description'] == 'Lunch'
    # assert rows[1]['description'] == 'Bus fare'
    # assert rows[2]['description'] == 'Groceries'
    # check if they are sorted by date
    rows = db.sort('date')
    #assert len(rows) == 3
    # assert rows[0]['description'] == 'Groceries'
    # assert rows[1]['description'] == 'Bus fare'
    # assert rows[2]['description'] == 'Lunch'
    # check if they are sorted by month
    #rows = db.sort('month')
    #assert len(rows) == 3
    # assert rows[0]['description'] == 'Bus fare'
    # assert rows[1]['description'] == 'Lunch'
    # assert rows[2]['description'] == 'Groceries'
    #check if they are sorted by year
    #rows = db.sort('year')
    #assert len(rows) == 3
    # assert rows[0]['description'] == 'Groceries'
    # assert rows[1]['description'] == 'Lunch'
    # assert rows[2]['description'] == 'Bus fare'

#Madina's method
def test_add(transactions):
    db = transactions 
    # add a transaction
    db.add({'amount': 10.0, 'date': '2022-03-26', 'description': 'Lunch'})
    # check if it was added
    rows = db.show_transactions()
    assert len(rows) == 1
    assert rows[0]['amount'] == 10.0
    assert rows[0]['date'] == '2022-03-26'
    assert rows[0]['description'] == 'Lunch'

#Madina's method
def test_delete(transactions):
    db = transactions
    # add a transaction
    db.add({'amount': 10.0, 'date': '2022-03-26', 'description': 'Lunch'})
    # delete the transaction
    db.delete(1)
    # check if it was deleted
    rows = db.show_transactions()
    assert len(rows) == 0

#Madina's method
def test_show_transactions(transactions):
    db = transactions
    # add some transactions
    db.add({'amount': 10.0, 'date': '2022-03-26', 'description': 'Lunch'})
    db.add({'amount': 5.0, 'date': '2022-03-26', 'description': 'Bus fare'})
    db.add({'amount': 20.0, 'date': '2022-03-27', 'description': 'Groceries'})
    # check if all transactions are returned
    rows = db.show_transactions()
    assert len(rows) == 3





