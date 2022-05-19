from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse


@api_view(['GET'])
def profile(request,username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(person, many=True)
    context = {
        'username': person.username,
        'email' : person.email,
    }
    print(context)
    return Response(serializer.data)
    # return JsonResponse(context)