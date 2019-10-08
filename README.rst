This is an example of how ftrack actions or event listeners can be built as a
python module when they should run as a service.

The python module can be packaged as a docker image to
simplify execution and distribution. The module has a built in health check
which is used to test that the module stay in a healthy state.

Note: To use the commands below the current shell is expected to have the
following environment variables exported FTRACK_SERVER, FTRACK_API_USER, FTRACK_API_KEY
and have a python virtual environment activated.

Install for development::
pip install -e .

Run the module::
python -m ftrack_service_example

Run the health check::
python -m ftrack_service_example --healthcheck

Build as a docker image::
docker build -t ftrack-service-example:latest --target final .

Run the docker image::
docker run --name ftrack-service-example -it --rm --env FTRACK_SERVER --env FTRACK_API_USER --env FTRACK_API_KEY ftrack-service-example:latest

See that the container is working and healthy::
docker ps

Running the container the container using docker will not restart it
automatically if it enters an unhealthy state. To have the container
automatically restarted when it becomes unhealthy a container orchestrator must
be used, such as docker swarm or kubernetes.

To run the container using docker swarm and allow it to heal after failure run
the following::
docker service create --name ftrack-service-example --env FTRACK_SERVER --env FTRACK_API_USER --env FTRACK_API_KEY ftrack-service-example:latest

Check that the service is running::
docker service ls

Look at the logs of the service::
docker service logs ftrack-service-example
