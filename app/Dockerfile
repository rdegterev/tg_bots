FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat python-dev python3-dev libevent-dev

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app/
EXPOSE 8000
CMD ["python3", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "critical"]