import pytest


@pytest.fixture(scope='function')
def introspection_of_test(request):
    yield
    test_name = str(request.function.__name__)
    print(f'\n- Имя теста (тестируемой функции): {test_name}.')
    print(f"- Описание теста:\n'''{request.function.__doc__}'''")
    print(f'- Имя коллекции (тестового класса): {request.cls}.')
    print(f'- Имя фикстуры: {request.fixturename}.')
    print(f'- Область видимости фикстуры: {request.scope}.')
    print(f'- Имя тестового модуля: {request.module.__name__}.')
    print(f'- Абсолютный путь к тестовому модулю: {request.fspath}.')
    if request.cls:
        return f"\n У теста(тестируемой функции) {request.function.__name__} есть коллекция (тестовый класс).\n"
    else:
        return f"\n У теста(тестируемой функции) {request.function.__name__} коллекция (тестовый класс) отсутствует.\n"


def strings_generator(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '????????????????????'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def digits():
    return '1234567890'


def latin_chars():
    return 'abcdefghijklmnopqrstwxyz'
