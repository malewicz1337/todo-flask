FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD ["run.py" ]
