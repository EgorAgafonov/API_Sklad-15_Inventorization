from api_client import Sklad15Inventorization
from conftest import *
import sys

s15 = Sklad15Inventorization()


class TestInventorizationSklad15:
    """Набор автоматизированных тест-кейсов для проверки GET-запроса функции "Инвентаризация"
    REST API 'Склад 15, Базовый'."""

    def test_select_data_from_invent_docs(self, query_value="?$select=id,name"):
        """Проверка GET-запрос функции 'Авторизация' на предмет предоставления сведений о id-номере и name-наименовании
        документа инвентаризации. Строка параметра query использует верифицированные значения, указанные в документации
        Swagger. Валидация теста успешна, если тело ответа содержит сведения о всех запрошенных атрибутах документов."""

        status, result = s15.get_select_docs_info(query=query_value)

        # 1. Проверка статуса ответа сервера:
        assert status == 200, f'Ошибка! Статус-код запроса: {status}'

        # 2. Проверка наличия в теле ответа значений ключей id и name:
        for i in result['value']:
            assert i['id'] != ""
            assert i['name'] != ""

    def test_get_strict_nums_of_invent_docs(self, query_value="?$top=5&$skip=10"):
        """Проверка GET-запрос функции 'Авторизация' на предмет предоставления сведений о документах инвентаризации в
        количестве (top) и с определенного индекса(пропуска), указанных в значении параметра query. Строка query
        использует верифицированные значения, указанные в документации Swagger. Валидация теста успешна, если тело
        ответа содержит количество документов, соответствующее значению в параметре запроса (top)."""

        status, result = s15.get_select_docs_info(query=query_value)

        # 1. Проверка статуса ответа сервера:
        assert status == 200, f'Ошибка! Статус-код запроса: {status}'

        # 2. Проверка количества документов в теле ответа:
        id_num_list = []
        for i in result["value"]:
            id_num_list.append(i['name'])
        assert len(id_num_list) == 5