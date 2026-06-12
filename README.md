# 🧠 AI Sentiment Analyzer — Fullstack ML Web Application

AI Sentiment Analyzer — это полнофункциональное веб-приложение, которое анализирует эмоциональную окраску текста с использованием машинного обучения.

Пользователь вводит текст → система определяет настроение (positive / negative / neutral) → показывает результат + confidence → сохраняет данные в базе → визуализирует статистику.

---

# 📌 1. Описание проекта

Данный проект разработан как учебный fullstack AI продукт, демонстрирующий:

- интеграцию машинного обучения в веб-приложение
- работу клиент–серверной архитектуры
- хранение данных в базе SQLite
- визуализацию результатов анализа

---

# 🧠 2. Что делает приложение

Пользователь может:

- вводить текст
- получать анализ эмоции текста
- видеть уверенность модели (confidence score)
- просматривать историю запросов
- очищать историю
- видеть статистику в виде графика

---

# 🏗️ 3. Архитектура проекта

Frontend (HTML + Bootstrap + JS + Chart.js)
            ↓ HTTP (fetch API)
Backend (Flask REST API)
            ↓
Machine Learning Model (scikit-learn)
            ↓
SQLite Database
            ↓
Frontend (History + Graph UI)


<img width="1536" height="1024" alt="AI" src="https://github.com/user-attachments/assets/c4dfd714-56e6-474f-8752-d1b7568ff320" />


# ⚙️ 4. Используемые технологии

## Backend
- Python 3
- Flask
- Flask-CORS
- SQLite
- scikit-learn
- pickle

## Machine Learning
- TF-IDF Vectorizer
- Logistic Regression
- Pipeline

## Frontend
- HTML5
- Bootstrap 5
- JavaScript
- Chart.js

---

# 🤖 5. AI модель

Используется классический Machine Learning:

### TF-IDF
Преобразует текст в числовой вектор.

### Logistic Regression
Классифицирует текст на:

- positive 😊
- negative 😡
- neutral 😐

---

# 📊 6. Функциональность

- Анализ текста через AI
- Определение эмоции
- Confidence score
- История запросов
- Очистка истории
- График статистики
- Bootstrap UI

---

# 🗄️ 7. База данных (SQLite)

Таблица `results`:

- id — уникальный ID
- input_text — текст пользователя
- ai_result — результат модели
- confidence — уверенность
- created_at — время

---


<img width="1920" height="1080" alt="Снимок экрана (11)" src="https://github.com/user-attachments/assets/06c5aff2-0fc9-478c-bc95-ea48cf0a8459" />
<img width="1920" height="1080" alt="Снимок экрана (10)" src="https://github.com/user-attachments/assets/14593297-cb61-45fd-9ef2-ae7f8060d23d" />


