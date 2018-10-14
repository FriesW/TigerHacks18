from sanic import response
import hashlib

USERS = dict()
USERS['tigerhacks2018Alpha@outlook.com'] = b'\xe2\xac-#:\x1f\xdfaPz\xdb\x8e\x11(\xf4\x86.\x9f\xf3Qg\xd2%\xc5vy\x96\x942\x97\xe5s'

STATE = dict()

def attach(sanic):
    
    sanic.static('/', 'web_assets/login.html')
    sanic.static('/login.css', 'web_assets/login.css')
    
    @sanic.route('/login', methods=['POST'])
    async def login(request):
        fu = request.form.get('username')
        fp = request.form.get('password')
        if fu == None or fp == None:
            return respoonse.redirect('/', status=307)
        h = hashlib.sha256()
        h.update(fp.encode())
        hp = h.digest()
        if fu in USERS:
            if USERS[fu] == hp:
                res = response.redirect('/account', status=307)
                res.cookies['test'] ='yoho'
                return res
        return response.redirect('/', status=307)
        
