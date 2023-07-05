from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    url = "https://princestudentapi.onrender.com/AddStudent//"
    response = requests.get(url)
    data = json.loads(response.text)
    return render(request, 'index.html', {'data':data})