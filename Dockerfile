FROM python:3.9-slim as base
MAINTAINER ftrack <sysop@ftrack.com>

COPY ./ /ftrack-service-example

RUN python -m venv /opt/ftrack && \
    /opt/ftrack/bin/pip install pip -U && \
    /opt/ftrack/bin/pip install --use-feature=in-tree-build /ftrack-service-example

FROM python:3.9-slim as final

RUN adduser --disabled-password --gecos '' ftrack
USER ftrack

COPY --from=base /opt/ftrack /opt/ftrack
ENV VENV=/opt/ftrack
ENV PATH="$VENV/bin:$PATH"
ENV FTRACK_API_SCHEMA_CACHE_PATH="/tmp/"

ENTRYPOINT python -m ftrack_service_example -v info

HEALTHCHECK --interval=60s --timeout=10s --start-period=30s \
    --retries=3 CMD python -m ftrack_service_example -v info --healthcheck
