import requests
import json

API_KEY = '11006c90d072cfdcbfb249d25eb8f5ee'
BASE_URL = "https://api.themoviedb.org/3"

def create_movie_data():
    total_data = []
    for i in range(1, 2):

        # popular로 movie_id를 받고
        request_url = f'{BASE_URL}/movie/popular?api_key={API_KEY}&language=ko-KR&page={i}'
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                movie_id = movie['id']

                # 1. movie_id를 이용해 recommendations 5개 영화 받기
                recommended_five_images = []
                for j in range(1, 6):
                    request_recommendations = f'{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}&language=ko-KR&page={j}'
                    recommendations = requests.get(request_recommendations).json()
                    poster_path_results = recommendations['results']
                    if poster_path_results and poster_path_results[0]:
                        poster_path = poster_path_results[0].get('poster_path')
                        recommended_five_images.append(poster_path)
                    else:
                        continue

                # 2. movie_id를 이용해 videos API에 접근해서 key 받기
                request_video = f'{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}&language=ko-KR'
                video = requests.get(request_video).json()
                if video['results']:
                    key = video['results'][0].get('key')  # key 받기
                
                # 예고편이 없으면 빈문자열
                else:
                    continue


                # 3. movie_id를 이용해 movie_detail API에 접근해서 정보들 받기
                request_movies = f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=ko-KR'
                movie_detail = requests.get(request_movies).json()
                
                fields = {
                    'movie_id': movie_id,
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'runtime': movie_detail['runtime'],
                    'poster_paths': recommended_five_images,
                    'video_key': key,
                }

                data = {
                    'pk': movie['id'],
                    'model': 'movies.movie',
                    'fields': fields,
                }
                total_data.append(data)
    
    with open('movie_data.json', 'w', encoding="UTF-8") as f:
        json.dump(total_data, f, indent=2)
    
create_movie_data()