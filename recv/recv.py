import imaplib

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
        print('======== MESSAGE ========')
        lines = data[0][1].split(NL)
        for l in lines:
            if l.startswith(b'Received:'):
                print(l)


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