import allure
import pytest

import helpers
from data import DataTest


@allure.story('Тесты на создание заказа')
class TestCreatingOrder:

    @allure.title('Тест создание заказа с разными цветами самоката и получения номера заказа')
    @pytest.mark.parametrize('color', DataTest.COLORS)
    def test_successful_order_creation_with_color(self, color):
        response = helpers.create_order(color)
        assert "track" in response
