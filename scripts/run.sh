#!/bin/bash

env=$1

if [ -z "$env" ]; then
  file=""
elif [ "$env" == "prod" ]; then
  file="-f docker-compose.yml -f docker/docker-compose.prod.yml"
else
  echo "Error: invalid environment: '$env'"
  exit 1
fi

export $(cat .env | grep -v ^# | xargs)

docker-compose $file up -d --build