# coding=utf-8
import thread
import time
import threading

# use thread to create
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#
# try:
#     thread.start_new_thread(print_time, ("Thread-1", 2,))
#     thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print "Error: unable to start thread"
#
# while 1:
#     pass

exitFlag = 0

# use threading to create
class MyThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


thread1 = MyThread(1, "Thread - 1", 1)
thread2 = MyThread(2, "Thread - 2", 2)

thread1.start()
thread2.start()

print "Exiting Main Thread"
