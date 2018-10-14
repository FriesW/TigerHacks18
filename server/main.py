from sanic import Sanic
from sanic import response
import asyncio
import uvloop
from signal import signal, SIGINT

import app

ssl_c = None

upgrade = Sanic('upgrade')
main = Sanic('main')

@upgrade.route('/')
@upgrade.route('/<path:path>')
async def reroute(request, path=''):
    return response.redirect(request.url.replace('http://','https://',1),         status=301)

app.attach(main)
    
asyncio.set_event_loop(uvloop.new_event_loop())

if ssl_c != None:
    srv_upgrade = upgrade.create_server(host='0.0.0.0', port=80)
    srv_main = main.create_server(host='0.0.0.0', port=443, ssl = ssl_c)
else:
    srv_main = main.create_server(host='0.0.0.0', port=80)

loop = asyncio.get_event_loop()

if ssl_c != None:
    asyncio.ensure_future(srv_upgrade)
asyncio.ensure_future(srv_main)

signal(SIGINT, lambda s, f: loop.sop())
try:
    loop.run_forever()
except:
    loop.stop()
