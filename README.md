# MyFlaskBlog

# Requirements
```
flask~=3.0.3
python-dotenv~=1.0.1
flask-wtf~=1.2.1
flask-sqlalchemy~=3.1.1
flask-migrate~=4.0.7
flask-login~=0.6.3
email-validator~=2.2.0
```
# Как запустить
_Версия питона - Python 3.10.12_

1. Установить виртуальное окружение командой `virtualenv nameenv`
2. Запустить виртуальное окружение командой`source nameenv/bin/activate`(выключение командой `deactivate`)
3. Установить зависимости `python -m pip install -r requirements.txt`
4. Запустить проект командой `flask run --host=0.0.0.0 --port=5001`