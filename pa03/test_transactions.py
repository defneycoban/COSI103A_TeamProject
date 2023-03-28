'''Testing various functions of transactions.py'''
import pytest
from transactions import Transactions

@pytest.fixture
def path(tmp_path):
    '''creates temporary database path'''
    yield tmp_path / 'todo.data'
# zev's test
@pytest.fixture(autouse = True)
def transactions(path):
    '''creating databse'''
    data = Transactions(path)
    yield data
# tests creating database, add, and delete
def test_init(transactions):
    '''testing basic sql functions'''
    data = transactions
    print(data)
    data.add({'amount': 1, 'date': '2022-02-26', 'description': 'Lunch'})
    results = data.show_transactions()
    assert len(results) == 1
    assert results[0]['amount'] == 1
    assert results[0]['date'] == '2022-02-26'
    data.delete(1)
    results = data.show_transactions()
    assert len(results) == 0

#Eliora's test
def test_sort(transactions):
    '''testing sort methods'''
    data = transactions
    # add some transactions
    data.add({'amount': 10.0, 'date': '2022-02-26', 'description': 'Lunch'})
    data.add({'amount': 5.0, 'date': '2022-03-24', 'description': 'Bus fare'})
    data.add({'amount': 20.0, 'date': '2023-01-27', 'description': 'Groceries'})
    # check original order
    rows = data.show_transactions()
    assert len(rows) == 3
    assert rows[0]['description'] == 'Lunch'
    assert rows[1]['description'] == 'Bus fare'
    assert rows[2]['description'] == 'Groceries'
    # check if they are sorted by date
    rows = data.sort('dates')
    assert len(rows) == 3
    assert rows[0]['description'] == 'Groceries'
    assert rows[1]['description'] == 'Bus fare'
    assert rows[2]['description'] == 'Lunch'
    # check if they are sorted by month
    rows = data.sort('02')
    assert len(rows) == 1
    assert rows[0]['description'] == 'Lunch'
    #check if they are sorted by year
    rows = data.sort('2022')
    assert len(rows) == 2
    assert rows[0]['description'] == 'Bus fare'
    assert rows[1]['description'] == 'Lunch'

#Madina's method
def test_add(transactions):
    '''testing add method'''
    data = transactions
    # add a transaction
    data.add({'amount': 10.0, 'date': '2022-03-26', 'description': 'Lunch'})
    # check if it was added
    rows = data.show_transactions()
    assert len(rows) == 1
    assert rows[0]['amount'] == 10.0
    assert rows[0]['date'] == '2022-03-26'
    assert rows[0]['description'] == 'Lunch'

#Madina's method
def test_delete(transactions):
    '''testing delete method'''
    data = transactions
    # add a transaction
    data.add({'amount': 10.0, 'date': '2022-03-26', 'description': 'Lunch'})
    # delete the transaction
    data.delete(1)
    # check if it was deleted
    rows = data.show_transactions()
    assert len(rows) == 0

#Madina's method
def test_show_transactions(transactions):
    '''testing show transactions'''
    data = transactions
    # add some transactions
    data.add({'amount': 10.0, 'date': '2022-03-26', 'description': 'Lunch'})
    data.add({'amount': 5.0, 'date': '2022-03-26', 'description': 'Bus fare'})
    data.add({'amount': 20.0, 'date': '2022-03-27', 'description': 'Groceries'})
    # check if all transactions are returned
    rows = data.show_transactions()
    assert len(rows) == 3

def test_run_query(transactions):
    '''testing run_query'''
    data = transactions
    # add some transactions to the database
    data.run_query("INSERT INTO transactions VALUES (10.0, '2022-03-26', 'Lunch')", ())
    data.run_query("INSERT INTO transactions VALUES (5.0, '2022-03-26', 'Bus fare')", ())
    data.run_query("INSERT INTO transactions VALUES (20.0, '2022-03-27', 'Groceries')", ())
    # execute a SELECT query to retrieve the transaction data
    results = data.show_transactions()

    # check if the number of rows returned is correct
    assert len(results) == 3
    # check if the data in the rows is correct
    assert results[0]['amount'] == 10.0
    assert results[0]['date'] == '2022-03-26'
    assert results[0]['description'] == 'Lunch'
    assert results[1]['amount'] == 5.0
    assert results[1]['date'] == '2022-03-26'
    assert results[1]['description'] == 'Bus fare'
    assert results[2]['amount'] == 20.0
    assert results[2]['date'] == '2022-03-27'
    assert results[2]['description'] == 'Groceries'
