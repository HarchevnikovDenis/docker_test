from flask import Flask  # импорт web framework


app = Flask(__name__)  # запуск web server
count = 0  # счетчик


@app.route("/")  # связывает python function and url
def get_count():
    return str(count)  # flask просит возвращать сроку (целочисленное значение не может)


@app.route("/stat/")
def increment_count():
    global count  # чтобы изменять переменную счётчик на уровне скрипта 5 строка
    count += 1

    return str(count)


@app.route("/about/")
def hello():
    html = """<h3>Hello, Denis</h3>"""  # формируем html код

    return html


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
