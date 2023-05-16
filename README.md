# Desafio Django - Django Challenge

CRUD API using Django and REST Framework

## Description

This project is a CRUD API built with Django and REST Framework. The main goal is to provide basic operations (Create, Read, Update, Delete) for two main entities: "esporte" and "time". The API allows users to manage sports and teams, associating each team with a specific sport.

The project was developed as a challenge and aims to demonstrate proficiency in building a simple API using Django and REST Framework. It follows the RESTful architectural style, providing a consistent and intuitive interface for interacting with the data.

To ensure the reliability and accuracy of the codebase, unit tests have been implemented, covering critical functionality and edge cases.

Additionally, the project includes a custom job that adds data from CSV files located in the "DATA" folder to the database. This job, implemented using Django's `BaseCommand`, can be executed manually or scheduled to run automatically on a daily basis using `django-crontab`.

To simplify the deployment process, a Docker Compose configuration has been provided, allowing users to easily set up the application along with the necessary dependencies. The project utilizes SQLite as the database for convenience, but it can be easily adapted to other databases supported by Django.


## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.
