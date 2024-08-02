from api_client import Sklad15Inventorization
from conftest import *
import sys
from settings import *
import requests
import json

s15 = Sklad15Inventorization()


class TestInventorizationSklad15:
    """Набор автоматизированных тест-кейсов для проверки GET-запроса функции "Инвентаризация"
    REST API 'Склад 15, Базовый'."""

    def test_select_data_from_docs_positive(self, query_value="?$select=id,name"):
        """Позитивный тест проверки GET-запроса функции 'Авторизация' на предмет предоставления сведений о id-номере и
        наименовании (name) документа инвентаризации. Строка параметра query использует верифицированные значения,
        указанные в документации на Swagger. Валидация теста успешна, если тело ответа содержит сведения о всех
        запрошенных атрибутах документов."""

        status, result = s15.get_select_docs_info(query=query_value)

        # 1. Проверка статуса ответа сервера:
        assert status == 200, f'Ошибка! Статус-код запроса: {status}'

        # 2. Проверка наличия в теле ответа значений ключей id и name:
        for i in result['value']:
            assert i['id'] != ""
            assert i['name'] != ""
            print(f"\n{i}")

    def test_get_strict_quantity_of_docs_positive(self, query_value="?$top=5&$skip=16"):
        """Позитивный тест проверки GET-запрос функции 'Авторизация' на предмет предоставления сведений о документах
        инвентаризации в количестве (top) и с определенного индекса(пропуска), указанных в значении параметра query.
        Строка query использует верифицированные значения, указанные в документации Swagger. Валидация теста успешна,
        если тело ответа содержит количество документов, соответствующее значению в параметре запроса (top)."""

        status, result = s15.get_select_docs_info(query=query_value)

        # 1. Проверка статуса ответа сервера:
        assert status == 200, f'Ошибка! Статус-код запроса: {status}'

        # 2. Проверка количества документов в теле ответа:
        id_num_list = []
        for i in result["value"]:
            id_num_list.append(i['name'])
        assert len(id_num_list) == 5

    @pytest.mark.parametrize("top_value", ["-1", "zero", "1.5"], ids=['negative num', 'zero string', 'float num'])
    def test_get_strict_quantity_of_docs_negative(self, top_value):
        """Негативный тест проверки GET-запроса функции 'Авторизация' на предмет предоставления сведений о документах
        инвентаризации в количестве (top) и с определенного индекса(пропуска), указанных в значении параметра query.
        Строка query принимает не валидные значения параметра top. Валидация негативного теста успешна, если статус-код
        ответа не равен 200 соответственно."""

        query = f"?$top={top_value}&$skip=16"
        response = requests.get(url_base + query)
        status = response.status_code
        result = response.json()

        assert status != 200
        print(result)





