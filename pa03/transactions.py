# All sql commands should be done in this class. Print statements go in tracker.py

class Transactions():
    ''' methods for obtaining transaction data '''
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
                      (item int, amount int, date text, description text))''', ())

    def process_args(arglist):
        ''' examine args and make appropriate calls to the database'''
        transaction = Transactions()
        if arglist==[]:
          print_usage()
        elif arglist[0]=="show":
            print_todos(todolist.selectActive())
        elif arglist[0]=="showall":
            print_todos(todos = todolist.selectAll())
        elif arglist[0]=="showcomplete":
            print_todos(todolist.selectCompleted())
        elif arglist[0]=='add':
            if len(arglist)!=3:
                print_usage()
            else:
                todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
                todolist.add(todo)
        elif arglist[0]=='complete':
            if len(arglist)!= 2:
                print_usage()
            else:
                todolist.setComplete(arglist[1])
        elif arglist[0]=='delete':
            if len(arglist)!= 2:
                print_usage()
            else:
                todolist.delete(arglist[1])
        else:
            print(arglist,"is not implemented")
            print_usage()