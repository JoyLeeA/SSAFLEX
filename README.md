# SSAFLIX

[TOC]

## About Our Team

> #### 김준호
>
> - 추천 알고리즘(SSAFLIX) 구현
> - 구현 모듈 통합, CSS
> - 영상 제작
>
> 
>
> #### 이종하
>
> - TMDB API 활용 데이터 생성
> - DB 구조 설계
> - Read Me 및 보고서 제작
>
> 
>
> #### 현성섭
>
> - Account 모듈 구현
> - SSAMUNITY 구현
> - 테스트 담당
>
> 

## 서비스 소개

#### demonstration video
[![Video Label](http://img.youtube.com/vi/nAp32E44Xrk/0.jpg)](https://youtu.be/nAp32E44Xrk)

* 이미지 클릭시, youtube에서 데모 영상을 시청할 수 있습니다.



### 0. 사용 방법

1. `git clone https://lab.ssafy.com/juno0810/final-pjt.git`

2. `pip install -r requirements.txt `

3. `cd Server`

4. - 번호 별로 영화를 불러오고 싶은 경우: `python getMovie_byNumber.py`
   - 기간 별로 영화를 불러오고 싶은 경우: `python getMovie_byPeriod.py`

5. `python manage.py makemigrations`

6. `python manage.py migrate`

7. `python manage.py loaddata Movies/fixtures/genre.json`

   `python manage.py loaddata Movies/fixtures/movie.json `

   `python manage.py loaddata Movies/fixtures/credits.json`

8. `python manage.py runserver`

9. Open New Terminal (or Git Bash)

10. `cd ..`

    `cd frontend`

11. `npm i`

12. `npm run serve`



### 1. 개발 도구

- django, HTML, CSS, javaScript, VisualCode, Bootstrap, python

![tools](asset/tools.png)



- Trello

![trello](asset/트렐로.png)



### 2. 영화

- 영화 목록, 페이지네이션

![추천](asset/추천.png)

*`페이지네이션`을 활용하여 평점 순으로 DB에 있는 영화들을 페이지에 당 5개씩 보여주도록 구현하였습니다.*

*오른쪽 화살표, 왼쪽화살표를 클릭하여 다른 영화를 계속 확인할 수 있습니다*



- 장르 필터

![1장르_러닝타임_개봉년대_필터](asset/장르선택.png)

![1장르_러닝타임_개봉년대_필터](asset/장르선택완료.png)

*장르에 맞춰 DB에있는 영화를 가져오도록 구현하였습니다.*



- 영화 소개 및 평점 부여

![별점](asset/별점.png)

기존 관객들이 부여했던 평점을 확인할 수 있으며, 직접 평점을 부여할 수 도 있습니다. 간단한 영화 줄거리를와 평점을 통해 사용자는 영화를 선택할 수 있습니다.



- 예고편

![예고편](asset/예고편.png)

*스크롤을 내리면, 관련 영화의 예고편을 확인할 수 있게끔 구현하였습니다.*



### 3. 커뮤니티

- 이동

![싸뮤니티](asset/싸뮤니티.png)

*SSAMUNITY 클릭 시, 영화에 대해서 토론할 수 있는 싸뮤니티 페이지로 이동합니다*



- 메인페이지

![싸뮤니티메인](asset/커뮤.png)

*SSAMUNITY 메인 페이지입니다.*



- 메뉴

![Menu](asset/Menu.png)

*메뉴 클릭시 메뉴를 확인할 수 있습니다*



- 회원가입

![회원가입](asset/회원가입.png)

회원가입 버튼을 누르면 회원가입을 할 수 있습니다.



-  로그인

![로그인](asset/로그인.png)

*회원가입시 자동으로 로그인페이지로 이동합니다.*



- 게시판

![게시판](asset/게시판.png)

*로그인이 완료되면, 자동으로 게시판으로 이동하게 됩니다*



- 글쓰기

![글쓰기](asset/글쓰기.png)

*로그인한 사용자가 글쓰기 버튼을 클릭하면 글을 작성할 수 있습니다*



- 게시글 확인

![확인](asset/확인.png)

*작성된 글을 게시판에서 확인 가능합니다*



- 게시글 세부정보 확인

![세부정보](asset/세부정보.png)

*게시글을 클릭하면, 제목, 내용, 글쓴이, 등록시간, 수정시간을 확인할 수 있습니다*



- 게시물 수정

![수정](asset/수정.png)

*수정 버튼을 누르면, 게시물의 제목과 내용을 수정할 수 있습니다*



- 게시물 수정 결과

![수정완료](asset/수정완료.png)

*수정 게시물을 저장하면, 수정된 결과를 보여줍니다*



- 댓글 작성

![댓글](asset/댓글.png)

*아래로 스크롤하면 게시물에 댓글을 작성할 수 있는 공간이 마련되어 있습니다*



- 댓글 작성

![댓글작성](asset/댓글작성.png)

*댓글 작성이 완료되면, 다음과 같이 댓글이 생성됩니다.*



### 4.관리

- 관리 페이지

![관리페이지](asset/관리페이지.png)

*django에서 기본으로 제공하는 admin-page를 활용*

*편리한 인터페이스로 구성되어있으며 간편하게 구현할 수 있어서 사용하였음*

*다음과 같은 명령으로 생성*

`python manage.py createsuperuser`



## 데이터베이스 모델링(ERD)



![ERD](asset/ERD.png)



## 느낀점

#### 김준호

- 처음 시작할때는 만만하게 생각했는데, 처음부터 끝까지 쌓아나간다는게 쉽지 않다는걸 느꼈습니다.
  만들면서도 배울 수 있는 귀중한 경험이었고, 다음에 하게 될 프로젝트에 더욱 욕심이 생기네요 ㅎㅎ
  생각한 그대로 만들 수 있는 실력을 갖고싶습니다!!!



#### 이종하

- 프로젝트를 수행하며, django와 vue.js가 모두 사용하기 편하도록 잘 만들어진 프레임워크라고 생각함과 동시에, 그럼에도 불구하고 많이 복잡하다라는 생각을 많이했습니다. 특히, 명령어 부분에서 헷갈리는 부분이 많아서 공식문서를 많이 참고하였고, 이를 통해 '준호'강사님이 말씀하셨던 공식문서를 보는 습관을 기를 수 있었던 것 같습니다. 생각보다 주어진 시간이 길지 않아서 마음이 많이 조급했지만, 팀원들과 '변승환'교수님이 있었기에 극복할 수 있었습니다. 팀원들과 함께 프로젝트를 진행하며, 개발자로서 한 걸음 더 나아갔다는 생각에 기쁩니다.

![수정](asset/변1.png)



#### 현성섭

- 프론트와 백을 각각 따로 나누어서 작성한 뒤에 연결시키는 과정을 단순하게 퍼즐을 붙이는 과정과 같이 생각하였습니다.
하지만 정말 프론트와 백을 퍼즐과 같이 만들려면 각각에 대해서 매우 정확하고 자세하게 알아야 가능하다는 것을 알게 되었습니다.
그리고 그것이 바탕이 된 다음에서야 상호간의 소통을 하면서 결합시킬 수 있다는 것과 아주 작은 한 줄의 코드로 인해서 원하는 기능을 구현하지 못하게 되고
그로인해 아주 많은 시간이 소요된다는 것을 매우 많이 느껴서, 앞으로 알게 되는 내용들에 대해서 조금 더 꼼꼼하게 정리하고 배워나가야 겠다고 다짐하게 하는 시간이었습니다.




