FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get upgrade


RUN useradd --home-dir /sergek_meteo_parser --create-home --shell /bin/bash user

WORKDIR /sergek_meteo_parser

USER user

COPY --chown=user:user ./deps.txt /sergek_meteo_parser
RUN pip install --no-cache-dir -r deps.txt

COPY --chown=user:user . /sergek_meteo_parser
