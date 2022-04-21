# Braeburn.py
## Description
App takes url as in input, extracts text from given url, then counts occurrences of words in that text. The project is now dockerized and can be run in a local container
## Stack
Python, Django Rest Framework, BeautifulSoup, Docker, SQlite, Nginx, Gunicorn

## Installation

Use the following commands with docker-compose to setup:

<!-- env files need to run the app -->
1. Create of the following files with sample values:
bramley/bramley/.env.prod
bramley/bramley/.env.dev
*sample values:*
DJ_SECRET_KEY=sample_secret_key
ALLOWED_HOSTS=[]
DEBUG=1

<!-- build containers -->
2. docker-compose -f docker-compose-prod.yml up -d --build
<!-- copy Django static files to a docker volume -->
3. docker-compose -f docker-compose-prod.yml exec web python manage.py collectstatic --no-input --clear
<!-- set up django db and create admin user -->
4. Django set-up
docker-compose -f docker-compose-prod.yml exec web python manage.py makemigrations
docker-compose -f docker-compose-prod.yml exec web python manage.py migrate
docker-compose -f docker-compose-prod.yml exec web python manage.py createsuperuser




## REST API
#### Description
App is accessible through Rest API, built using Django Rest Framework.
Successful queries are stored in the local database (SQlite).
API is also accessible through DRF browser interface at address: http://localhost:1337
Username and password are needed to access the api, users can be created in Django admin panel

#### Access points: 
- root:   link to users list (access for admin only)
        link to user's queries list (or all queries if superuser is logged in)

- queries/    GET request will list logged user's queries
            POST request with form data 'url':'valid url address' will return json response
                with the results of Braeburn.py script, and store these results in the database

- queries/id/ users can access stored queries by their id numbers. Queries can be modified or deleted from this endpoint here with PUT or DELETE requests

- health/     shows system status

#### sample requests using httpie on localhost:
http -a demo:grannysmith --form POST :1337/queries/ url="http://www.bbc.co.uk"
http -a demo:grannysmith GET :1337/queries/
http -a demo:grannysmith GET :1337/queries/4/

#### Braeburn.py Usage:
- usage: braeburn.py [-h] [-u] url

- positional arguments:
  url             Enter full url: https://example.com

- options:
  -h, --help      show this help message and exit
  -u, --unittest  Show unit tests

- Response is a json object with the following information:
status - success or error code
message - error message
url - url accessed
data - Word occurrences from the input url

**Braeburn.py output codes:**
10 - success
01 - invalid or no input
02 - url address invalid 
03 - http errors: check response for details


## Files
- bramley/ -- Django Rest Framework files
- bramley/braeburn.py -- main app file
- bramley/braeburn_info.lof -- main app log file
- requirements.txt -- list of dependancies needed
- readme.md -- project description and usage

- nginx/ -- nginx config and dockerfile

- docker-compose.yml - development version compose file
- docker-compose-prod.yml - production version compose file (set up for localhost)


<!-- for api testing -->
test_reqs.py -- simple script to test the app under load (needs updating for auth)
    Testing results (using django development server):
    - 100 requests google.com ~1s per request
    - 100 requests localhost <0.5 sec per request

    Testing results using Nginx and Gunicorn (bbc.co.uk): 
      <!--  -->
      98: 201
      99: 201
      100: 201
      Elapsed time: 0:01:18.903999
      <!--  -->


test_responses.txt test_reqs.py sample result
