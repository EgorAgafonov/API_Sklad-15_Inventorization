from api_client import Sklad15Inventorization
from conftest import *
import sys

s15 = Sklad15Inventorization()


class TestInventorizationSklad15:
    """Набор позитивных, автоматизированных тест-кейсов для проверки GET-запроса функции
    "Инвентаризация" REST API 'Склад 15, Базовый'."""

    def test_get_data_from_invent_docs(self, key="$select", value="id,name"):
        """Проверка GET-запрос функции 'Авторизация' на предмет предоставления сведений о документах инвентаризации.
        Параметр запроса query использует верифицированные значения, указанные в документации Swagger. Валидация теста
        успешна, если тело ответа содержит сведения о всех запрошенных атрибутах документов."""

        status, result = s15.get_select_docs_info(query_key=key, query_value=value)

        assert status == 200, f'Ошибка! Статус-код запроса: {status}'

        for i in result['value']:
            assert i['id'] != ""
            assert i['name'] != ""


    # @pytest.mark.three
    # @pytest.mark.get_info_invalid
    # @pytest.mark.parametrize('filter', [strings_generator(255),
    #                                     strings_generator(1001),
    #                                     russian_chars(),
    #                                     russian_chars().upper(),
    #                                     chinese_chars(),
    #                                     special_chars(),
    #                                     digits()],
    #                          ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese chars',
    #                               'specials', 'digits'])
    # def test_getAllPets_invalid_filter(self, get_api_key, filter):
    #     """Негативный тест проверки запроса размещенных пользователем карточек питомцев. Используется фикстура
    #     get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
    #     классом атрибутов и методов PetFriends выполняется get-запрос на предоставление всех карточек питомцев,
    #     созданных пользователем. В параметрах запроса передаётся необходимое значение фильтра - 'my_pets'. Валидация
    #     теста считается успешной в случае, если статус ответа сервера не равен коду 200."""
    #
    #     status, result = pf.get_all_pets(auth_key=get_api_key, filter=filter)
    #
    #     if status == 200:
    #         raise Exception(f'Ошибка сервера, некорректный запрос успешно обработан! Код ответа - {status}')
    #     else:
    #         assert status != 200
    #         print(f'\nОжидаемый код ответа сервера: 500')
    #         print(f'Фактический код ответа сервера: {status}')
    #         print(f"Тестируемое не верифицированное значение filter: '{filter}'")