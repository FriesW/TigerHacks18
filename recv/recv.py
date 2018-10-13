import imaplib
import email.parser
import email.utils

IMAP_SERVER = 'outlook.office365.com'
EMAIL_ACCOUNT = 'tigerhacks2018Alpha@outlook.com'
EMAIL_FOLDER = 'inbox'
PASSWORD = '9El%wSC73^kO'

NL = b'\r\n'

def list_mb(m):
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
        print('======== MESSAGE ========')
        print('From:', pd.get('From'))
        print('Subject:', pd.get('Subject'))
        
        pow = pd.get('X-work-proof')
        if not pow:
            print('Proof: NONE')
        else:
            print('Proof:', pow)
        
        recv_header = pd.get('Received')
        if not recv_header:
            print('Received: MISSING')
            continue
        datetime = email.utils.parsedate_to_datetime(
            recv_header.split(';')[-1])
        if not datetime:
            print('Received: Failed to parse')
            continue
        recv_time = datetime.timestamp()
        print('Received:', datetime)
        
        
            


m = imaplib.IMAP4_SSL(IMAP_SERVER)
m.login(EMAIL_ACCOUNT, PASSWORD)
rv, data = m.select(EMAIL_FOLDER)
if rv == 'OK':
    print('OK!')
    list_mb(m)
    m.close()
else:
    print('error...')
m.logout()