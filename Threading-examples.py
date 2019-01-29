import threading
from time import sleep
import os

db = {}

def helloAllTennisLovers(name):
    for i in range(10):
        print ('Hello All dear Tennis Lovers from : ',os.getpid(),threading.current_thread().name)
        db[i] = threading.current_thread().name
        sleep(2)

def helloAllCricketLovers(name):
    for i in range(10,20):
        print ('Hello all dear Cricket Lovers : ', os.getpid(), threading.current_thread().name)
        db[i] = threading.current_thread().name
        sleep(2)

if __name__ == "__main__":
    t1 = threading.Thread(target=helloAllCricketLovers, args=('abc',))
    t2 = threading.Thread(target=helloAllTennisLovers, args=('def',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print (db)