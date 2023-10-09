from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(15):
            print("Hello")
            sleep(2)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(2)
t1=hello()
t2=hi()
t1.start()
t2.start()
