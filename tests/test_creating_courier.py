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
        assert response.status_code == 409 and response.json()["message"] == DataTest.ERROR_MESSAGE2

    @allure.title('Тест запрета создания курьеров без заполнения логина')
    def test_creating_courier_without_login(self):
        payload = {
            "login": "",
            "password": helpers.generate_random_string(10),
            "firstName": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Тест запрета создания курьеров без заполнения пароля')
    def test_creating_courier_without_password(self):
        payload = {
            "login": helpers.generate_random_string(10),
            "password": "",
            "firstName": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Тест на правильный код ответа при создании курьера')
    def test_code_courier_creation_response(self):
        payload = {
            "login": helpers.generate_random_string(10),
            "password": helpers.generate_random_string(10),
            "firstName": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        courier_id = helpers.login_courier(payload["login"], payload["password"]).json()["id"]
        helpers.delite_courier(courier_id)
        assert response.status_code == 201

    @allure.title('Тест сообщения успешного запроса на создание курьера')
    def test_successful_request(self):
        payload = {
            "login": helpers.generate_random_string(10),
            "password": helpers.generate_random_string(10),
            "firstName": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        courier_id = helpers.login_courier(payload["login"], payload["password"]).json()["id"]
        helpers.delite_courier(courier_id)
        assert response.json() == {'ok': True}

    @allure.title('Тест правильного сообщения об ошибке при создании курьера без поля логин')
    def test_absence_login_field(self, courier):
        payload = {
            "password": courier["password"],
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.json()["message"] == DataTest.ERROR_MESSAGE1

    @allure.title('Тест правильного сообщения об ошибке при создании курьера без поля пароля')
    def test_absence_password_field(self, courier):
        payload = {
            "login": courier["login"],
            "firstName": courier["firstName"]
        }
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.json()["message"] == DataTest.ERROR_MESSAGE1
