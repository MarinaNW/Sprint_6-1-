from time import sleep

from selenium.common import TimeoutException

from data import Data
from locators.OrderPageLocators import OrderPageLocators
from pages.base_page import BasePage
from urls import Urls


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def open(self):
        self.get(Urls.ORDER_URL)

    def customer_data_entry(self, name, surname, address, phone_number):
        self.fill_input(self.locators.NAME_INPUT,name)
        self.fill_input(self.locators.SURNAME_INPUT,surname)
        self.fill_input(self.locators.ADDRESS_INPUT,address)
        self.click_on_element(self.locators.METRO_INPUT)
        self.click_on_element(self.locators.DROPDOWN_CLASS)
        self.fill_input(self.locators.PHONE_NUMBER, phone_number)
        self.click_on_element(self.locators.BUTTON_NEXT)

    def order_data_entry(self, calender_text,period_text):
        self.click_on_element(self.locators.ORDER_DATE_INPUT)
        calender_locator = self.locators.get_calender(calender_text)
        self.click_on_element(calender_locator)
        self.click_on_element(self.locators.ORDER_PERIOD_INPUT)
        period_locator = self.locators.get_period(period_text)
        self.click_on_element(period_locator)
        self.click_on_element(self.locators.BUTTON_ORDER)

    def order_confirmation(self):
        self.click_on_element(self.locators.BUTTON_ORDER_CONFIRMATION)

    def order_window(self):
        return self.find_element(self.locators.ORDER_WINDOW)

    def click_on_logo_scooter(self):
        self.click_on_element(self.locators.LOGO_SCOOTER)

    def wait_url_changed_page_first(self):
        return self.wait_url_changed(Urls.ORDER_URL)

    def wait_url_expected_page(self):
        return self.wait_expected_url(Urls.BASE_URL)

    def click_on_logo_yandex(self):
        self.click_on_element(self.locators.LOGO_YANDEX)

    def wait_url_changed_page_second(self):
        return self.wait_url_changed(Urls.ORDER_URL)

    def wait_url_changed_to_dzen(self):
        return self.wait_expected_url(Urls.DZEN_URL)

    def wait_last_page(self):
        self.switch_to_last_tab()