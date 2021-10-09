FROM python:3.8-alpine

WORKDIR /app

# устанавливает зависимости для python app.py
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# копирует всё из текущей директории (исходники приложения)
COPY . /app

CMD ["python", "app.py"]
