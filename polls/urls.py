from django.urls import path
# from .models import naushnik, allinfo
from .views import getallinfo, postallinfo, detail

urlpatterns=[
    path('all/', getallinfo.as_view()),
    path('detail/<int:myid>', detail),
    path('create/', postallinfo.as_view())
]