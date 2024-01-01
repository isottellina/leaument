from starlette.templating import Jinja2Templates
from leaument.constants import DAY_VALUES

from leaument.converter import RepublicanDate

def format_day_value(name, href, gender) -> str:
    link = f'<a href="https://fr.wikipedia.org{href}"/>{name}</a>'
    
    if name[0].lower() in ["a", "e", "é", "è", "i", "o", "u", "y"]:
        return f"de l'{link}"
    elif gender == "M":
        return f"du {link}"
    elif gender == "F":
        return f"de la {link}"

def day_value(date: RepublicanDate) -> str:
    value = DAY_VALUES[date.month - 1][date.day - 1]
    return format_day_value(value["name"], value["href"], value["gender"])

TEMPLATES = Jinja2Templates(directory="templates")
TEMPLATES.env.filters["day_value"] = day_value
