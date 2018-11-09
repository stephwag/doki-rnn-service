from aiohttp import web
import asyncio
import aiohttp
from textgenrnn import textgenrnn

routes = web.RouteTableDef()
t = textgenrnn('renpy_script_ddlc.hdf5')
rate = 1

@routes.get('/')
async def hello(request):
    if 'temp' in request.rel_url.query:
        temp = float(request.rel_url.query['temp'])
    else:
        temp = 1.0

    sentences = t.generate(rate, temperature=temp, return_as_list=True)
    return web.Response(text="\n".join(sentences))

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8081)
