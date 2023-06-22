import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_there_is_a_name_age_and_breed(go_to_my_pets):
    """Поверяем что на странице у всех питомцев есть имя, возраст и порода"""

    # Настраиваем неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//tbody/tr")))
    pet_data = pytest.driver.find_elements(By.XPATH, '//tbody/tr')

    # Сохраняем в переменную names элементы с именами питомцев
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td[1]')))
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    # Сохраняем в переменную breed элементы с названиями пород питомцев
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td[2]')))
    breed = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')

    # Сохраняем в переменную age элементы с возрастом питомцев
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td[3]')))
    age = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')

    # Проверяем, что в списке у всех питомец есть имя, возраст и порода
    for i in range(len(pet_data)):
        assert names[i].text, "Отсутствует имя питомца"
        assert age[i].text, "Отсутствует возраст питомца"
        assert breed[i].text, "Отсутствует порода питомца"
