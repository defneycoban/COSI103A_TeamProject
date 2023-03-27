# All printing should be done in this class. Sql commands go in transactions.py
import sys
from transactions import Transactions

# Eliora's method
def process(arglist):
    ''' examine args and make appropriate calls to the database'''
    transaction = Transactions()
    
    if arglist==[]:
        print_usage()
    elif arglist[0]=="quit":
        quit()
    elif arglist[0]=="show":
        print_transactions(transaction.show())
    elif arglist[0]=='add':
        if len(arglist)!=5: #because there are 5 fields
            print_usage()
        else:
            dictName = {'item #':arglist[1],'amount':arglist[2],'category':arglist[3],'date':arglist[4],'description':arglist[5]}
            transaction.add(dictName)
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            transaction.delete(arglist[1])
    elif arglist[0]=="summarizeDates":
        print_transactions(transaction.sort('date'))
    elif arglist[0]=="summarizeMonths":
        print_transactions(transaction.sort('month'))
    elif arglist[0]=="summarizeYears":
        print_transactions(transaction.sort('year'))
    elif arglist[0]=="print":
        print_usage()
    else:
        print(arglist," is not implemented")
        print_usage()

# Madina's method
def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transactions quit
            transactions show transactions
            transactions add transaction
            transactions delete transaction
            transactions summarize transactions by date
            transactions summarize transactions by month
            transactions summarize transactions by year
            transactions summarize transactions by category
            transactions print this menu
            '''
            )

# created by Defne
def print_transactions(transactions):
    ''' print the transaction items '''
    if len(transactions) == 0:
        print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-20s %-30s %-20s"%('item #','amount','category','date','description'))
    print('-'*90)
    for item in transactions:
        values = tuple(item.values()) #(item, amount, date, category, description)
        print("%-10s %-10s %-20s %-30s %-20s"%values)

    

# Created by Zev
def read_eval():
    ''' reads and evaluates input '''
    if len(sys.argv) == 1:
        # no arguments passed
        print_usage() 
        args = []
        while args != ['']:
            args = input('>> ').split(' ')
            if args[0] == 'add':
                # join everything after the "add" keyword
                args = ['add', args[1], ' '.join(args[2:])]
            process(args)
            print('-' * 40 + '\n' * 3)
    else:
        #read and process args
        args = sys.argv[1:]
        process(args)
        print('-' * 40 + '\n' * 3)

read_eval()


