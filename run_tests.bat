@echo off

SET SCRIPT_PATH=%~dp0
SET DJANGO_SETTINGS_MODULE=chileayuda.settings.test

coverage run --source="." --branch --omit="manage.py,*/test*" --include=api.* %SCRIPT_PATH%/manage.py test --verbosity=2 %*
coverage html
