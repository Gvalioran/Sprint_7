# Sprint_7
# Проект автоматизации тестирования Яндекс самокат
* Основа для написания автотестов — фреймворк pytest.
* Установить зависимости — pip install -r requirements.txt.
* Команда для запуска — pytest tests --alluredir allure_results
* Команда для формирования отчетов Allure — allure serve allure_results 

data.py
* Url - Класс описания ссылок
* DataTest - Класс c тестовыми данными

helpers.py
* register_new_courier_and_return_login_password - функция для создания курьера
* generate_random_string - функция для создания случайных наборов символов
* login_courier - функция для логина курьера
* delite_courier - функция для удаления курьера
* create_order - функция для создания заказа
* get_order_list - функция для получения списка заказов

test_creating_courier.py
* test_can_create_courier - функция для проверки успешного создания курьера
* test_cannot_create_two_identical_couriers - функция для проверки запрета создания одинаковых курьеров
* test_creating_courier_without_login - функция для проверки запрета создания курьеров без заполнения логина
* test_creating_courier_without_password - функция для проверки запрета создания курьеров без заполнения пароля
* test_code_courier_creation_response - функция для проверки правильного кода ответа при создании курьера
* test_successful_request - функция для проверки сообщения успешного запроса на создание курьера
* test_absence_login_field - функция для проверки правильного сообщения об ошибке при создании курьера без поля логин
* test_absence_password_field - функция для проверки правильного сообщения об ошибке при создании курьера без поля пароля

test_creating_order.py
* test_successful_order_creation_with_color - функция для проверки создания заказа с разными цветами самоката и получения номера заказа

test_login_courier.py
* test_can_login_courier - функция для проверки возможности авторизации курьера
* test_login_courier_without_password - функция для проверки запрета авторизации курьера без пароля
* test_login_courier_without_login - функция для проверки запрета авторизации курьера без логина
* test_login_courier_wrong_login - функция для проверки запрета авторизации курьера с неверным логином
* test_login_courier_wrong_password - функция для проверки Тест запрета авторизации курьера с неверным паролем
* test_login_courier_without_password_error - функция для проверки ошибки при авторизации курьера без пароля
* test_login_courier_without_login_error - функция для проверки ошибки при авторизации курьера без логина
* test_login_courier_wrong_login_error - функция для проверки ошибки при авторизации курьера с неверным логином
* test_login_courier_wrong_password_error - функция для проверки ошибки при авторизации курьера с неверным паролем
* test_successful_login_message - функция для проверки сообщения успешного запроса на логин курьера

test_order_list.py
* test_successful_order_list  - функция для проверки получения списка заказов