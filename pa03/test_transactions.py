# pytest tests for transactions.py
from transactions import Transactions

transaction = Transactions()

def test_add_transaction():
    tracker = transaction('test.db')
    tracker.add_transaction(1, 10, 'food', '2023-03-26', 'Lunch')
    tracker.c.execute("SELECT * FROM transactions")
    transaction = tracker.c.fetchone()
    assert transaction == (1, 10, 'food', '2023-03-26', 'Lunch')

def test_show_transactions():
    # Initialize Transaction object and add a transaction
    tracker = transaction('test.db')
    tracker.add_transaction(1, 10, 'food', '2023-03-26', 'Lunch')

    # Get the transactions as a list of strings
    transactions = tracker.get_transactions_as_strings()

    # Check that the transactions are formatted correctly
    expected_output = 'Item: 1, Amount: 10, Category: food, Date: 2023-03-26, Description: Lunch\n'
    assert transactions == expected_output

def test_delete_transaction():
    # Initialize Transaction object and add a transaction
    tracker = transaction('test.db')
    tracker.add_transaction(1, 10, 'food', '2023-03-26', 'Lunch')

    # Delete the transaction
    tracker.delete_transaction(1)

    # Check that the transaction was deleted
    tracker.c.execute("SELECT * FROM transactions")
    transaction = tracker.c.fetchone()
    assert transaction is None