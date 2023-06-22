import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_pet_photo(go_to_my_pets):
    """Поверяем что на странице хотя бы у половины питомцев есть фото"""

    # Настраиваем неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Сохраняем в переменную statistic элементы статистики
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    statistic = pytest.driver.find_element(By.CSS_SELECTOR, ".\\.col-sm-4.left").text.split('\n')[1]

    # Получаем количество питомцев из данных статистики
    number = int(statistic.split(' ')[1])

    # Находим половину от количества питомцев
    half = number // 2

    # Сохраняем в переменную images элементы с атрибутом img
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover img')))
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Находим кол-во питомцев с фотографией
    photo_count = [image for image in range(len(images)) if images[image].get_attribute('src')]

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert len(photo_count) >= half, "У большинства питомцев отсутствует фото"
