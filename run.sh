#!/bin/bash

docker stop $1 $2
docker rm $1 $2
docker-compose up
