# ChileAyuda API

[![Build Status](https://travis-ci.org/m4droid/ChileAyuda-API.svg?branch=master)](https://travis-ci.org/m4droid/ChileAyuda-API)
[![Coverage Status](https://coveralls.io/repos/github/m4droid/ChileAyuda-API/badge.svg?branch=master)](https://coveralls.io/github/m4droid/ChileAyuda-API?branch=master)

### Develop instructions

##### 1. COPY CONFIG FILE
	# Linux / OS X
    cp chileayuda/settings.py{.default,}

    # Windows
    copy chileayuda\settings.py.default chileayuda\settings.py

##### 2. INSTALL PYTHON DEPENDENCIES
    pip install -r requirements.txt

    # Test requirements
    pip install -r requirements-test.txt

##### 3. INIT SYSTEM
	# Run DB migrations
    python manage.py migrate

    # Load fixtures
    python manage.py loaddata fixtures/regions.json
    python manage.py loaddata fixtures/provinces.json
    python manage.py loaddata fixtures/communes.json
    python manage.py loaddata fixtures/styles.json
    python manage.py loaddata fixtures/categories.json

##### 4. RUN WEB SERVICE
    python manage.py runserver

### Run tests

    ./run_tests.sh
