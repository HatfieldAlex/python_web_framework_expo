# Python Web Framework Expo

Web frameworks are often compared in theory - with long checklists about scalability, security, and built-in features - but it’s rare to see a comparison from a **developer experience** point of view. I wanted something more hands-on. This project tries to fill that gap by comparing three of the most widely used Python web frameworks: **Django**, **FastAPI**, and **Flask**.

To explore how they *feel* to build with, I’m creating the same simple web app - a demo IMDB-style clone - in each framework. I will be approaching the builds cross sectionally and iteratively - rather than finishing the entire app in one framework before moving to the next, I’ll add a small feature to all three apps, compare the experience, then move on to the next feature. After each iteration, I will reflect and document what my experience was like. Once the app is complete in all three frameworks, I’ll summarise my overall impressions on how each framework shapes the development journey from a hands-on developer perspective.


# Python Web Framework Expo

Though web frameworks are often compared on an academic level - with robust comparisons on scalability, security, built in features etc - I feel it is rare to see a comparsion from a developer expeirnce perspective in a hands on persptice. This project is intended to fill this gap, and provide a comparison betwen arguably the min three python web frameowrks: Django, FastAPI, and Flask.

To gain a comparison of all three, I will create simple web app, a dummy IMDB clone, made by each fraemwork, and createing it iteratively in individual stages, giving commentary on each. Then at the end, I will summarisee the 'feeling' of each.


## 1. Stage 1 - Initialising a Project

The very first thing I this comparison between the frameworks was how different the “getting started” moment feels.

| Framework | Built-in project scaffolding? | Typical first step |
|-----------|------------------------------|--------------------|
| **Django** | ✅ Yes | `django-admin startproject myproject` |
| **Flask** | ❌ No | Create your own folder and `app.py` file |
| **FastAPI** | ❌ No | Create your own folder and `main.py` file |

Django could be spun up with just a single comman - `django-admin startproject` instantly led to settings, URLs, WSGI/ASGI entry points, all ready to go. By contrast, Flask and FastAPI needed to be setup manually. 

## Stage 2 – Creating a simple “Hello World” page (inline HTML response)

This stage was just about getting each framework to return a barebones HTML response — no templates, just `<h1>Hello World!</h1>` from the endpoint itself.

The main thing I noticed was that Django (WSGI) and Flask (Werkzeug) come with their own built-in development servers, so `python manage.py runserver` (Django) and `flask run` (Flask) just work out of the box. FastAPI on the other hand doesn’t ship with a server - instead I installed Uvicorn manually, the industry standard.

As usual, Django requested to run initial migrations before I could run the server. Though this is standard, it felt noticaivble heavier in this expo when compared to Flask and FastAPI directly, which had no such equivalents. 

Finally a small curiosity - Flask defaults to port 5000, while Django and FastAPI use 8000.

## Stage 3 – Moving Hello World view from inline HTML to template

Django: felt a little involved - I had to create an app, add a templates directory and HTML file, and link the app’s URL to the central URL config.

FastAPI: felt very lightweight compared to Django - I only had to add a single HTML file to make the change to a template rendering. However, already it seemed like the trade off between flexibility and scalability/robustness was evident, manually handling the HTML file path with the os module. 
