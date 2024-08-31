import pytest
from selenium import webdriver
from imdb_search_page import IMDbSearchPage  # Import the IMDbSearchPage class

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_imdb_search(driver):
    driver.get("https://www.imdb.com/search/name/")
    search_page = IMDbSearchPage(driver)
    
    # Accept cookies
    search_page.accept_cookies()
    
    # Fill in the search form with some sample data
    search_page.enter_name("Brad Pitt")
    search_page.select_gender("Male")
    search_page.select_birth_month("December")
    search_page.enter_birth_year("1963")
    search_page.select_death_month("January")
    search_page.enter_death_year("2023")
    search_page.select_exact_name_match()
    
    search_page.click_search()

    # Add assertions to verify the search results, for now we just print the page title
    assert "Name Search" in driver.title

if __name__ == "__main__":
    pytest.main()
