## Recommender Systems

[![Website monip.org](https://img.shields.io/website-up-down-green-red/http/monip.org.svg)](http://recommendersystems.appspot.com/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![HitCount](http://hits.dwyl.com/pinarkaymaz6/Recommender-Systems.svg)](http://hits.dwyl.com/pinarkaymaz6/Recommender-Systems)
[![GitHub last commit](https://img.shields.io/github/last-commit/pinarkaymaz6/Recommender-Systems.svg?style=flat)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)



The application is live at [http://recommendersystems.appspot.com/](http://recommendersystems.appspot.com/).

## Setup

### 1. Get a copy of Recommender-Systems repo
Go ahead and clone this repo your to machine

```shell
git clone https://github.com/pinarkaymaz6/Recommender-Systems.git
```

### 2. Run locally 
Running locally is not a mandatory step, but I highly recommend it. It's easier to save and view your changes, since deployment to cloud takes a few minutes.
- Create a virtual environment and install dependencies
    ```shell
    cd Recommender-Systems/recommender
    python3 -m venv FILENAME
    source FILENAME/bin/activate
    pip install -r requirements.txt
    ```
- Start the app
    ```shell
    python3 main.py
    ``` 
- Now visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/) to view your application.

### 3. Deploy to Google App Engine
First you should create a project on Google Cloud dashboard if you don't have one. You can follow the instructions [here](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project?hl=en-GB) to create a project. 
- Install Google Cloud SDK. [Here](https://cloud.google.com/sdk/docs/quickstart-macos) is the guide for macOS. Make sure you initialize the setups by running `gcloud init`.

- Deploy application with your project ID
    ```shell
    gcloud app deploy app.yaml --project PROJECTID
    ```

- Your application should be ready shortly on `PROJECTID.appspot.com`.