# 🏋️‍♂️ Fitness Bot

Телеграм-бот для трекинга личных фитнес-данных: упражнения, прогресс, советы и многое другое. Создан с использованием `aiogram`.

## 🚀 Возможности

- Отслеживание тренировок и прогресса
- Удобные команды и интерфейс
- Панель администратора
- Расширяемая архитектура

## 📁 Структура проекта

```
.
├── app
│   ├── core
│   │   ├── bot.py              # Инициализация бота
│   │   └── config_reader.py    # Загрузка конфигураций
│   ├── handlers
│   │   ├── admin               # Админ-команды
│   │   └── user                # Команды пользователя
│   ├── keyboards               # Кастомные клавиатуры
│   ├── middlewares            # Middleware-логика
│   └── utils                  # Утилиты и вспомогательные функции
├── main.py                     # Точка входа в приложение
└── readme.md                   # Документация
```

## ⚙️ Установка

```bash
git clone https://github.com/yourusername/fitness-bot.git
cd fitness-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создай `.env` файл в корне проекта и укажи:

```
BOT_TOKEN=your_token_here
ADMINS=your_admin_id
```

## 🧠 Используемые технологии

- Python 3.10+
- aiogram 3.x
- python-dotenv
- asyncio

## 📌 TODO

- [ ] Добавить хранение данных (SQLite/PostgreSQL)
- [ ] Вывод графиков и статистики
- [ ] Поддержка напоминаний и целей

## 👨‍💻 Автор

<!-- **\[Твой ник или имя]** – Frontend / Telegram developer
Telegram: [@твой\_ник](https://t.me/твой_ник) -->
