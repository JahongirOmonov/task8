from django.urls import path
# from .models import naushnik, allinfo
from .views import all, detail

urlpatterns=[
    path('all/', all),
    path('detail/<int:myid>', detail)
]