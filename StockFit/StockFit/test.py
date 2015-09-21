import multiprocessing
import time

def worker():
    while True:
        try:
            name = multiprocessing.current_process().name
            print (name, 'Running')
            i = 10/0
            time.sleep(2)
        except ZeroDivisionError:
            print("That didn't go well")
            time.sleep(2)
    

def my_service():
    while True:
        name = multiprocessing.current_process().name
        print (name, 'Running')
        time.sleep(3)

if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)

    worker_1.start()
    service.start()