@echo off
call venv\Scripts\activate
pytest --browser chromium --headed
pause
