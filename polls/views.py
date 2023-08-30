
from django.shortcuts import render, get_object_or_404
from .models import allinfo, naushnik
from django.http import JsonResponse

# Create your views here.

def all(request):
    natija=[]
    hammasi=allinfo.objects.all()
    for i in hammasi:
        natija.append({
            'name':i.name,
            'count':i.count
        })
    return JsonResponse(natija, safe=False)
    


def detail(request, myid):
    each = get_object_or_404(naushnik, id=myid)
    data={'name':each.name, 'number':each.number}
    return JsonResponse(data, safe=False)
        
