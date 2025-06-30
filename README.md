# Blog 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)]()

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)


Brief summery: This project is a Web-Based application for managing a private Weblog.

## Features
- [API]: Has REST framework as the api 

## Technologies Used
- Python (3.12)**
- Django (5.2.1)**
- REST framework**

## Setup Instructions 

Follow these steps to get a copy of the project running on your local machine:

1. Clone the repository:
```bash
git clone https://github.com/AlirezaKar/weblog.git
cd weblog
```

2. Create a virtual environment and activate it:
python -m venv env
# on Windows: 
env\Scripts\activate
# on Linux:
source env/bin/activate

3. Install dependencies:
# for developers:
pip install -r requirements.txt
pip install -r requirements.dev.txt
# for end-users:
pip install -r requirements.txt

4. Run database migrations
python manage.py migrate

5. start the development server
python manage.py runserver

## Usage

- Visit http://127.0.0.1:8000
# for developers 
- To access the admin area: python manage.py createsuperuser 

## Author
- Alireza Kalaie
- Email: alirezakalaie1384@gmail.com

