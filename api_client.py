import requests
import pytest
import json
from settings import url_base


class Sklad15Inventorization:
    """Класс c методом отправки GET запроса к REST API "Склад 15 Базовый" для тестирования функции "Инвентаризация"."""

    def __init__(self):
        self.base_url = url_base

    def get_invent_docs_info(self):
        """"""


