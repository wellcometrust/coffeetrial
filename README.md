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
./docker_exec.sh python manage.py recreate-db
```

You can then execute commands from within the container using:
```
./docker_exec.sh [COMMAND]
```

## Manage.py file
You can use the manage.py file to create the table locally and import the data.
 - `python manage.py recreate-db` will recreate the database (drop - create - commit)
 - `python manage.py import-csv` will import the data from the csv datasets. This command assumes you have the following:
    - A `datasets` folder
    - Within this folder: a `dataset.csv` and a `matches.csv` file containing the user and matches data

## Build and Serve front end

The current version left the frontend behind to focus on primarily useful features.
The old front end can still be used, though:

The front end is built in react. Cd into the frontend folder. To build and then serve:
- `cd frontend`
- `npm i`
- `npm run build`
- In a different terminal run `pipenv shell`
- `python manage.py run`
- Go to localhost:5000
If you make any changes you have to rebuild and then restart the flask server.
