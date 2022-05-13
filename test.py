import logging
import sys

from aiohttp import web

import aiocqhttp
from aiocqhttp import CQHttp

logging.getLogger("aiocqhttp").setLevel(logging.DEBUG)
l = logging.StreamHandler(sys.stdout)
l.setLevel(logging.DEBUG)
logging.getLogger("aiocqhttp").addHandler(l)
logging.getLogger("aiohttp.web").setLevel(logging.DEBUG)
logging.getLogger("aiohttp.web").addHandler(l)
cqhttp = CQHttp()

@cqhttp.on_message()
async def _(event):
    print(event)


cqhttp._server_app.add_routes([
    web.post('/', cqhttp._handle_http_event),
    web.get('/ws/', cqhttp._handle_wsr),
    web.get('/ws/event/', cqhttp._handle_wsr),
    web.get('/ws/api/', cqhttp._handle_wsr),
    ])

for i in cqhttp.server_app.router.items():
    print(1, i)

cqhttp.run()

