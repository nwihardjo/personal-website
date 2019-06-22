# Personal Website

This website for my portfolio is built using Django 2 with `SQLite`, packaged in a Docker container, and deployed using Heroku with the `Postgres` as the database. Might be overkill for personal website to be made with Django and Docker, but why not? 

`datadump.json` is used to handle different database uses in the deployment and development environment. Building Docker Images in heroku is done with `heroku.yml`.

## Dependencies

- Install Docker and Compose based on your OS from [here](https://docs.docker.com/install/)
- Enable running Compose as a non-root user from [here](https://docs.docker.com/install/linux/linux-postinstall/)
- Make sure Docker is running by `systemctl start docker` and properly installed by running `docker run hello-world`

## Installation and Building the system

- Clone this repo
- Run `docker-compose up` on the root directory of the repo
- Head up to `localhost:8000` from your browser.
