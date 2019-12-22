# Resource Center 2.0

A modern take on the OpenRA Resource Center

## Requirements

1. Docker

## Development

Uses the default Django development server.

1. Rename *sample-dev.env* to *dev.env*.
1. Update the environment variables in the *docker-compose.yml* and *.env* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

## Production

Uses gunicorn + nginx.

1. Rename *sample-prod.env* to *prod.env* and *sample-prod-db.env* to *prod-db.env*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

## Tooling

* Hop into the alpine container with `docker exec -it rc2_web /bin/sh` (it doesn't have `bash`)

## References

Original docker repository setup: <https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx>
