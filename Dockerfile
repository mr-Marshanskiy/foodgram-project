FROM python:3.9.2
WORKDIR /code
COPY . .
RUN pip install -r ./requirements.txt
CMD cd ./foodgram && gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000