from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_INPUT = By.XPATH, "//input[@placeholder='* Станция метро']"
    DROPDOWN_CLASS = (By.CLASS_NAME, 'select-search__select')
    PHONE_NUMBER = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    def get_calender(self, text):
        return By.XPATH, f"//div[@aria-label='{text}']"

    ORDER_DATE_INPUT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    ORDER_PERIOD_INPUT = By.XPATH, "//div[text()='* Срок аренды']"

    def get_period(self, text):
        return By.XPATH, f"//div[text()='{text}']"

    BUTTON_ORDER = By.XPATH, "//button[contains(@class,'Button_Middle__1CSJM') and (text()='Заказать')]"

    BUTTON_ORDER_CONFIRMATION = By.XPATH, "//button[text()='Да']"

    ORDER_WINDOW = (By.CLASS_NAME, 'Order_Modal__YZ-d3')

    LOGO_SCOOTER = By.XPATH, "//img[@alt ='Scooter']"
    LOGO_YANDEX = By.XPATH, "//img[@alt ='Yandex']"
