# Project Breaburn - technical test

## Files

- drf_api/ - Django Rest Framework Files
- drf_api/api/ - Api files
- drf_api/tests/ - tests folder
- drf_api/pytest.ini - pytest settings

## Endpoints

- health/:  returns response if the Api is running
<!-- get data from the url and return data here -->
- api/?url=www.example.com: returns string www.example.com

## process data from url

- pass url as an argument to the module
- validate:
    - if invalid, log return error
    - if valid:
        - request data from url
        - pass data thru soup
        - filter data
        - log and return data