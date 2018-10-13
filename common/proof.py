from time import time
import hashlib
from os import urandom
import base64

class _Tester:
    def __init__(self, diff):
        self.zeros = diff//8
        self.last_bit = int('1'*(8 - diff%8), 2)
    
    def _hash_test(self, *args):
        m = hashlib.sha256()
        for i in args:
            m.update(i)
        h = m.digest()
        for i in range(self.zeros):
            if h[i] != 0:
                return False
        if h[self.zeros] <= self.last_bit:
            return True
        return False

def check(diff, header, delta_max=60):
    if type(diff) != int:
        raise TypeError()
    if diff < 0:
        raise ValueError()
    if type(header) != bytes:
        raise TypeError()
    
    starting, creation_time, b64_nonce = header.split(b';')
    if abs(time() - int(creation_time)) > delta_max:
        return False
    t = _Tester(diff)
    return t._hash_test(starting, creation_time, base64.b64decode(b64_nonce))
    

def pow(diff, starting = b''):
    if type(diff) != int:
        raise TypeError()
    if diff < 0:
        raise ValueError()
    if type(starting) != bytes:
        raise TypeError()
    
    t = _Tester(diff)
    s = time()

    while True:
        creation_time = str(int(time())).encode()
        nonce = urandom(32)
        if t._hash_test(starting, creation_time, nonce):
            break

    e = time()
    print( 'Took:', e-s, 'seconds')
    return b';'.join((starting, creation_time, base64.b64encode(nonce)))
