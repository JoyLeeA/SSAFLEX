import requests
import json


file_path = "./Movies/fixtures/movie.json"
file_path2 = "./Movies/fixtures/genre.json"
file_path3 = "./Movies/fixtures/credits.json"

# API KEY 지정
apikey = "529f77b70f79db91006091c13d770c20"

# 정보를 알고 싶은 영화 리스트 만들기(번호별)
# 번호 범위 지정 <이곳만 수정>
movie_list = range(29100, 29202)

# API 지정
api = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}&language=ko&page=1®ion=KR"
api2 = "https://api.themoviedb.org/3/movie/{movies}/credits?api_key={key}&language=ko&page=1®ion=KR"


# key에러 발생 방지를 위한 메서드
class Default(dict):
    def __missing__(self, key):
        return key


result = []
credit_= []
genres = []

for idx, name in enumerate(movie_list):
    try:
        movie = {}
        credit = {}
        
        # API의 URL 구성하기
        url = api.format_map(Default(movies=name, key=apikey))
        url2 = api2.format_map(Default(movies=name, key=apikey))

        # API에 요청을 보내 데이터 추출하기
        r = requests.get(url)  
        r2 = requests.get(url2)

        # 결과를 JSON 형식으로 변환하기
        data = json.loads(r.text)
        data2 = json.loads(r2.text)

        genre_list = []
        for i in data['genres']:
            genre = {}
            genre_list.append(i['id'])
            #genre.json
            genre["pk"] = i['id']
            genre["model"] = "Movies.Genre"
            genre["fields"] = {"name": i['name']}
            if genre not in genres:
                genres.append(genre)

        #movie.json    
        movie["pk"] = data['id']
        movie["model"] = "Movies.movie"
        movie['fields'] = { "title" : data['title'], "image":data['poster_path'], "userRating":data['vote_average'], "genres":genre_list
        , "backdrop":data['backdrop_path'], "description":data['overview'], "pubDate":data['release_date'] }

        # credits.json
        actor = []
        crew = []
        fields = {"movie":data2['id']}
        credit['pk'] = idx+1
        credit['model'] = "Movies.credit"
        for l, i in enumerate(data2['cast']):
            l += 1
            if l == 7:
                break
            else:
                actor.append(i['name'])

        for l, i in enumerate(actor):
            fields['actor'+str(l+1)] = i         
   
        for i in data2['crew']:
            if i['known_for_department'] == 'Directing' and i['department'] == 'Directing':
                fields['director'] = i['name']
                break
        credit['fields'] = fields


        if movie['fields']['image'] == None or movie['fields']['backdrop']==None or movie['fields']['description'] == '':
            print('good')
        else:
            result.append(movie)
            credit_.append(credit)
    except:
        print("영화번호 " + str(name) + " 에 데이터 없음")

with open(file_path, 'w') as outfile:
    json.dump(result, outfile, ensure_ascii=False)

with open(file_path2, 'w') as outfile:
    json.dump(genres, outfile, ensure_ascii=False)

with open(file_path3, 'w') as outfile:
    json.dump(credit_, outfile, ensure_ascii=False)