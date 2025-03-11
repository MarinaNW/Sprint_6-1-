from locators.MainPageLocators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def open(self):
        self.get(Urls.BASE_URL)

    def scroll_and_click_on_question(self, question_text):
        question_locator = self.locators.get_question(question_text)
        question_element = self.wait_to_be_visible(question_locator)
        self.scroll_to_the_element(question_element)
        self.js_click_on_element(question_element)

    def find_answer(self, answer_text):
        answer_locator = self.locators.get_answer(answer_text)
        return self.wait_to_be_visible(answer_locator)

    def click_on_top_button_order(self):
        self.click_on_element(self.locators.TOP_BUTTON)

    def click_on_bottom_button_order(self):
        self.scroll_and_find_the_element(self.locators.BOTTOM_BUTTON)
        button_order = self.wait_to_be_visible(self.locators.BOTTOM_BUTTON)
        self.js_click_on_element(button_order)

    def wait_url_changed_to_main_page(self):
        return self.wait_url_changed(Urls.BASE_URL)