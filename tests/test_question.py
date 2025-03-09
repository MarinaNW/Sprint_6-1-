import allure
import pytest
from data import Data
from pages.main_page import MainPage

@allure.title("Тест открытия вопроса с соответствующим ответом")
@pytest.mark.parametrize("question_text, question_answer", Data.QUESTIONS_ANSWER)
def test_questions(driver, question_text, question_answer):
    #Arrange
    main_page = MainPage(driver)
    main_page.open()

    #Act
    main_page.scroll_and_click_on_question(question_text)

    #Assert
    assert main_page.find_answer(question_answer).is_displayed(), f"Текст ответа '{question_answer}' не отобразился."