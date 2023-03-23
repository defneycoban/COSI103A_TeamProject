# All printing should be done in this class. Sql commands go in transactions.py


def process(arglist):
    ''' examine args and make appropriate calls to the database'''
    transaction = Transactions()
    if arglist==[]:
        #not implemented yet: print_usage() in tracker.py
        print("placeholder")
    elif arglist[0]=="quit":
        quit()
    elif arglist[0]=="show":
        #not implemented yet: print_transactions(transaction.show()) in tracker.py, transaction.show() in transactions.py
        print("placeholder")
    elif arglist[0]=='add':
        if len(arglist)!=5: #because there are 5 fields
            #not implemented yet: print_usage() in tracker.py
            print("placeholder")
        else:
            dictName = {'item #':arglist[1],'amount':arglist[2],'category':arglist[3],'date':arglist[4],'description':arglist[5]} in tracker.py #dictName in transactions.py
            #not implemented yet: transaction.add(dictName) in transactions.py, dictName in transactions.py
            print("placeholder")
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            #not implemented yet: print_usage() in tracker.py
            print("placeholder")
        else:
            #not implemented yet: transaction.delete(arglist[1]) in transactions.py
            print("placeholder")
    elif arglist[0]=="summarizeDates":
        #not implemented yet: print_transactions(dictName = transaction.sort(date)) in tracker.py, transaction.select() in transactions.py, dictName in transactions.py
        print("placeholder")
    elif arglist[0]=="summarizeMonths":
        #not implemented yet: print_transactions(dictName = transaction.sort(month)) in tracker.py, transaction.select() in transactions.py, dictName in transactions.py
        print("placeholder")
    elif arglist[0]=="summarizeYears":
        #not implemented yet: print_transactions(dictName = transaction.sort(year)) in tracker.py, transaction.select() in transactions.py, dictName in transactions.py
        print("placeholder")
    elif arglist[0]=="print":
        #not implemented yet: print_usage() in tracker.py
        print("placeholder")
    else:
        print(arglist," is not implemented")
        #not implemented yet: print_usage() in tracker.py