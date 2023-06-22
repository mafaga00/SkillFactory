import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_duplicat_name(go_to_my_pets):
    """Проверяем что на странице у всех питомцев разные имена"""

    # Настраиваем неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Сохраняем в переменную names элементы с атрибутом
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td[1]')))
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    # Проверяем, что в списке нет повторяющихся имен
    names_lst = [name.text for name in names]

    assert len(names) == len(set(names_lst)), "Присутствуют питомцы с одним именем"
