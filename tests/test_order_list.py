import allure

import helpers


@allure.story('Тесты списка заказов')
class TestOrderList:

    @allure.title('Тест получения списка заказов')
    def test_successful_order_list(self):
        response = helpers.get_order_list()
        assert "orders" in response
