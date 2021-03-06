from aiohttp import web
import aiohttp_jinja2
import jinja2

from settings import BASE_DIR, config
from routes import setup_routes
from db import pg_context


app = web.Application()
setup_routes(app)
app['config'] = config
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')))
app.cleanup_ctx.append(pg_context)
web.run_app(app)
