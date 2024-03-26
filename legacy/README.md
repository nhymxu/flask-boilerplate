# flask-base
A boilerplate Flask RESTful API

# Requirements
- Python 3.6+
- poetry
- pyenv (optional)
- MongoDB (optional)
- Redis (optional)

# Setup
### Install poetry
```shell script
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Docs: [https://poetry.eustace.io/docs/](https://poetry.eustace.io/docs/)

### Create virtual environment for project
cd to your project directory

`cd ~/flask-base`

create virtual environment

`python3 -m venv .venv`

### Install package for virtual environment with dev package

active virtualenv

```shell script
source .venv/bin/activate
```

install requirement packages

```shell script
poetry install
```

### Run flask for dev
`python run.py`

### Test route

```
http://localhost:8000/ping
http://localhost:8000/v1/starter
```

# Test before pull request or commit

## Check code style
`flake8 app`
