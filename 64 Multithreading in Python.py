'''
Multithreading in Python programming is a well-known technique in which multiple threads in a process share their data space with the main thread
 which makes information sharing and communication within threads easy and efficient. Threads are lighter than processes. Multi threads may execute
 individually while sharing their process resources. The purpose of multithreading is to run multiple tasks and function cells at the same time.


Start()	Starts the activity of a thread. It must be called only once for each thread because it will throw a runtime error if called multiple times.

join()	It blocks the execution of other code until the thread on which the join() method was called gets terminated.
'''

from time import sleep
from  threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("bye")