[![CI](https://github.com/nogibjj/Jiechen_Li_Individual_4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jiechen_Li_Individual_4/actions/workflows/cicd.yml)

# Jiechen_Li_Individual_4

## Purpose

* Build a publicly accessible auto-scaling container using Azure App Services and Flask.
* Enables the Flask App to run in a Docker Container.
* Hosting functioning container on DockerHub.
* Deploying container via Azure Web App to a public endpoint.

## Dataset

The dataset is selected from [Kaggle](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) as a good clean dataset of books. The dataset contains the detailed information about the books and authors, primarily. Detailed description for each column can be found alongside.

## Flask App Guidance on Local IDE

1. **Install it in Python Environment**

```command line
pip install Flask
```

2. **Create ``flask_app.py`` file**

We name our App as "BookBuddy", which is a book recommemdation system.

```python
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
books_df = pd.read_csv('books.csv')

@app.route('/')
def index():
    return "Welcome to BookBuddy!"
```

3. **Test ``flask_app.py`` file**

```python
import unittest
from flask_app import app
import urllib.parse

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to BookBuddy!", response.data)
```

## Docker Guidance

1. **Write a Dockerfile**

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run flask_app.py when the container launches
CMD ["python", "flask_app.py"]
```

2. **Build Docker Image Locally**

```Dockerfile
docker build -t bookbuddy:latest . 
```

Ensure we installed Docker Desktop in local, and have our tag name with lowercase

3. **Create a Repository on Docker Hub**

Create a new repository named ``bookbuddy``, and push the Docker image.

```command line
docker login
docker tag bookbuddy:latest carrieli15/bookbuddy:latest
docker push carrieli15/bookbuddy:latest
```

## Azure Guidance

1. **Set Up Azure CLI**

Install it from the offical website and configure it locally.

```command line
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew update && brew install azure-cli
```

2. **Create a Web App and Deploy**

In the Web App's settings, we can find the section for deployment, often labeled as "Deployment Center". Choose the option to deploy a container from Docker Hub. Provide the details of our Docker image.

3. **Continuous Deployment**

Azure can automatically redeploy our app whenever you update the Docker image on Docker Hub by chooing "On" for continuous deployment.

### Results

1. **Create Flask App of BookBuddy**
<img decoding="async" src="1_flask_app.png" width="85%"><br>  

2. **Test for Flask App of BookBuddy**
<img decoding="async" src="2_test_app.png" width="85%"><br/>

3. **Docker Image Build for BookBuddy App**
<img decoding="async" src="3_docker.png" width="85%"><br/>

4. **Push Docker Image to Docker Hub**
<img decoding="async" src="4_docker_hub.png" width="85%"><br/>

5. **Create Azure Web App**
<img decoding="async" src="5_create_web.png" width="85%"><br/>

6. **App Unique URL**
<img decoding="async" src="6_uniq_url.png" width="85%"><br/>

7. **Azure Logs Showing the Progress of the Deployment**
<img decoding="async" src="7_log_deployment.png" width="85%"><br/>

## Demo Video

[Project Walkthrough Video](https://youtu.be/NVmPZFgrJ2Q)

## Reference

Please click <a href="https://github.com/nogibjj/python-ruff-template">here</a> to see the template of this repo.
