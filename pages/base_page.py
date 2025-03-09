from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.driver.maximize_window()

    def get(self, url):
        self.driver.get(url)

    def scroll_to_the_element(self,locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator )

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # def hide_overlaying_element(self):
    #     overlaying_element = self.driver.find_element_by_xpath('//img[@src="/assets/scooter.png"]')
    #     if overlaying_element:
    #         for element in overlaying_element:
    #             self.driver.execute_script('arguments[0].style.display = "none";', element)

    def js_click_on_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def fill_input(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_to_be_visible(self,locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_to_be_clickable(self,locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def scroll_and_find_the_element(self, locator):
        # Сначала находим элемент по локатору
        element = self.find_element(locator)
        # Затем выполняем прокрутку до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def сlick_on_the_input_field(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def wait_expected_url(self,url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def wait_url_changed(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_changes(url))

    #@allure.step("Переключение на последнюю открытую вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
