import os
from src import spell_scraper as sc


def test_scraper(tmp_path):
    assert sc.scrape_spells(os.path.join(tmp_path, "spells.json")) == 200, "Did not retrieve spells correctly"
