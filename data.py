class Url:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    LOGIN = BASE_URL + "/api/v1/courier/login"
    CREATE_COURIER = BASE_URL + "/api/v1/courier"
    DELITE_COURIER = BASE_URL + "/api/v1/courier/"
    ORDERS = BASE_URL + "/api/v1/orders"


class DataTest:
    ERROR_MESSAGE1 = "Недостаточно данных для создания учетной записи"
    ERROR_MESSAGE2 = "Этот логин уже используется. Попробуйте другой."
    ERROR_MESSAGE3 = "Учетная запись не найдена"
    ERROR_MESSAGE4 = "Недостаточно данных для входа"
    COLORS = ['[]', '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']
    DATA_FOR_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
