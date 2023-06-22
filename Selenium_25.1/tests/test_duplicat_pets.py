import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_duplicate_pets(go_to_my_pets):
    """Поверяем что на странице нет повторяющихся питомцев"""

    # Настраиваем неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Сохраняем в переменную data_my_pets элементы с данными о питомцах
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    data_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Проверяем, что в списке нет повторяющихся питомцев:
    pet_list = [i.text.replace('\n×', '') for i in data_my_pets]

    assert len(pet_list) == len(set(pet_list)), "Присутствуют одинаковые питомцы"
