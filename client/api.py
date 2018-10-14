import ssl
import urllib.request

class api:
    _ctx = ssl.create_default_context()
    _ctx.check_hostname = False
    _ctx.verify_mode = ssl.CERT_NONE
    
    _last_s = None
    _last_r = None
    _last = None

    @classmethod
    def get(cls, sender, recip):
        if sender == cls._last_s and recip == cls._last_r:
            return cls._last
        cls._last_s = sender
        cls._last_r = recip
        p = 'http://pureproof.org/api/{0}/{1}'.format(sender, recip)
        try:
            cls._last = int(urllib.request.urlopen(p, context=cls._ctx).read())
        except Exception:
            cls._last = None
        return cls._last
