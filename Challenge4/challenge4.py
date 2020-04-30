import requests
import threading


def solution():
    response = requests.get('http://steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key')
    s = requests.session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    while response.status_code != 202:
        response = requests.get('http://steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key')
        
    resultado = response.json()

    text_file = open("Output.txt", "w")
    text_file.write(resultado['key'])
    text_file.close()

threads = list()

for i in range(2000):
    t = threading.Thread(target=solution )
    threads.append(t)
    t.start()
