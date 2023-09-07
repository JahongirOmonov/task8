
from django.shortcuts import render, get_object_or_404
from .models import allinfo, naushnik
from django.http import JsonResponse
from .serializer import allinfoSerializer, naushnikSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     all=allinfo.objects.all()
#     result=allinfoSerializer(all, many=True)
#     # for i in hammasi:
#     #     natija.append({
#     #         'name':i.name,
#     #         'count':i.count
#     #     })
#     return JsonResponse(result.data, safe=False)

class getallinfo(APIView):
    def get(self, request):
        nega = allinfo.objects.all()
        shunga=allinfoSerializer(nega, many=True)
        return Response(shunga.data)
    


def detail(request, myid):
    # each = get_object_or_404(naushnik, id=myid)
    # data={'name':each.name, 'number':each.number}
    some = naushnik.objects.filter(id=myid)
    forgett = naushnikSerializer(some, many=True)
    return JsonResponse(forgett.data, safe=False)

class postallinfo(APIView):
    def post(self, request):
        goodd=request.data
        duck = allinfoSerializer(data=goodd)
        if duck.is_valid():
            duck.save()
            return Response(duck.data)
        return Response(duck.errors)
        
