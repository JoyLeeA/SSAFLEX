import requests
import json

file_path = "./Movies/fixtures/movie.json"
file_path2 = "./Movies/fixtures/genre.json"
file_path3 = "./Movies/fixtures/credits.json"

# API KEY 지정
apikey = "529f77b70f79db91006091c13d770c20"

# API 지정
api0 = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}&language=ko&page=1®ion=KR"
api = "https://api.themoviedb.org/3/discover/movie?api_key={key}&language=ko&region=KR&release_date.gte=2019-11-16&release_date.lte=2020-11-02&page={pages}"
api2 = "https://api.themoviedb.org/3/movie/{movies}/credits?api_key={key}&language=ko&page=1®ion=KR"

# key에러 발생 방지를 위한 메서드
class Default(dict):
    def __missing__(self, key):
        return key


result = []
credit_= []
genres = []
idx = 1

# 특정 기간의 페이지 구성
for page in range(1,78):
    try:
        # API의 URL 구성하기
        url = api.format_map(Default(key=apikey, pages=page))
        r = requests.get(url) 
        data = json.loads(r.text)
        for k in data['results']:
            movie = {}
            credit = {}
            genre_list = []
            url0 = api0.format_map(Default(movies= k['id'], key=apikey))
            r0 = requests.get(url0)
            data0 = json.loads(r0.text)
            for i in data0['genres']:
                genre = {}
                genre_list.append(i['id'])
                #genre.json
                genre["pk"] = i['id']
                genre["model"] = "Movies.Genre"
                genre["fields"] = {"name": i['name']}

            if genre not in genres:
                genres.append(genre)
                genre["fields"] = {"name": i['name']}

            #movie.json    
            movie["pk"] = data0['id']
            movie["model"] = "Movies.movie"
            movie['fields'] = { "title" : data0['title'], "image":data0['poster_path'], "userRating":data0['vote_average'], "genres":genre_list
            , "backdrop":data0['backdrop_path'], "description":data0['overview'], "pubDate":data0['release_date'] }

            # credits.json
            url2 = api2.format_map(Default(movies=k['id'], key=apikey))
            r2 = requests.get(url2)
            data2 = json.loads(r2.text)
            actor = []
            crew = []
            fields = {"movie":data2['id']}
            credit['pk'] = idx
            idx += 1
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
                print('fail')
            else:
                result.append(movie)
                credit_.append(credit)
    except:
        print("데이터 없음")

with open(file_path, 'w') as outfile:
    json.dump(result, outfile, ensure_ascii=False)

with open(file_path2, 'w') as outfile:
    json.dump(genres, outfile, ensure_ascii=False)

with open(file_path3, 'w') as outfile:
    json.dump(credit_, outfile, ensure_ascii=False)