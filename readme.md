# Project Breaburn - technical test

## Files

- drf_api/ - Django Rest Framework Files
- drf_api/api/ - Api files
- drf_api/tests/ - tests folder
- drf_api/pytest.ini - pytest settings

## Endpoints

- health/:  returns response if the Api is running
<!-- get data from the url and return data here -->
- api/?url=<http://www.example.com>: returns string <http://www.example.com>

## process data from url

- pass url as an argument to the module
- validate:
    - if invalid, log return error
    - if valid:
        - request data from url
        - pass data thru soup
        - filter data
        - log and return data

## todos

- [x] validate the url
- [x] finish words counter
- [x] add missing tests to the word counter
- [] add api docs (swagger)
- [x] add word counter to the api view
- [] review naming
- [] lint whole project
- [] dockerize
- [] readme