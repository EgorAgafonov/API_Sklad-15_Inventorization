import requests
import pytest
import json
from settings import url_base


class Sklad15Inventorization:
    """Класс c методом отправки GET запроса к REST API "Склад 15 Базовый" для тестирования функции "Инвентаризация"."""

    def __init__(self):
        self.base_url = url_base

    def get_select_docs_info(self, query_key: str, query_value: str):
        """"""

        query = {query_key: query_value}

        response = requests.get(self.base_url, params=query)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result


