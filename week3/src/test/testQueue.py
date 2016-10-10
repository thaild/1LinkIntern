import threading
import Queue
import time
import os
import json

exitflag = 0

class myThread(threading.Thread):
    def __init__(self, file_list, event, q):
        threading.Thread.__init__(self)
        self.file_list = file_list
        self.event = event

    def run(self):
        print "start "+self.name
        self.file_list = os.listdir("../data/DIEM_THI_2016/")
        process_data(self.file_list)
        print "end"+self.name

def process_data(file_list):
    data_import = []
    fo = open("../input.json", "w+")
    while not exitflag:
        queueLock.acquire()
        if not workQueue.empty():

            queueLock.release()
            for i in range(file_list.__len__()):
                file_input = open("../data/DIEM_THI_2016/"+file_list[i]).read()
                data_import.append(json.loads(file_input))

            fo.write(json.dumps(data_import))
            time.sleep(1)
            fo.close()
        else:
            queueLock.release()
        time.sleep(1)

threadList =  ["thread-1", "thread-2", "thread-3"]
nameList = ["one", "two", "three", "four", "five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

for tname in threadList:
    thread = myThread(threadID, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
# Dien vao queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Doi den khi queue la trong
while not workQueue.empty():
    pass

# Thong bao cho thread do la thoi gian de ket thuc
exitFlag = 1

# Doi cho tat ca thread ket thuc
for t in threads:
    t.join()
print "Ket thuc Main Thread"


