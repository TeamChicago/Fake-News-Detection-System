# HR-Recommendation-System
충북대학교 소프트웨어학과 팀 시카고의 졸업작품 과제. tessoract-OCR을 이용한 문자인식 및 분석으로 인재추천 시스템 구축.

## 팀 구성
| **이름** | **학번** |
|----------|-----|
|😃[장동혁](https://github.com/JDhyeok)|2016039049|
|😃[신한솔](https://github.com/961230)|2016039084|
|😃[황세호](https://github.com/sehoHwang)|2014041077|

## 사용 기술
![title](https://img.shields.io/badge/-Docker-2496ED?&logo=Docker&logoColor=white)  ![title](https://img.shields.io/badge/-SpringBoot-6DB33F?&logo=Spring&logoColor=white) ![title](https://img.shields.io/badge/-React-61DAFB?&logo=React&logoColor=white) ![title](https://img.shields.io/badge/-Postgresql-4479A1?&logo=Postgresql&logoColor=white) 


## 프로젝트 세팅
### 파일 구조
HR-Recommendation-System \
├── client \
├──── Dockerfile \
├── server \
├──── Dockerfile \
├── .env.pg \
├── .env.pgadmin \
├── docker-compose.yml \
└── README.md

### 환경 설정
.env 파일 설정
```python
# .env.pg
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

# .env.pgadmin
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

### 프로젝트 실행
```shell
 $ docker-compose up --build # 최초 실행
 $ docker-compose up
```