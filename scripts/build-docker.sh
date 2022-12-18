#!/usr/bin/env bash
docker-compose -f ../deploy/docker-compose.yml --env-file ../.env up -d --build
