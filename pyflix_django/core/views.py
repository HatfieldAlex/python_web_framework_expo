import importlib.util
import os
from django.shortcuts import render

temp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp_data_storage.py'))
spec = importlib.util.spec_from_file_location("temp_data_storage", temp_file)
temp_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(temp_module)

favourite_movies = temp_module.favourite_movies

def home(request):
    return render(request, 'home.html', {'favourite_movies': favourite_movies})
