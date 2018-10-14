from sanic import response
from functools import wraps
import hashlib
from itsdangerous import Signer
from os import urandom

dangerous = Signer(urandom(32))

SEED = b'\x06\x10\x0c?M\xa5u\x1c\x1e\x8d\x8b\xae-"\x86u' #Should be secret, but whatever

USERS = dict()
USERS['tigerhacks2018Alpha@outlook.com'] = b'\xe2\xac-#:\x1f\xdfaPz\xdb\x8e\x11(\xf4\x86.\x9f\xf3Qg\xd2%\xc5vy\x96\x942\x97\xe5s'

STATE = dict()

def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            # run some method that checks the request
            # for the client's authorization status
            try:
                c = request.cookies.get('auth').encode()
                print(c)
                dangerous.unsign(c)
                is_authorized = True
            except:
                is_authorized = False

            if is_authorized:
                # the user is authorized.
                # run the handler method and return the response
                return await f(request, *args, **kwargs)
            else:
                # the user is not authorized.
                return response.text('not authorized', 403)
        return decorated_function
    return decorator

def attach(sanic):
    
    sanic.static('/', 'web_assets/login.html')
    sanic.static('/login.css', 'web_assets/login.css')
    
    @sanic.route('/login', methods=['POST','GET'])
    async def login(request):
        fu = request.form.get('username')
        fp = request.form.get('password')
        if fu == None or fp == None:
            return response.redirect('/', status=303)
        h = hashlib.sha256()
        h.update(fp.encode())
        hp = h.digest()
        if fu in USERS:
            if USERS[fu] == hp:
                res = response.redirect('/account', status=303)
                res.cookies['auth'] = dangerous.sign(b'auth').decode()
                return res
        return response.redirect('/', status=303)
    
    @sanic.route('/account')
    @authorized()
    async def account(request):
        return response.text('here we are',200)
    
    @sanic.route('/account/update')
    @authorized()
    async def update(request):
        return response.text('hmmmm....')
    
    @sanic.route('/api/<sender>/<recip>')
    async def api(request, sender, recip):
        print(sender, recip)
        if recip in STATE:
            r = STATE[recip]
            if sender in r:
                return response.text(r[sender])
        h = hashlib.sha256()
        h.update(SEED)
        h.update(sender.encode())
        h.update(recip.encode())
        hd = h.digest()
        c = hd[0] + hd[1] + hd[2]
        c = (c%20)+10
        return response.text(str(c))
        
        
