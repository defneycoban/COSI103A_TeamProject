# PA03

This is our programming assignment for PA03. We have a file transactions.py, which creates a database for financial transactions and handles all queries to the database (add, delete, sort, etc.). We have a file tracker.py, which presents the user with options for database interactions and makes calls to the Transactions class to update the database. Lastly, we have a file test_transactions.py which tests the Transactions class.

We divided all the methods amongst our team members, and we each implemented and tested our own. We then worked together on debugging and formatting.

- Running pylint script on transactions.py:

(base) Eliora@MacBook-Pro pa03 % pylint transactions.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

- Running pylint script on tracker.py:

(base) Eliora@MacBook-Pro pa03 % pylint tracker.py
************* Module tracker
tracker.py:10:0: R0912: Too many branches (20/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.84/10 (previous run: 9.84/10, +0.00)

(We decided to keep the number of branches, since the method inherently required lots of if statements and this follows Professor Hickey's formatting from previous lectures)

- Running pylint on test_transactions.py:

(base) Eliora@MacBook-Pro pa03 % pylint test_transactions.py
************* Module test_transactions
test_transactions.py:11:17: W0621: Redefining name 'path' from outer scope (line 6) (redefined-outer-name)
test_transactions.py:16:14: W0621: Redefining name 'transactions' from outer scope (line 11) (redefined-outer-name)
test_transactions.py:30:14: W0621: Redefining name 'transactions' from outer scope (line 11) (redefined-outer-name)
test_transactions.py:60:13: W0621: Redefining name 'transactions' from outer scope (line 11) (redefined-outer-name)
test_transactions.py:73:16: W0621: Redefining name 'transactions' from outer scope (line 11) (redefined-outer-name)
test_transactions.py:85:27: W0621: Redefining name 'transactions' from outer scope (line 11) (redefined-outer-name)
test_transactions.py:96:19: W0621: Redefining name 'transactions' from outer scope (line 11) (redefined-outer-name)

------------------------------------------------------------------
Your code has been rated at 9.09/10 (previous run: 9.09/10, +0.00)

(We decided to keep this, since it had to do with the database path and we didn't want to mess with it)

- Running pytest:

(base) Eliora@MacBook-Pro pa03 % pytest
================================================== test session starts ==================================================
platform darwin -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/Eliora/Desktop/github/COSI103A_TeamProject/pa03
plugins: anyio-3.5.0
collected 6 items                                                                                                       

test_transactions.py ......                                                                                       [100%]

=================================================== 6 passed in 0.04s ===================================================

- Running Eliora's methods from tracker.py:

Eliora wrote the process method.

process:

>> quit
(base) Eliora@MacBook-Pro pa03 % python3 tracker.py
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
>> show
no transactions to print
----------------------------------------



>> add 10 2022-03-06 lunch
----------------------------------------



>> add 15 2022-06-03 dinner
----------------------------------------



>> add 20 2023-03-07 breakfast
----------------------------------------



>> show


id     amount       date                    description
------------------------------------------------------------------------------------------
1 10 2022-03-06 lunch
2 15 2022-06-03 dinner
3 20 2023-03-07 breakfast
----------------------------------------



>> add 2
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> summarizeMonths 03


id     amount       date                    description
------------------------------------------------------------------------------------------
3 20 2023-03-07 breakfast
1 10 2022-03-06 lunch
----------------------------------------



>> summarizeYears 2022


id     amount       date                    description
------------------------------------------------------------------------------------------
2 15 2022-06-03 dinner
1 10 2022-03-06 lunch
----------------------------------------



>> summarizeYears 2
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> summarizeMonths 3
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> summarizeDates


id     amount       date                    description
------------------------------------------------------------------------------------------
3 20 2023-03-07 breakfast
2 15 2022-06-03 dinner
1 10 2022-03-06 lunch
----------------------------------------



>> print
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> delete 3
----------------------------------------



>> show


id     amount       date                    description
------------------------------------------------------------------------------------------
1 10 2022-03-06 lunch
2 15 2022-06-03 dinner
----------------------------------------



>> delete 1
----------------------------------------



>> show


id     amount       date                    description
------------------------------------------------------------------------------------------
2 15 2022-06-03 dinner
----------------------------------------



>> gksafhdsk
['gksafhdsk']  is not implemented
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> 
['']  is not implemented
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------

Eliora wrote the sort method.

>> show


id     amount       date                    description
------------------------------------------------------------------------------------------
1 10 2022-03-06 lunch
2 15 2022-06-03 dinner
3 20 2023-03-07 breakfast
----------------------------------------

>> summarizeMonths 03


id     amount       date                    description
------------------------------------------------------------------------------------------
3 20 2023-03-07 breakfast
1 10 2022-03-06 lunch
----------------------------------------



>> summarizeYears 2022


id     amount       date                    description
------------------------------------------------------------------------------------------
2 15 2022-06-03 dinner
1 10 2022-03-06 lunch
----------------------------------------



>> summarizeYears 2
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> summarizeMonths 3
usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions print this menu
            
----------------------------------------



>> summarizeDates


id     amount       date                    description
------------------------------------------------------------------------------------------
3 20 2023-03-07 breakfast
2 15 2022-06-03 dinner
1 10 2022-03-06 lunch
----------------------------------------

- Running Madina's methods:
PS C:\Users\madin\Documents\github\COSI103A_TeamProject\pa03> python tracker.py
usage:
            quit
            show transactions
            add transaction: 'amount' 'date' 'description'
            delete transaction
            summarizeDates
            summarizeMonths "MM"
            summarizeYears "YYYY"
            print this menu

>> show transactions

id     amount       date                    description
------------------------------------------------------------------------------------------
2 15 2022-06-03 dinner
----------------------------------------

>> add 10.0 2022-03-05 Groceries
----------------------------------------



>> show transactions


id     amount       date                    description
------------------------------------------------------------------------------------------
2 15 2022-06-03 dinner
3 10 2022-03-05 Groceries
----------------------------------------



>> delete 3
----------------------------------------


>> show transactions


id     amount       date                    description
------------------------------------------------------------------------------------------
2 15 2022-06-03 dinner
----------------------------------------


