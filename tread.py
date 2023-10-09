import threading

def hello():
    for i in range(1,11):
        print("Hello")

def hi():
    for i in range(1,6):
        print("Hi")
        
def test():
    for i in range(1,3):
        print("test")
th1=threading.Timer(3,hello)
th1.start()
th1.join()
th2=threading.Timer(3,hi)
th2.start()
th3=threading.Timer(3,test)
th3.start()
#hello()
#hi()
#test()
