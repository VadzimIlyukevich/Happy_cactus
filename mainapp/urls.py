from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('cactus/', CactusListView.as_view(), name='cactus'),
    path('succulent/', SucculentListView.as_view(), name='succulent'),
    path('about/', AboutView.as_view(), name='about'),
    path('search/', SearchView.as_view(), name='search'),
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    path('sign_up/', SignUp.as_view(), name='sign_up'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user_pot/', user_pot, name='user_pot'),
    path('joke/', joke, name='joke'),
    url('', include('social_django.urls', namespace='social')),
]
