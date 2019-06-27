# ☕ Randomised Coffee Trial
## TODO
* Route to opt-in/out people from admin
* Button to add a user
* Button to create matches for the round
* Also make it less db dependant

## Dependencies
To run this app, you'll need:
 - Python > 3.5
 - virtualenv https://virtualenv.pypa.io/en/latest/
 - Docker, with docker-compose

## Running the app
To run the development server:
```
make virtualenv
make docker-build
docker-compose up -d
```

You can then execute commands from within the container using:
```
./docker_exec.sh [COMMAND]
```

You can pull down the whole application by running:
```
docker-compose down
```

## Manage.py file
You can use the manage.py file to create the table locally and import the data.
 - `python manage.py recreate-db` will recreate the database (drop - create - commit)
 - `python manage.py add-superuser $FIRSTNAME $LASTNAME $EMAIL` will create a superuser for the given email after asking for a password
 - `python manage.py new-round` will generate a first round
 - `python manage.py import-csv` will import the data from the csv datasets. This command assumes you have the following:
    - A `datasets` folder
    - Within this folder: a `dataset.csv` and a `matches.csv` file containing the user and matches data
