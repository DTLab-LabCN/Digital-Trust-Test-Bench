FROM python:3.11-slim

WORKDIR /dtt-service

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app ./app
COPY config.py main.py ./

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]