from bs4 import BeautifulSoup
import requests
import json
import os


def scrape_spells():
    url = "https://www.pojo.com/harry-potter-spell-list/"
    req = requests.get(url)
    response = req.text
    print(f"P{req}")
    soup = BeautifulSoup(response, features='html.parser')
    table = soup.findChild("table")
    rows = table.findChildren("tr")

    spells_file = open(os.path.join(os.curdir, "../data/spells.json"), "w")
    data = {"spells": []}
    for row in rows[2:]:
        cells = row.findChildren('td')
        if cells[0].string != "—":
            data["spells"].append({"incantation": cells[0].string, "type": cells[1].string, "effect": cells[2].string})
            print(f"Learning spell: {cells[0].string}")
    json.dump(data, spells_file, indent=4)
    return req.status_code


scrape_spells()
