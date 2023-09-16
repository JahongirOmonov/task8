from .views import GetAllNaushnik, GetDetailNaushnik, PostNaushnik, PatchNaushnik, DeleteNaushnik, AllFunctionNaushnik, PostGetNaushnik
from django.urls import path









from .views import GetAllAllinfo, PostAllinfo, GetDetailAllinfo, PatchAllinfo, DeleteAllinfo, AllFunctionAllinfo, PostGetAllinfo

urlpatterns=[
    path('GetAllAllinfo/', GetAllAllinfo.as_view()),







    path('GetDetailAllinfo/<int:pk>', GetDetailAllinfo.as_view()),







    path('PostAllinfo/', PostAllinfo.as_view() ),







    path('PatchAllinfo/<int:pk>', PatchAllinfo.as_view()),
    path('DeleteAllinfo/<int:pk>', DeleteAllinfo.as_view()),







    path('PostGetAllinfo/', PostGetAllinfo.as_view()),
    path('AllFunctionAllinfo/<int:pk>', AllFunctionAllinfo.as_view()),







    path('GetAllNaushnik/', GetAllNaushnik.as_view()),
    path('GetDetailNaushnik/<int:pk>', GetDetailNaushnik.as_view()),







    path('PostNaushnik/', PostNaushnik.as_view() ),
    path('PatchNaushnik/<int:pk>', PatchNaushnik.as_view()),







    path('DeleteNaushnik/<int:pk>', DeleteNaushnik.as_view()),







    path('PostGetNaushnik/', PostGetNaushnik.as_view()),
    path('AllFunctionNaushnik/<int:pk>', AllFunctionNaushnik.as_view())









]