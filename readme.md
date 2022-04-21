# Braeburn - technical test

Version 0.2
project simplified, file naming changed, code cleaned-up

## Goals

- Create Python web service using any framework
- Receive a URL, get contents and return number of word occurrences (can be sorted)
- provide a /health endpoint
- include full test suite
- specify dependancies
- dockerize the app

## Files

- drf_api/ - Django Rest Framework Api files
- drf_api/tests/ - tests folder
- pytest.ini - pytest settings
- src/ - modules and tests for modules
- static/openapi.json - Swagger Api Documentation schema
- templates/swagger-ui.html - Swagger Documentation template
- Dockerfile
- docker-compose.yml
- pytest.ini - pytest settings
- manage.py - django app file
- requirements.txt - dependancies
- api.log - app log file

## Endpoints

- health/:  returns response if the Api is running
- api/: with url address sent as parameter, returns counted dict of words from the website, sorted by frequency
- docs/: - Api documentation (Swagger)

## Requirements

Docker

## Installation

docker-compose up -d --build

## Usage

Sample request using HTTPIE:
http GET localhost:8000/api/ url==<http://bbc.co.uk>

Tests:
execute "pytest" command in the main folder
