from selenium.webdriver.common.by import By

class MainPageLocators:
    def get_question(self, text):
        return By.XPATH, f"//div[text()='{text}']"

    def get_answer(self, text):
        return By.XPATH, f"//p[text()='{text}']"


    TOP_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g']"
    BOTTOM_BUTTON = By.XPATH,"//button[contains(@class,'Button_UltraBig__UU3Lp') and (text()='Заказать')]"