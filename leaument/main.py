from starlette.applications import Starlette
from starlette.routing import Route

from leaument.templates import TEMPLATES


async def index(request):
    return TEMPLATES.TemplateResponse(request, "index.html")


app = Starlette(
    routes=[
        Route("/", index),
    ]
)
