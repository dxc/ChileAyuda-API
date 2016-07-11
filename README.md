# ChileAyuda API

[![Build Status](https://travis-ci.org/dxc/ChileAyuda-API.svg?branch=master)](https://travis-ci.org/dxc/ChileAyuda-API)
[![Coverage Status](https://coveralls.io/repos/github/dxc/ChileAyuda-API/badge.svg?branch=master)](https://coveralls.io/github/dxc/ChileAyuda-API?branch=master)

### Develop instructions

##### 0. Use virtualenvwrapper (optional)
    # Linux / OS X
    pip install virtualenvwrapper

    # Windows
    pip install virtualenvwrapper-win

    # Create a new virtualenv
    mkvirtualenv chileayuda

    # Use virtualenv
    workon chileayuda

##### 1. COPY CONFIG FILE
    # Linux / OS X
    cp chileayuda/settings/local.py.default chileayuda/settings/local.py

    # Windows
    copy chileayuda\settings\local.py.default chileayuda\settings\local.py

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
    # Linux / OS X
    ./run_tests.sh

    # Windows
    run_tests.bat
