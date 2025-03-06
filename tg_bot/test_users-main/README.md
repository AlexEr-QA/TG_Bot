<h2>Телеграм бот для генерации паролей</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
* Помогает быстро сгенерировать сложные пароли для тестирования или использования.
* Принимает на вход запрос на количество паролей и создает случайные пароли определенной длины.

## 🖼 Скриншоты

Стартовое меню:

![image]()

После выбора количества пользователей:

![image]()

## 💻 Технологии

* Python
* Библиотека `telebot`
* Библиотека `faker`

## ⏬ Установка на локальном компьютере

1. Скачать проект

2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
PS> C:\Users\Name\AppData\Local\Programs\Python\Python312\python -m venv venv\
```

``` markdown
PS> venv\Scripts\activate
(venv) PS>
```
4. Устанавливаем библиотеки

``` markdown
(venv) PS> python -m pip install pyTelegramBotAPI
```

``` markdown
(venv) PS> python -m pip install faker
```

5. Запускаем
``` markdown
(venv) PS> python test_users_bot.py

```

## Автор

Ероскин Алексей ([@surra_gott](https://t.me/surra_gott))
