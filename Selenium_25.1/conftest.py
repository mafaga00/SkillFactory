import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def start_pet_friends():
    pytest.driver = webdriver.Chrome('/driver/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()


@pytest.fixture()
def go_to_my_pets():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

    # Проверяем наличие корректного URL
    current_url = pytest.driver.current_url
    assert current_url == "https://petfriends.skillfactory.ru/my_pets"
