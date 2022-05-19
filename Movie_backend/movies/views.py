from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_list_or_404
from .models import Movie, Genre
from .serializers import MovieSerializer
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):    
    movies = get_list_or_404(Movie)
    print(movies)
    movies_serializer = MovieSerializer(data=movies, many=True)
    return Response(movies_serializer.data)