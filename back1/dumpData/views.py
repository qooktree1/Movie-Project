
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.models import Movie, Genre
from movies.serializers import GenreSerializer
import requests

API_KEY = '11006c90d072cfdcbfb249d25eb8f5ee'
BASE_URL = "https://api.themoviedb.org/3"

@api_view(['GET'])
def genre_data(request):
    res = requests.get(f'{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=ko')
    data = res.json()['genres']
    serializer = GenreSerializer(data=data, many=True)

    serializer.is_valid(raise_exception=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def movie_data(request):
    link = f'{BASE_URL}/movie/popular?api_key={API_KEY}&language=ko-KR&page='
    
    for tmp in Movie.objects.all():
        tmp.delete()

    # 영화 개수 1페이지당 20개
    
    for page in range(1, 21):
        res = requests.get(link+str(page))
        data_list = res.json()['results']

        for movie_data in data_list:
            movie_id = movie_data['id']

            link_detail = f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&append_to_response=videos&language=ko'
            res2 = requests.get(link_detail)

            data = res2.json()
            title = data.get('title')

            
            vote_average = data.get('vote_average')
            overview = data.get('overview')
            poster_path = data.get('poster_path')
            release_date = data.get('release_date')
            runtime = data.get('runtime')
            try:
                video_path = data.get('videos').get('results')[0].get('key')
            except:
                continue

            if not runtime or not release_date:
                continue

            movie = Movie.objects.create(id = movie_id, 
                title = title,
                release_date= release_date,
                vote_average=vote_average,
                overview=overview,
                poster_path=poster_path,
                video_path=video_path,
                runtime=runtime,
            )
            for movie_genre in data.get('genres') :
                genre = Genre.objects.get(pk=movie_genre.get("id"))
                movie.genres.add(genre)

    return Response()