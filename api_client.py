import requests
import pytest
import json
from settings import url_base


class Sklad15Inventorization:
    """Класс c методом отправки GET запроса к REST API "Склад 15 Базовый" для тестирования функции "Инвентаризация"."""

    def __init__(self):
        self.base_url = url_base

    def get_select_docs_info(self, query_key: str, query_value: str):
        """GET-mетод для предоставления сведений о документах инвентаризации приложения MobileSMARTS "Склад 15, Базовый.
         Аргументы query_key и query_value принимают значения, указанные в REST API документации Swagger для
         «Mobile SMARTS: Магазин 15»."""

        query = {query_key: query_value}

        response = requests.get(self.base_url, params=query)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result


