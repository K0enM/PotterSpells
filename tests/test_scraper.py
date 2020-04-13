from src import spell_scraper as sc

def test_scraper():
    assert sc.scrape_spells() == 200, "Did not retrieve spells correctly"