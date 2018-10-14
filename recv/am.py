#import sys
#sys.path.append('.')
from . import recv

def _limit(length, string):
    string = string.replace('\n', '')
    string = string.replace('\r', '')
    if len(string) > length:
        string = string[:length-3] + '...'
    return string

def _pow_format(pow):
    if pow == None:
        return 'plain'
    if pow == True:
        return 'Success'
    if pow == False:
        return 'FAILURE'

fs = '{:<32}  {:^7} | {:<18} | {:<26} | {:<34}'

def am_get():
    f = recv.Fetcher()

    out = []

    i = 0
    for e in d:
        out.append( (fs.format(_limit(32,e.sender), _pow_format(e.pow), _limit(18,e.subject), _limit(26, str(e.date)), _limit(34,e.body) ), i ) )
        i += 1

    f.close()
    return out