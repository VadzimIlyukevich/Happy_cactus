from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

import requests

api_url = "http://127.0.0.1:8000/api/"


class BaseView(View):
    def get(self, request, *args, **kwargs):
        cactuses = requests.get(api_url + "cactus").json()
        categories = requests.get(api_url + "category").json()
        return render(request, 'base.html', context={'cactuses': cactuses,
                                                     'categories': categories, })


class CactusListView(View):
    def get(self, request):
        cactuses = requests.get(api_url + "cactus").json()
        categories = requests.get(api_url + "category").json()
        return render(request, 'cactus_list.html', context={'cactuses': cactuses,
                                                            'categories': categories})


class SucculentListView(View):
    def get(self, request):
        succulents = requests.get(api_url + "succulent").json()
        categories = requests.get(api_url + "category").json()
        return render(request, 'succulent_list.html', context={'succulents': succulents,
                                                               'categories': categories})


class AboutView(View):
    def get(self, request):
        categories = requests.get(api_url + "category").json()
        return render(request, 'about.html', context={'categories': categories})


class SearchView(View):
    def get(self, request):
        categories = requests.get(api_url + "category").json()
        return render(request, 'search.html', context={'categories': categories})


class SignIn(View):
    def get(self, request):
        return render(request, 'sign_in.html')

    def post(self, request):
        if request.method == "POST":
            payload = {
                "username": request.POST['username'],
                "password": request.POST['password'],
            }
            status_code = requests.post(api_url + "register", json=payload)
            if status_code.status_code != 200:
                return redirect('user_pot')
            else:
                return HttpResponseRedirect('/')
        return render(request, 'sign_in.html', {})


class SignUp(View):
    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        if request.method == "POST":
            payload = {
                "name": request.POST['name'],
                "email": request.POST['email'],
                "password": request.POST['password'],
            }
            status_code = requests.post(api_url + "register", json=payload)
            if status_code.status_code != 200:
                return redirect('user_pot')
            else:
                return HttpResponseRedirect('/')
        return render(request, 'sign_up.html', {})


def user_pot(request):
    return render(request, 'user_pot.html')


def joke(request):
    return render(request, 'joke.html')
