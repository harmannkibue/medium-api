ARG PYTHON_VERSION=3.10.2-slim-bullseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

# use the -y to disallow promps while installing
# use --no-install-recommends to disallow installing recommended packages not needed
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# This tells python to not write .pyc file to disk
ENV PYTHONDONTWRITEBYTECODE 1

# Python output is directly transmitted to the terminal without being buffered thus realtime
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o
    APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -r /wheels/

# coppying the entrypoint
COPY ./docker/local/django/entrypoint /entrypoint
# Looking for endings in the shell scripts and converting any windows shell endings to unix
RUN sed -i 's/\r$//g' /entrypoint
# making the shell script excecutable
RUN chmod +x /entrypoint

#start script ensures that django models are migrated, server started and static fiiles collected
COPY ./docker/local/django/start /start
# Looking for endings in the shell scripts and converting any windows shell endings to unix
RUN sed -i 's/\r$//g' /start
# making the shell script excecutable
RUN chmod +x /start

#copy all our code to the application directory
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
