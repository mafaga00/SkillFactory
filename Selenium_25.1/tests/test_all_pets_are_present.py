import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_are_present(go_to_my_pets):
    """Проверяем что на странице присутствуют все питомцы."""

    # Настраиваем неявные ожидания
    pytest.driver.implicitly_wait(10)

    # Сохраняем в переменную statistic нужный элемент статистики
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    statistic = pytest.driver.find_element(By.CSS_SELECTOR, ".\\.col-sm-4.left").text.split('\n')[1]

    # Получаем количество питомцев из данных статистики
    number = int(statistic.split(' ')[1])

    # Сохраняем в переменную pets элементы карточек питомцев
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    assert number == len(pets), "Ошибка в статистике питомцев"
