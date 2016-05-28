@echo off

SET SCRIPT_PATH=%~dp0

coverage run --source='.' --branch --omit="manage.py,*/test*" --include=api.* %SCRIPT_PATH%/manage.py test --verbosity=2 %*
