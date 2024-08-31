from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies_button = (By.XPATH, '//button[contains(text(), "Accept")]')
        self.name_input = (By.NAME, 'name')
        self.gender_select = (By.NAME, 'gender')
        self.birth_month_select = (By.NAME, 'birth_monthday')
        self.birth_year_input = (By.NAME, 'birth_year')
        self.death_month_select = (By.NAME, 'death_monthday')
        self.death_year_input = (By.NAME, 'death_year')
        self.match_exact_name_radio = (By.ID, 'name_matching_exact')
        self.search_button = (By.XPATH, '//button[@type="submit"]')

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_cookies_button)).click()
        except Exception as e:
            print("No cookies acceptance button found or clickable:", e)

    def enter_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)

    def select_gender(self, gender):
        gender_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.gender_select))
        Select(gender_element).select_by_visible_text(gender)

    def select_birth_month(self, month):
        birth_month_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birth_month_select))
        Select(birth_month_element).select_by_visible_text(month)

    def enter_birth_year(self, year):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birth_year_input)).send_keys(year)

    def select_death_month(self, month):
        death_month_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_month_select))
        Select(death_month_element).select_by_visible_text(month)

    def enter_death_year(self, year):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_year_input)).send_keys(year)

    def select_exact_name_match(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.match_exact_name_radio)).click()

    def click_search(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()
