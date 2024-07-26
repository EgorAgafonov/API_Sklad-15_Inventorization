from api_client import Sklad15Inventorization
from conftest import *
import sys

s15 = Sklad15Inventorization()


class TestInventorizationSklad15:
    """Набор авто-тестов для проверки GET-запроса функции "Инвентаризация" REST API 'Склад 15, Базовый'."""

    def test_get_data_from_invent_docs(self, key="$select", value="id,name"):
        """Позитивный тест проверки запроса"""

        status, result = s15.get_select_docs_info(query_key=key, query_value=value)

        assert status == 200, f'Ошибка! Статус-код запроса: {status}'
        print(result)
        for i in result['value']:
            line = f'\n{i}'
            print(line)
        # assert len(result.get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
        # print(f"\nТестируемое значение filter = : '{filter}'")

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