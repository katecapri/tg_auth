FROM python:3.10

RUN pip install "poetry==1.7.1"

RUN mkdir /application
WORKDIR /application

COPY site/pyproject.toml /application

RUN poetry config virtualenvs.create false  \
    && poetry install --no-interaction --no-ansi

COPY site /application

ENV PYTHONPATH "/application"

VOLUME /data

RUN chmod +x /application/script.sh
CMD [ "sh", "-c", "/application/script.sh" ]
