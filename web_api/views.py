from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializer, Urlserializer
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from .models import WebUrl, Urldetail
from django.views import View

# Create your views here.


class Registration(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"val": "user has created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Addlink(APIView):
    def post(self, request):
        serializer = Urlserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"url": "url has added"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        all_url = WebUrl.objects.all()
        serializer = Urlserializer(all_url, many=True)
        print(serializer.data)
        return Response(serializer.data)


class GetLinks(View):
    def get(self, request):
        getall = WebUrl.objects.all()
        return render(request, "web/linkpage.html", {"all_links": getall})


def countlink(request, id):
    url = WebUrl.objects.get(id=id)
    print(url)
    print("------------------------------------")
    db_url, created = Urldetail.objects.get_or_create(
        weburls=url, userurl=request.user)
    print(created)   # return boolean value
    if not created:
        db_url.counts += 1
    db_url.save()

    return render(request, "web/showlink.html", {"link": url})
