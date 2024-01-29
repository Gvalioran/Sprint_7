import requests
import allure
import helpers
from data import Url, DataTest


@allure.story('Тесты создания курьера')
class TestCreatingCourier:

    @allure.title('Тест успешного создания курьера')
    def test_can_create_courier(self, courier):
        response = helpers.login_courier(courier["login"], courier["password"])
        assert response.status_code == 200

    @allure.title('Тест запрета создания одинаковых курьеров')
    def test_cannot_create_two_identical_couriers(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 409

    @allure.title('Тест запрета создания курьеров без заполнения логина')
    def test_creating_courier_without_login(self, courier):
        payload = {
            "login": "",
            "password": courier["password"],
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Тест запрета создания курьеров без заполнения пароля')
    def test_creating_courier_without_password(self, courier):
        payload = {
            "login": courier["login"],
            "password": "",
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Тест на правильный код ответа при создании курьера')
    def test_code_courier_creation_response(self, courier):
        assert courier["status_code"] == 201

    @allure.title('Тест сообщения успешного запроса на создание курьера')
    def test_successful_request(self, courier):
        assert courier["json"] == {'ok': True}

    @allure.title('Тест корректного ответа без заполнения логина')
    def test_absence_login_field(self, courier):
        payload = {
            "password": courier["password"],
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.json()["message"] == DataTest.ERROR_MESSAGE1

    @allure.title('Тест корректного ответа без заполнения пароля')
    def test_absence_password_field(self, courier):
        payload = {
            "login": courier["login"],
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.json()["message"] == DataTest.ERROR_MESSAGE1

    @allure.title('Тест создания пользователя, логин которого уже используется')
    def test_creation_username_used(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["firstName"],
            "firstName": courier["password"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.json()["message"] == DataTest.ERROR_MESSAGE2
