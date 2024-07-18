# My CV Django Application

## Overview
This application presents CV data as a JSON REST API and provides a CLI command to print the data to the console.

## Getting Started

### Prerequisites
- Docker
- Python 3.9

### Installation

1. Clone this repository:
```sh
git clone 'https://github.com/madjar-code/CV_API_Cegeka_Task'
cd CV_API_Cegeka_Task
```

2. Create .env file similar to .env.example, but first go to the desired directory (Django project core):
```sh
cd cv_api/cv_api
# create .env
cd ..
```

3. Build Docker image and start container by the following command:
```sh
docker compose up -d
# or
make up
```

4. To run tests with a running container you can use the `make test` command.

5. To run CLI command you can use the `make print_cv` command.

6. You can see other commands in the Makefile.
