FROM devops.cuic.mitre.org/cuic-lab/mitre-cuic-debian-bookworm:py3.11

ENV HTTP_PROXY=devops.cuic.mitre.org
ENV APP_HOME=/home/cuic-dev/accel-open-dis-python
ENV PROJECT_REGISTRY=devops.cuic.mitre.org

WORKDIR $APP_HOME

## Copy code into container
COPY . .

RUN poetry config certificates.cuic-devops-registry.cert /etc/ssl/certs/ca-certificates.crt

RUN echo `poetry --version`

# Use the below to use secrets
RUN --mount=type=secret,id=dev_server_password \
    --mount=type=secret,id=dev_server_username \
    DEV_SERVER_USERNAME=$(cat /run/secrets/dev_server_username) \
    && export DEV_SERVER_USERNAME \
    && DEV_SERVER_PASSWORD=$(cat /run/secrets/dev_server_password) \
    && export DEV_SERVER_PASSWORD \
    && poetry config http-basic.cuic-devops-registry $DEV_SERVER_USERNAME $DEV_SERVER_PASSWORD \
    && poetry install --no-root --only main,dev

ENTRYPOINT [ "" ]

# Copy code into correct location into site-packages since poetry does not cooperate, even without no-root
WORKDIR /usr/local/lib/python${PYTHON_VERSION}/site-packages/opendis
COPY ./opendis  .

WORKDIR $APP_HOME
