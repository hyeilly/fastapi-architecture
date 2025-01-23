# fastapi-architecture
fastapi architecture 

## directory
my-project/  
├── core-api/                   # FastAPI 라우트 및 공통 모듈  
│   ├── app/  
│   │   ├── routes/            # Fas tAPI 엔드포인트 모음    
│   │   │   ├── __init__.py  
│   │   │   └── example_route.py    
│   │   ├── services/          # 비즈니스 로직 모음    
│   │   │   ├── __init__.py  
│   │   │   └── example_service.py
│   │   ├── models/            # 데이터베이스 모델  
│   │   │   ├── __init__.py  
│   │   │   └── example_model.py  
│   │   ├── db/                # 데이터베이스 연결  
│   │   │   ├── __init__.py  
│   │   │   └── connection.py  
│   │   ├── core/              # 공통 설정 및 유틸리티  
│   │   │   ├── __init__.py  
│   │   │   ├── config.py  
│   │   │   └── middleware.py  
│   │   └── main.py            # FastAPI 진입점  
│   └── Dockerfile             # core-api용 Dockerfile  
├── logs/                      # 로그 파일 디렉토리  
│   ├── app.log  
│   └── error.log  
├── nginx/                     # Nginx 설정  
│   ├── default.conf           # Nginx 설정 파일  
│   └── Dockerfile             # Nginx용 Dockerfile  
├── requirements/              # 의존성 관리  
│   ├── base.txt               # 공통 의존성 목록  
│   ├── dev.txt                # 개발용 의존성 목록  
│   └── prod.txt               # 프로덕션용 의존성 목록  
├── docker-compose.yml         # Docker Compose 설정  
└── README.md                  # 프로젝트 설명 파일  
## Docker 실행
```
docker-compose build --no-cache

docker exec -it {container_id} bash
```