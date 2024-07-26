Авто-тесты для 
функционального тестирования REST API модуля "Инвентаризация" приложения MobileSMARTS "Склад 15, Базовый".


Cтруктура проекта представлена:
1) папкой tests c модулем test_get_invent_docs_info.py, содержащим позитивные и негативные тест-кейсы;
2) модулем api_client.py, содержащим класс с методом отправки GET-запроса к REST API MobileSMARTS 
"Склад 15, Базовый";
3) модулем conftest.py c фикстурами Pytest для запуска тестов и вспомогательными тестовыми объектами;
4) модулем settings.py c переменными среды окружения (env);
5) файлом requirements.txt c необходимыми библиотеками для импорта.

Каждая функция и класс содержат аннотацию к выполняемому коду.

Агафонов Е.А., 2024 г.
