FROM ubuntu

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app

COPY . /app

RUN pip install flask

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]