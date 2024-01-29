import pytest

import helpers


@pytest.fixture
def courier():
    courier = helpers.register_new_courier_and_return_login_password()
    courier_id = helpers.login_courier(courier["login"], courier["password"]).json()["id"]
    yield courier
    helpers.delite_courier(courier_id)
