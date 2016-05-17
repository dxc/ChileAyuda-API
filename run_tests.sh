#!/bin/bash

coverage run --branch --omit="*/test*" --include=api* ./manage.py test --verbosity=2
coverage html
