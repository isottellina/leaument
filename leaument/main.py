from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route
from starlette.responses import Response
from datetime import date
from leaument.converter import RepublicanDate

from leaument.templates import TEMPLATES
from pydantic import BaseModel, ValidationError
from leaument.constants import CALENDER_BEGINNING


async def index(request: Request):
    return TEMPLATES.TemplateResponse(request, "index.html")


class RepublicanDayRequest(BaseModel):
    date: date


async def republican_day(request: Request):
    form_data = await request.form()
    try:
        parsed_data = RepublicanDayRequest.model_validate(form_data)
    except ValidationError:
        return Response("Bad date", status_code=422)

    if parsed_data.date < CALENDER_BEGINNING:
        return Response("Dates before September 22nd, 1792 are not valid", status_code=422)

    republican_date = RepublicanDate.from_gregorian(parsed_data.date)

    return TEMPLATES.TemplateResponse(
        request, "day.html", context={"republican_date": republican_date}
    )


app = Starlette(
    routes=[
        Route("/", index, methods=["GET"]),
        Route("/day", republican_day, methods=["POST"]),
    ]
)
