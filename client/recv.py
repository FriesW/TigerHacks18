import imaplib
import email
import email.parser
import email.utils
from collections import namedtuple
import re

import proof

_email = namedtuple('Email',['sender','subject','date','body','pow'])

IMAP_SERVER = 'outlook.office365.com'
EMAIL_ACCOUNT = 'tigerhacks2018Alpha@outlook.com'
EMAIL_FOLDER = 'inbox'
PASSWORD = '9El%wSC73^kO'

def _list_mb(m):
    out = []
    rv, data = m.search(None, 'ALL')
    if rv != 'OK':
        print('list error...')
        return
    for n in data[0].split():
        rv, data = m.fetch(n, '(RFC822)')
        if rv != 'OK':
            print('iter error...')
            return
        raw = data[0][1]
        hp = email.parser.BytesParser()
        pd = hp.parsebytes(raw)
        
        pow = pd.get('X-work-proof')
        
        recv_header = pd.get('Received')
        if not recv_header:
            continue
        datetime = email.utils.parsedate_to_datetime(
            recv_header.split(';')[-1])
        if not datetime:
            print('Received: Failed to parse')
            continue
        recv_time = datetime.timestamp()
        
        pow_status = None
        if pow:
            pow_status = proof.check(20, EMAIL_ACCOUNT, pow.encode(), recv_time)
        body = ''
        b = email.message_from_string(raw.decode())
        p = b.get_payload()
        if type(p) != str:
            for payload in p:
                body += payload.get_payload()
        else:
            body = p
        rep = re.compile(r'<.*?>')
        body = rep.sub('', body)
        out.append( _email(pd.get('From'), pd.get('Subject'), datetime, body, pow_status) )
    
    out.reverse()
    return out

class Fetcher:
    def __init__(self):
        self.m = imaplib.IMAP4_SSL(IMAP_SERVER)
        self.m.login(EMAIL_ACCOUNT, PASSWORD)
        self.c = False
    def fetch(self):
        if self.c:
            return
        rv, data = self.m.select(EMAIL_FOLDER)
        if rv == 'OK':
            return _list_mb(self.m)
        self.c = True
        print('error...')
        return
    def close(self):
        try:
            self.c = True
            self.m.close()
            self.m.logout()
        except:
            pass

            
            
            
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

def build_option():
    fs = '{:<32}  {:^7} | {:<18} | {:<26} | {:<34}' 
    f = Fetcher()
    d = f.fetch()
    out = []
    i = 0
    for e in d:
        out.append( (fs.format(_limit(32,e.sender), _pow_format(e.pow), _limit(18,e.subject), _limit(26, str(e.date)), _limit(34,e.body) ), i ) )
        i += 1

    f.close()
    return out