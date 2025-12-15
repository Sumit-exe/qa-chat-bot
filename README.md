##Steps to setup project

Take a clone

open project and go to terminal inside backend folder

DO below steps:-

1.python -m venv venv 

2.venv\Scripts\Activate.ps1

3.pip install -r requirements.txt

4.uvicorn app.main:app --reload


Then use below curl:-

curl --location 'http://127.0.0.1:8000/ask' \
--header 'Content-Type: application/json' \
--data '{ "website_url": "https://example.com", "question": "What is this website about?" }'
