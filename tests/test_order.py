import allure
import pytest
from data import Data
from helpers import Helper
from pages import base_page
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls

@allure.title("Тест успешного создания заказа")
class TestOrder:

    def test_order_via_top_button(self,driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.open()
        order_page = OrderPage(driver)

        # Act
        main_page.click_on_top_button_order()
        order_page.customer_data_entry(Data.NAME_FIRST, Data.SURNAME_FIRST, Data.ADDRESS_FIRST, Helper.generate_phone_number())
        order_page.order_data_entry(Data.CALENDAR_FIRST, Data.PERIODS_FIRST)
        order_page.order_confirmation()
        order_popup = order_page.order_window()

        # Assert
        assert order_popup.is_displayed(), "Order confirmation popup did not appear."

    def test_order_via_bottom_button(self,driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.open()
        order_page = OrderPage(driver)

        # Act
        main_page.click_on_bottom_button_order()
        order_page.customer_data_entry(Data.NAME_SECOND, Data.SURNAME_SECOND, Data.ADDRESS_SECOND, Helper.generate_phone_number())
        order_page.order_data_entry(Data.CALENDAR_SECOND, Data.PERIODS_SECOND)
        order_page.order_confirmation()
        order_popup = order_page.order_window()

        # Assert
        assert order_popup.is_displayed(), "Order confirmation popup did not appear."


    def test_button_logo_scooter(self,driver):
        # Arrange
        order_page = OrderPage(driver)
        order_page.open()
        # Act
        order_page.click_on_logo_scooter()
        order_page.switch_to_last_tab()
        # Assert
        assert order_page.wait_url_changed_page_first()


    def test_button_logo_yandex(self,driver):
        # Arrange
        order_page = OrderPage(driver)
        order_page.open()
        # Act
        order_page.click_on_logo_yandex()
        order_page.switch_to_last_tab()
        # Assert
        assert order_page.wait_url_changed_to_dzen()