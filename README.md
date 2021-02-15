# Plotly-Dash-Traefik-Example

This repository serves as a minimum viable example for deploying a [Plotly Dash][1] app using Traefik and Docker.

Dash is "a productive Python framework for building web analytic applications" according to the Plotly Dash docs. It uses python and javascript to make building complex dashboards simple!

This repository holds a minimum viable single-page app built on Python3.9 and is deployed using Docker and Traefik. This setup makes building scalable, easily-deployed analytics dashboards and setups simple.

## Installation Requirements

To run this example, you will need Docker and Docker Compose installed. There are plenty of great examples available elsewhere, so we will not cover that here.

## How to run this example app

We can use the docker-compose file to run both containers, but first, we need to create the network if it is not already created:

```sh
# Create the network app-net
$ docker network inspect dash-net >/dev/null 2>&1 || \ 
    docker network create -d overlay dash-net

# Launch the containers
$ docker stack deploy -c docker-compose.yml dash
```

Once deployed, you can navigate to localhost in your browser and you should see the following:

![Screen Capture](/assets/localhost.png)


That's it! If you have any comments, questions, or suggestions, please use the Issues tab above!


[1]: https://plotly.com/dash/