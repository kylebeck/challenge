## Synopsis

A simple dockerized flask-based web app that enables the user to compute various comparison metrics between two strings.


## Setup

Build the docker container by running the command `docker build -t challenge .`

Run the web app by running the command `docker run -d -p 5000:5000 challenge`


## Motivation

To have fun and learn new techniques with a practical example!


## Additional Information

Automated integration testing with selenium is configured.  You will need chromedriver installed in your path in order to run the tests.

With the web app running, enter the command `python test/form_tests.py` in a terminal to perform the integration tests.
