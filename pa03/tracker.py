# All printing should be done in this class. Sql commands go in transactions.py
import sys
from transactions import Transactions

# Eliora's method
def process(arglist):
    ''' examine args and make appropriate calls to the database'''
    transaction = Transactions('transactions.db')
    if arglist==[]: #if no arguments are passed, print the options
        print_usage()
    elif arglist[0]=="quit":
        quit()
    elif arglist[0]=="show":
        print_transactions(transaction.show_transactions())
    elif arglist[0]=='add':
        if len(arglist)!=4: #because there are 3 fields that must be added each time
            print_usage()
        else:
            dict_name = {'amount':arglist[1],'date':arglist[2],'description':arglist[3]}
            transaction.add(dict_name)
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            transaction.delete(arglist[1])
    elif arglist[0]=="summarizeDates":
        print_transactions(transaction.sort('dates'))
    elif arglist[0]=="summarizeMonths":
        if len(arglist)!=2:    #user must input a month
            print_usage()
        if len(arglist[1])!=2 : #user must input a month in the correct format
            print_usage()
        else:
            print_transactions(transaction.sort(arglist[1]))
    elif arglist[0]=="summarizeYears":
        if len(arglist)!=2:    #user must input a year
            print_usage()
        if len(arglist[1])!=4:   #user must input a year in the correct format
            print_usage()
        else:
            print_transactions(transaction.sort(arglist[1]))
    elif arglist[0]=="print":
        print_usage()
    else:   #if the user inputs something that is not an option
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
    print("%s %s %s "%('amount','date','description'))
    print('-'*90)
    for item in transactions:
        values = tuple(item.values()) #(item, amount, date, category, description)
        print("%s %s %s"%values)

# Created by Zev
def read_eval():
    ''' reads and evaluates input '''
    if len(sys.argv) == 1: # no arguments passed
        print_usage()
        args = []
        while args != ['']:
            args = input('>> ').split(' ')
            # if args[0] == 'add':
            #     # join everything after the "add" keyword
            #     args = ['add', args[1], ' '.join(args[2:])]
            process(args)
            print('-' * 40 + '\n' * 3)
    else:
        #read and process args
        args = sys.argv[1:]
        process(args)
        print('-' * 40 + '\n' * 3)

read_eval()