from sanic import response
import hashlib
from itsdangerous import Signer
from os import urandom

dangerous = Signer(urandom(32))

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
                c = request.cookies.get('auth')
                print(c)
                dangerous.unsign(c)
                is_authorized = True
            except:
                is_authorized = False

            if is_authorized:
                # the user is authorized.
                # run the handler method and return the response
                response = await f(request, *args, **kwargs)
                return response
            else:
                # the user is not authorized.
                return response.text('not authorized', 403)
        return decorated_function
    return decorator

def attach(sanic):
    
    sanic.static('/', 'web_assets/login.html')
    sanic.static('/login.css', 'web_assets/login.css')
    
    @sanic.route('/login', methods=['POST'])
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
                res.cookies['auth'] = dangerous.sign(b'auth')
                return res
        return response.redirect('/', status=303)
    
    @sanic.route('/account')
    @authorized()
    async def account(request):
        return request.text('here we are',200)
        
