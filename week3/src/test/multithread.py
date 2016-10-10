import threading
from Queue import Queue
import time



# 10 workers, 20 tasks
NUM_WORKERS = 10
NUM_JOBS = 20
start = time.time()
q = Queue()


def exampleJob(jobID):
    time.sleep(0.5)
    print(threading.currentThread().name, jobID)


def work():
    while True:
        todoJob = q.get()
        exampleJob(todoJob)
        q.task_done()


def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def create_jobs():
    for job in range(NUM_JOBS):
        q.put(job)
    q.join()

create_workers()
create_jobs()

print('Entire job took:', time.time() - start)