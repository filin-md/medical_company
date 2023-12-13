# medical_company

Django приложение сайта медицинской компании.

Используемые технологии:
    - Django
    - PostgreSQL
    - Bootstrap
    - Git


Для запуска:

1. Скачайте архив
2. Создайте в корне проекта файл .env
3. Перенесите переменные из шаблона .env.sample
4. Подставьте данные своей postgres базы данных в переменные
5. Запустите терминал в папке с проектом
6. Выполните поочередно команды:
    - python -m venv venv
    - .\venv\Scripts\activate (для windows)
    - source venv/bin/activate (для MacOS)
    - pip install -r requirements.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py csu
    - python manage.py runserver
7. Перейдите в браузере по адресу 127.0.0.1:8000
8. Войдите с учётной записью админа (admin@admin.ru/12345), или зарегистрируйте новую учётную запись.