import requests
import threading


def solution():
    print("hola")


threads = list()

for i in range(20):
    t = threading.Thread(target=solution )
    threads.append(t)
    t.start()
