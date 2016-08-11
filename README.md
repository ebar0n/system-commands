# App system commands

[![Requirements Status](https://requires.io/github/ebar0n/system-commands/requirements.svg?branch=master)](https://requires.io/github/ebar0n/system-commands/requirements/?branch=master)
[![Build Status](https://travis-ci.org/ebar0n/system-commands.svg?branch=master)](https://travis-ci.org/ebar0n/system-commands)

## Requirements

0. Install and configure Docker

    0. Install docker. [Docker](https://www.docker.com)

    0. Install docker-machine and virtualbox. [Machine](https://docs.docker.com/machine/), [Virtualbox](https://www.virtualbox.org/wiki/Downloads) `optional in linux`

    0. Intall docker-compose. [Compose](https://docs.docker.com/compose/install/)

0. Set Var Environment

    * Copy to `env.example` into `.env`

            cp env.example .env

    * Edit values in `.env`

            nano .env

### Run the project DEV

0. Only in docker-machine `optional in linux`

    0. Pre-Build

            docker-machine create --driver virtualbox --virtualbox-memory 10240 --virtualbox-cpu-count 2 app
            docker-machine start app
            eval "$(docker-machine env app)"

0. Build containers

        docker-compose build

## BackEnd

0. Run Django Project

        docker-compose up -d
        
0. Open project on browser

        http://127.0.0.1:8000

### Run tests to style

0. Run tests isort

        docker-compose run --rm django isort -c -rc -df

0. Run tests flake8

        docker-compose run --rm django flake8
