import allure

import helpers
from data import DataTest


@allure.story('Тесты на логин курьера')
class TestLoginCourier:

    @allure.title('Тест возможности авторизации курьера')
    def test_can_login_courier(self, courier):
        response = helpers.login_courier(courier["login"], courier["password"])
        assert response.status_code == 200

    @allure.title('Тест запрета авторизации курьера без пароля')
    def test_login_courier_without_password(self, courier):
        response = helpers.login_courier(courier["login"], "")
        assert response.status_code == 400

    @allure.title('Тест запрета авторизации курьера без логина')
    def test_login_courier_without_login(self, courier):
        response = helpers.login_courier("", courier["password"])
        assert response.status_code == 400

    @allure.title('Тест запрета авторизации курьера с неверным логином')
    def test_login_courier_wrong_login(self, courier):
        response = helpers.login_courier(courier["password"], courier["password"])
        assert response.status_code == 404

    @allure.title('Тест запрета авторизации курьера с неверным паролем')
    def test_login_courier_wrong_password(self, courier):
        response = helpers.login_courier(courier["login"], courier["login"])
        assert response.status_code == 404

    @allure.title('Тест ошибки при авторизации курьера без пароля')
    def test_login_courier_without_password_error(self, courier):
        response = helpers.login_courier(courier["login"], "")
        assert response.json()["message"] == DataTest.ERROR_MESSAGE4

    @allure.title('Тест ошибки при авторизации курьера без логина')
    def test_login_courier_without_login_error(self, courier):
        response = helpers.login_courier("", courier["password"])
        assert response.json()["message"] == DataTest.ERROR_MESSAGE4

    @allure.title('Тест ошибки при авторизации курьера с неверным логином')
    def test_login_courier_wrong_login_error(self, courier):
        response = helpers.login_courier(courier["password"], courier["password"])
        assert response.json()["message"] == DataTest.ERROR_MESSAGE3

    @allure.title('Тест ошибки при авторизации курьера с неверным паролем')
    def test_login_courier_wrong_password_error(self, courier):
        response = helpers.login_courier(courier["login"], courier["login"])
        assert response.json()["message"] == DataTest.ERROR_MESSAGE3

    @allure.title('Тест сообщения успешного запроса на логин курьера')
    def test_successful_login_message(self, courier):
        response = helpers.login_courier(courier["login"], courier["password"])
        assert "id" in response.json()
