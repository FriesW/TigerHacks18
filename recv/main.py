from recv import Fetcher
from time import sleep

def cls():
    print('\n'*100)

def limit(length, string):
    string = string.replace('\n', '')
    string = string.replace('\r', '')
    if len(string) > length:
        string = string[:length-3] + '...'
    return string

def pow_format(pow):
    if pow == None:
        return 'plain'
    if pow == True:
        return 'Success'
    if pow == False:
        return 'FAILURE'

fs = '| {:<32}  {:^7} | {:<18} | {:<26} | {:<34} |'

f = Fetcher()

header = fs.format('Sender', 'PoW', 'Subject', 'Date', 'Body')

try:
    while True:
        d = f.fetch()
        cls()
        print( header )
        print ( '|' + ('-' * (len(header) - 2)) + '|')
        for e in d:
            print( fs.format(limit(32,e.sender), pow_format(e.pow), limit(18,e.subject), limit(26, str(e.date)), limit(34,e.body) ) )
        sleep(10)
finally:
    f.close()