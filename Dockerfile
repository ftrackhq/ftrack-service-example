FROM python:3.9-slim as base
MAINTAINER ftrack <sysop@ftrack.com>

COPY ./ /ftrack-service-example
RUN pip install /ftrack-service-example

FROM python:3.9-slim as final

COPY --from=base /usr/local /usr/local

ENTRYPOINT python -m ftrack_service_example -v info

HEALTHCHECK --interval=60s --timeout=10s --start-period=30s --retries=3 CMD python -m ftrack_service_example -v info --healthcheck
