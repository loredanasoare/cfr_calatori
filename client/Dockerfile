FROM python:3.6

EXPOSE 5005

WORKDIR /client

COPY . /client

RUN pip install -r requirements.txt

CMD python3 client.py
