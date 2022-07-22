# pjt0722

# 소감
- 처음 problem_a를 열었을 때는 당황했지만 자세히 들여다 보니 구조가 파악이 되어서 순조롭게 진행할 수 있었다.
- json파일과 폴더 전체를 다루는 기술에 더 친숙해져야겠다.

# 파일 구현
## problem_a
- get을 이용해 새로운 딕셔너리의 value값 지정을 해볼 수 있었다.

```python
from hashlib import new
import json
from pprint import pprint

def movie_info(movie):
    # 여기에 코드를 작성합니다.    
    movie = {'title': movie_dict.get('original_title'),    #get을 이용해 새로운 딕셔너리의 value값 지정을 해볼 수 있었다.
            'id': movie_dict.get('id'),
            'poster_path': movie_dict.get('poster_path'),
            'vote_average': movie_dict.get('vote_average'),
            'overview': movie_dict.get('overview'),
            'genre_ids': movie_dict.get('genre_ids'),
    }
    return movie



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```

## problem_b
### 구현 생각
- genre_ids 에 [18,80] 으로 출력되는 것을 [Drama,crime] 으로 바꾸는 문제
- genres_json 은 리스트이다. 그 리스트에 있는 dic에서 movie1의 'genre_ids' 의 value(list형식) 안에 숫자가 있으면 genres에 해당요소의 'name'을 append 한다.

```python
import json
from pprint import pprint


def movie_info(movie, genres):
     
    # movie1에 원하는 key값만을 다시 저장
    movie1 = {'title': movie.get('original_title'),
            'id': movie.get('id'),
            'poster_path': movie.get('poster_path'),
            'vote_average': movie.get('vote_average'),
            'overview': movie.get('overview'),
            'genre_ids': movie.get('genre_ids'),
    }
    # 새로운 리스트를 선언한다.
    genres = []
    # genres_list에서 요소를 받는다
    for i in genres_list:
    # 그 요소의 'id'의 value가 movie1의 genre_ids 안에 있으면 genres에 해당 요소의 'name'을 append한다.
        if i['id'] in movie1['genre_ids']:
            genres.append(i['name'])
    # movie1의 genres 부분을 숫자가 아닌 이름이 나오게 value를 바꿔준다.
    movie1['genre_ids'] = genres
    
    return movie1

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

```


## problem_c
- a,b 와는 다르게 더 많은 정보의 파일을 다루어야 해서 처음엔 막막했다.
- 하지만 a,b 와 형식을 맞추는 부분에 집중하여 해결할 수 있었다.

```python
import json
from pprint import pprint

def movie_info(movies, genres):
    # a,b와는 다르게 진행해야 했던 부분
    # 새로운 리스트를 만들고 그 안에 원하는 딕셔너리를 계속 추가했다.
    movie1 = [] 
    for i in movies :
        A = {'title': i.get('original_title'),
            'id': i.get('id'),
            'poster_path': i.get('poster_path'),
            'vote_average': i.get('vote_average'),
            'overview': i.get('overview'),
            'genre_ids': i.get('genre_ids'),
                }
        movie1.append(A)        
    
    # b와 동일하지만 반복이 더 필요한 부분이었다.
    # for문을 상당히 많이 사용했는데 구현할 때 많은 시행착오가 있었다.
    # for문을 줄일 수 있으면 줄이는 법을 알아봐야 할 것 같다.
    for i in range(len(movies)):   
        genres1 = []
        for j in genres:
            for k in movie1:
                if j['id'] in k['genre_ids']:
                    genres1.append(j['name'])
        movie1[i]['genre_ids'] = genres1
        
    return movie1

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

## problem_d
- 좀더 폴더 단위로 더 많은 파일로 접근해야하는 문제였다.
- 새롭게 f스트링으로 파일명에 변수를 두어 반복해서 파일을 오픈하는 법을 알았다.
- money 변수에 새로운 최고 수익 영화가 등장할 경우 수익을 기록해야하는데 값에 0을 곱하고 새 값을 더하는 방식을 골랐다.

```python
from hashlib import new
import json
from pprint import pprint

def max_revenue(movies):
    new_ML = []
    for movie in movies:
        id = movie.get('id')
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        new_ML.append(movie_list)
    

    GOAT = ''
    money = 0
    for A in new_ML:
        if A['revenue'] > money :
            money = money*0 + A['revenue']
            GOAT = A['title']
    
    return GOAT
     
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```


## problem_e
- 간단하게 12월 개봉 영화를 찾아보는 문제였다.
- 12월 만 찾는 코드를 만들었지만, 원하는 월을 입력하면 해당 월에 개봉한 영화를 찾는 방식으로 바꿔봐도 재밌을 것 같다.
  
```python
import json

def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    new_ML = []
    for movie in movies:
        id = movie.get('id')
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        new_ML.append(movie_list)    
    # release_date라는 key에서 12라는 value를 가졌다면 그 타이틀을 decfilm에 저장한다.
    decfilm = []
    for i in new_ML:
        if i['release_date'][5:7] == '12':
            decfilm.append(i['title'])
    
    return decfilm

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```

## problem_f
- 새롭게 평점을 입력하면 그 이상의 평점을 가진 영화들을 출력하는 코드를 작성해 보았다.
- 맨 아래 부분도 바꿔보아 원하는 내용을 출력할 수 있었다.
- 실제 프로그램을 만들어 보는것 같아서 재미있었다.

```python
import json


def score_movies(movies):
    new_ML = []
    for movie in movies:
        id = movie.get('id')
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        new_ML.append(movie_list)    

    film = []
    score = float(input('원하시는 평점을 입력해주세요: '))
    for i in new_ML:
        if i["vote_average"] >= score:
            film.append(i['title'])
    
    return film

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    score_result = score_movies(movies_list)
    print(f'원하시는 평점의 영화는 다음과 같습니다.\n{score_result}')

```