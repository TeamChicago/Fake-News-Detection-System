# Fake-News-Detection-System
충북대학교 소프트웨어학과 팀 시카고의 졸업작품 과제.

SNS에 기사로 위장한 선동적, 자극적인 게시글로 인해 속는 사람들이 빈번하게 나타난다. 우리는 사용자가 게시글이 얼마나 신뢰도가 있는지 알게하기 위해 SOTA NLP 모델인 BERT를 활용하여 게시글이 어느정도의 신뢰도가 있는지 퍼센티지로 나타내는 웹 사이트를 만들었다.

## 팀 구성
| **이름** | **학번** |
|----------|-----|
|😃[장동혁](https://github.com/JDhyeok)|2016039049|
|😃[신한솔](https://github.com/961230)|2016039084|
|😃[황세호](https://github.com/sehoHwang)|2014041077|

## 사용 기술
![title](https://img.shields.io/badge/-Docker-2496ED?&logo=Docker&logoColor=white) ![title](https://img.shields.io/badge/-PyTorch-%23EE4C2C.svg?&logo=Pytorch&logoColor=white) 
  ![title](https://img.shields.io/badge/-SpringBoot-6DB33F?&logo=Spring&logoColor=white) ![title](https://img.shields.io/badge/-React-61DAFB?&logo=React&logoColor=white) ![title](https://img.shields.io/badge/-Postgresql-4479A1?&logo=Postgresql&logoColor=white)  ![title](https://img.shields.io/badge/-Flask-000000?&logo=Flask&logoColor=white)  
  
## 파일 구조
Fake-News-Detection-System \
├── client \
├──── Dockerfile \
├── server \
├──── Dockerfile \
├── model \
├──── (BERT MODEL.pt) \
├── .env.pg \
├── .env.pgadmin \
├── docker-compose.yml \
└── README.md

## 프로젝트 구성도
![image](https://user-images.githubusercontent.com/70086033/140952604-996ee12b-ca8f-4cc3-ba8c-8254fe4c8735.png)

## 프로젝트 세팅
### 환경 설정
- .env 파일 설정
```python
# .env.pg
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

# .env.pgadmin
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

### 모델 다운로드
- URL : https://drive.google.com/file/d/1zeW96unGCSIhaL55W_JM17k9RgfN-fVi/view?usp=sharing
- FILEID : 위 url의 id 
- FILENAME : final_model.pt
```shell
 $ cd model
 $ wget --no-check-certificate 'https://docs.google.com/uc?export=download&id={FILEID}' -O {FILENAME}
```

## 프로젝트 실행

### 웹 서버 시작
```shell
 $ docker-compose up --build # 최초 실행
 $ docker-compose up
```

### 모델 서버 시작
```shell
 $ cd model
 $ flask run
```

### 프로젝트 시연 화면
![image](https://user-images.githubusercontent.com/70086033/140952250-adcd1eb6-1573-45f4-84ef-3a2d61e4cf49.png)

## 학습 데이터 출처
- Kaggle Fake news 데이터셋

https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset
