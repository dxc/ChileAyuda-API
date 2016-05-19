#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

coverage run --source='.' --branch --omit="manage.py,*/test*" --include=api.* $DIR/manage.py test --verbosity=2 $@
coverage html
