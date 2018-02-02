FROM python:3.6-slim-stretch

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir /code && \
    mkdir -p /usr/share/man/man1/ && \
    mkdir -p /usr/share/man/man7/ && \
    apt-get -qq update && \
    apt-get install -y --no-install-recommends \
        gcc libc6-dev libc-dev libssl-dev make automake libtool autoconf \
        pkg-config libffi-dev postgresql-client postgresql-client-common && \
    pip3 install pipenv setuptools pip --upgrade && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qq update && apt-get install -my wget gnupg && \
    apt-get -qq update && apt-get -qq -y install curl && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get -qq update && apt-get -y -qq install nodejs

WORKDIR /code

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY entrypoint.sh /usr/bin/entrypoint.sh
COPY package*.json ./

RUN npm install

RUN set -ex && pipenv install --deploy --system

RUN apt-get purge -y --auto-remove \
        gcc libc6-dev libc-dev libssl-dev make automake libtool autoconf \
        pkg-config libffi-dev

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
