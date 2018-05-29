# GSoC Past Data Scraper

## About

* This can be used to scrape past gsoc data of any org. This fetches both org information and projects list and displays them in a web page hosted by Django.

## Technology Used:

* Python 3.5.2
* This uses Django to display scraped data.
* This uses [Scrapy](https://doc.scrapy.org/en/latest/index.html) to scrape the data. 
* This uses YAML to store the data.
* ruamel.yaml to dump json data to yaml files.

## Steps to run:

* Clone this project.
* Create Python virtual environment with python version 3.5.2 
  > virtualenv -p python3 venv
* If you chose to go with virtualenv, it's time to activate it:
  > source venv/bin/activate
* Now install all dependencies
  > pip3 install -r requirements.txt
* It's time to scrpae GSoC data
  > scrapy crawl gsoc
* It will ask you for org name and year. Enter the correct org name and year which is past year.
* Now if previous steps succeeds, you can start your django server via
  > python manage.py runserver
* Go to `localhost:8000` and enjoy.


#### Report bugs [here](https://github.com/pradeepgangwar/GSoC-Data-Scraper/issues)

## Contributing

* You can contribute to this project by adding a new feature or scraping this year's data.
* You can report bugs [here](https://github.com/pradeepgangwar/GSoC-Data-Scraper/issues).

