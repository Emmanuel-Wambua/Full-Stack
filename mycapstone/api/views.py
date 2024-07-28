from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import AttackTitan,MyHero,JujutsuKaisen
from .serializers import AttackTitanSerializer,MyHeroSerializer,JujutsuKaisenSerializer
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import AttackTitan, MyHero, JujutsuKaisen
from .serializers import AttackTitanSerializer, MyHeroSerializer, JujutsuKaisenSerializer
from rest_framework.views import APIView

class AttackTitanListCreate(generics.ListCreateAPIView):
    queryset = AttackTitan.objects.all()
    serializer_class = AttackTitanSerializer

    def delete(self, request, *args, **kwargs):
        AttackTitan.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AttackTitanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttackTitan.objects.all()
    serializer_class = AttackTitanSerializer
    lookup_field = "pk"

class AttackTitanFilterList(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("name", "")

        if name:
            # Filter the queryset based on the name
            titans = AttackTitan.objects.filter(name__icontains=name)
        else:
            # If no name is provided, return all AttackTitans
            titans = AttackTitan.objects.all()

        serializer = AttackTitanSerializer(titans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AttackTitanImageList(APIView):
    def get(self, request, *args, **kwargs):
        images = AttackTitan.objects.all()   
        serializer = AttackTitanSerializer(images, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyHeroListCreate(generics.ListCreateAPIView):
    queryset = MyHero.objects.all()
    serializer_class = MyHeroSerializer

    def delete(self, request,*args,**kwargs):
        MyHero.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MyHeroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyHero.objects.all()
    serializer_class = MyHeroSerializer
    lookup_field = "pk"

class MyHeroList(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("name", "")

        if name:
            # Filter the queryset based on the name
            blog_posts = MyHero.objects.filter(name__icontains=name)
        else:
            # If no name is provided,return all blog posts
            blog_posts = MyHero.objects.all()

        serializer = MyHeroSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MyHeroApiView(APIView):
    def get(self, request,*args,**kwargs):
        images = MyHero.objects.all()   
        serializer = MyHeroSerializer(images, context = {'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class JujutsuKaisenListCreate(generics.ListCreateAPIView):
    queryset = JujutsuKaisen.objects.all()
    serializer_class = JujutsuKaisenSerializer

    def delete(self, request,*args,**kwargs):
        JujutsuKaisen.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JujutsuKaisenRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JujutsuKaisen.objects.all()
    serializer_class = JujutsuKaisenSerializer
    lookup_field = "pk"

class JujutsuKaisenList(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("name", "")

        if name:
            # Filter the queryset based on the name
            blog_posts = JujutsuKaisen.objects.filter(name__icontains=name)
        else:
            # If no name is provided,return all blog posts
            blog_posts = JujutsuKaisen.objects.all()

        serializer = JujutsuKaisenSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class JujutsuKaisenApiView(APIView):
    def get(self, request,*args,**kwargs):
        images = JujutsuKaisen.objects.all()   
        serializer = JujutsuKaisenSerializer(images, context = {'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
