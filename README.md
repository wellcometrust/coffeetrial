# ☕ Randomised Coffee Trial
## How to install this code

This repository uses Pipenv, if you don't have it, you can find install instructions here:
 - https://pipenv.readthedocs.io/en/latest/

Once you installed pipenv, just run `pipenv install` to install the requirements.
This project uses SQLalchemy, and requires you to setup the database url in the config file.
The configuration can be selected by exporting the `APP_SETTINGS` environment variable and settings it to one of these:
 - `config.DevelopmentConfig`
 - `config.ProductionConfig`
 - `config.TestingConfig`

You can add a local configuration is you feel the need, but please be sure not to push it on this repository.

## Manage.py file
You can use the manage.py file to create the table locally and import the data.
 - `python manage.py recreate_db` will recreate the database (drop - create - commit)
 - `python manage.py import_from_csv` will import the data from the csv datasets. This command assumes you have the following:
    - A `datasets` folder
    - Within this folder: a `dataset.csv` and a `matches.csv` file containing the user and matches data

## Build and Serve front end
The front end is built in react. Cd into the frontend folder. To build and then serve:
- `cd frontend`
- `npm i`
- `npm run build`
- In a different terminal run `pipenv shell`
- `python manage.py run`
- Go to localhost:5000
If you make any changes you have to rebuild and then restart the flask server. 
