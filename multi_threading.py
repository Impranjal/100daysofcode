import threading
import logging
import time
import concurrent.futures
def func(name):
    logging.info("Welcome to therad automation %s",name)
    time.sleep(2)
    logging.info("Thread stopped %s",name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("starting")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as exec:
        exec.map(func,range(3))