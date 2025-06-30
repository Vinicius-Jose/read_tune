# Read Tune
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.3%2B-blue)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange)](./LICENSE)

## 🎵 Read Tune Frontend
- This is the frontend interface for the [Read Tune API](https://github.com/Vinicius-Jose/read_tune_api), built with Django, HTML, CSS, JavaScript, and Bootstrap. It provides a user-friendly interface for interacting with the Read Tune music recommendation system.



## Where can I access ?
 - Currently, the application is not publicly accessible. It will be available online soon. If you'd like to know more, feel free to contact me here or via [Linkedin](https://www.linkedin.com/in/vin%C3%ADcius-jos%C3%A9-pierri-nogueira-341aa2175/)

 
## Which technologies were used?
 -  This project was built using:
    - Django 
    - HTML
    - CSS
    - Javascript  
    - Bootstrap 

## How to Run Locally
- Duplicate the .env.sample to a new file  .env, and follow the instructions below to edit your .env:
    - **READ_TUNE_API_URL**: The URL for Read Tune API, you can use the url metioned above, or run the API Locally by cloning the repository and following the instructions on [README.md](https://github.com/Vinicius-Jose/read_tune_api/blob/main/README.md).
    - **READ_TUNE_API_EMAIL**: The email for authentication on Read Tune API, must be registered
    - **READ_TUNE_API_PASSWORD**: Your password for the Read Tune API
    - **DJANGO_SETTINGS_MODULE**: Must be "playlist.settings".
    - **DJANGO_DEBUG**: Use this for debug , must be True(if you are using for develop) or False(for production).
    - **DJANGO_SECRET_KEY**: The secret key can be generated using the following command on your cli after run poetry install and put the returned value in your .env:
    ```bash
    poetry run python -c ‘from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())’
    ```
- **Install dependencies:**
    - You can run like any other Django Application, but firstly install poetry, on your cli:
        ```bash
        pip install poetry
        ```
    - Then, inside the folder where you downloaded this project, run:
        ```bash  
        poetry install
        ```
        This command will create a virtual environment and install all dependencies required to run.
    - Set up the database:
        - To run, you will need first start the database as any Django project, on your cli :
            ```bash
            poetry run python manage.py makemigrations read_tune
            poetry run python manage.py makemigrations 
            poetry run python manage.py migrate
            ```
    - Start the server: 
        - Development mode:
            ```bash  
            poetry run python manage.py runserver 0.0.0.0:8080
            ```
        - Production mode (ASGI with uvicorn):
        ```bash  
            poetry run uvicorn playlist.asgi:application --host 0.0.0.0 --port 8080
            ```
    - In your favorite browser open [http://127.0.0.1:8080](http://127.0.0.1:8080)
    - For more information on how to use Poetry please visit this [link](https://python-poetry.org/docs/basic-usage/).

## Running in docker
 - First build the Docker image:
    ```bash
    docker build --pull --rm -f "Dockerfile" -t read_tune:latest "."
    ```
    - Run the container:
    ```bash
    docker run -dti -p 8080:8080 --env-file .env  --name read_tune_image read_tune 
    ```
    - In your favorite browser open [http://127.0.0.1:8080](http://127.0.0.1:8080)

## 📄 License
- This project is licensed under the [Apache 2.0 License](./LICENSE).