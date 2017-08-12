############################################################
# Dockerfile to build Python String Comparison Web App
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Kyle Beck

# Update package list
RUN apt-get update

# Install Python
RUN apt-get install -y python-dev python-pip
#RUN apt-get install -y python-dev python-pip unzip curl

# Download and extract ChromeDriver for integration testing
# RUN curl -O https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
# RUN unzip chromedriver_linux64.zip -d /usr/bin

# Add requirements.txt to container
ADD requirements.txt /challenge/

# Get pip to download and install requirements:
RUN pip install -r challenge/requirements.txt

# Add web app to container
ADD . /challenge

# Set the default directory for our environment
ENV HOME /challenge
WORKDIR /challenge

# Expose flask debug port
EXPOSE 5000

# Set the default command to execute
CMD python run.py
