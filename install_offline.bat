@echo off
python -m venv venv
call venv\Scripts\activate
pip install --no-index --find-links=wheels -r requirements.txt
