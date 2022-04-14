# Project Braeburn - technical test

Goals:

- Create Python web service
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

## Endpoints

- health/:  returns response if the Api is running
- api/?url=<http://www.example.com>: returns counted dict of words from the website, sorted by frequency
- docs/: - Api documentation (Swagger)

