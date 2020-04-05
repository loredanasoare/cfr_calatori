FROM python:3.6

EXPOSE 5000

WORKDIR /server

COPY . /server

RUN pip install -r requirements.txt

CMD python3 server.py
