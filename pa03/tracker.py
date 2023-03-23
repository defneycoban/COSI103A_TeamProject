# All printing should be done in this class. Sql commands go in transactions.py
import sys


def read_eval():
    ''' reads and evaluates input '''
    if len(sys.argv) == 1:
        # no arguments passed
        # print_usage() (Madina's method)
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
