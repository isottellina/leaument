import httpx, json
from bs4 import BeautifulSoup

URL = "https://fr.wikipedia.org/wiki/Calendrier_r%C3%A9publicain"

client = httpx.Client(follow_redirects=True)
data = client.get(URL).text
soup = BeautifulSoup(data, features="html.parser")
result = []


def try_to_get_gender(name: str) -> str:
    print("Trying to get gender for", name)
    try:
        wiktionary_page = client.get(f"https://fr.wiktionary.org/wiki/{name.lower()}")
        wiktionary_page.raise_for_status()
    except httpx.HTTPError:
        return "?"

    wiktionary_soup = BeautifulSoup(wiktionary_page.text, features="html.parser")
    gender = wiktionary_soup.find(class_="ligne-de-forme").text

    if gender == "masculin":
        return "M"
    elif gender == "féminin":
        return "F"
    else:
        return "?"


for month_table in soup.find_all(
    "table", style="border-spacing: 2px; border: 1px solid darkgray;"
):
    month_result = []

    for link in month_table.find_all("a"):
        month_result.append({"name": link.text, "href": link.get("href")})

    result.append(
        [
            {**day_value, "gender": try_to_get_gender(day_value["name"])}
            for day_value in month_result[2:]
        ]
    )

with open("day_values.json", "w") as fp:
    json.dump(result, fp)

__import__("pprint").pp(result)
