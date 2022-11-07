# ftrack-service-example

This is an example of how ftrack actions or event listeners can be built
as a python module when they should run as a service. Multiple actions
can be built into the same module if they need to share logic or are
part of the same solution.

The python module can be packaged as a docker image to simplify
execution and distribution. The module has a built in health check which
is used to test that the module stay in a healthy state.

## Note

General knowledge on python, how ftrack actions are built and how to
build and run docker containers is expected. To use the commands below
the current shell is expected to have the following environment
variables exported FTRACK_SERVER, FTRACK_API_USER, FTRACK_API_KEY and
have a python virtual environment activated.

This module does not handle scaling out actions. It would however be
possible add a message to a queue instead of doing work async in the
same process. Separate workers could be setup to consume those messages
in parallel.


## Examples

Below is a list of useful commands that can be used to work with this
module.

Install for development

``` python
pip install -e .
```

Run the module with python

``` python
python -m ftrack_service_example
```

Run the health check. It will exit with code 0 if the service is running
and hang forever if not

``` python
python -m ftrack_service_example --healthcheck
```

Build as a docker image

``` bash
docker build -t ftrack-service-example:latest --target final .
```

Test the image by running it as a container in the foreground

``` bash
docker run --name ftrack-service-example -it --rm --env FTRACK_SERVER --env FTRACK_API_USER --env FTRACK_API_KEY ftrack-service-example:latest
```

See that the container is working and is healthy

``` bash
docker ps
```

Running the container using docker will not restart it automatically if
it enters an unhealthy state. To have the container automatically
restarted when it becomes unhealthy a container orchestrator must be
used, such docker swarm or kubernetes.

To run the container as a docker service (swarm) and allow it to heal
after failure run the following

``` bash
docker swarm init
docker service create --name ftrack-service-example --env FTRACK_SERVER --env FTRACK_API_USER --env FTRACK_API_KEY ftrack-service-example:latest
```

Check that the service is running

``` bash
docker service ls
```

Look at the logs of the service

``` bash
docker service logs ftrack-service-example
```
