from flask import Flask, render_template, jsonify

# Создание flask app
app = Flask(__name__)

# Симулятор базы данных
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bishkek, Kyrgyzstan',
    'salary': '15 000 $'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '10 000 $'
  },
  {
    'id': 3,
    'title': 'Frontand Engineer',
    'location': 'Remout'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'USA',
    'salary': '120 000 $'
  }
]

# Регистрация маршрута ("/") - домашняя, главная страница
@app.route("/")

# Функция, которая будет выполняться при запросе к домашней страниц
def hello_jovian():
  # Визуализировать шаблон
  # Отправить в шаблон параметр с данными
  return render_template("home.html",
                        jobs=JOBS,
                        company_name="Jovian")

@app.route("/api/jobs")

# Использование API для получения данных (отображение информации в формате json)
def list_jobs():

  # Преобразование данных в формат json
  return jsonify(JOBS)

# Проверка, что запускаем именно это приложение app.py
if __name__ == "__main__":
  # Запуск приложения
  # host = "0.0.0.0" - для того, чтобы приложение работало в локальном режиме
  # debug = True - для того, чтобы приложение выводило ошибки при работе (отладка)
  app.run(host="0.0.0.0", debug=True)