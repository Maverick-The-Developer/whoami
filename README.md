# WHOAMI project
이미지를 입력받아 보유한 얼굴 데이터와 비교하여 이름과 정보를 알려주는 RESTful API 서비스

# docker로 실행하기
클론 후
```sh
docker compose up -d --build
```
위 명령어로 도커 이미지를 빌드하고 콘테이너를 실행한다.  
테스트 전에  
데이터베이스를 생성하기 위해
```sh
docker ps
```
위 명령어로 whoami-app이 실행되는 컨테이너의 ID를 확인한 후  
```sh 
docker exec -it [컨테이너명 또는 컨테이너ID] /bin/sh
```
위 명령어로 shell 진입하여,
```sh
cd /app
python make_chroma_db.py
```
위 명령어들을 실행한다.  
data 디렉토리 아래 이미지들로 벡터 DB를 생성하게됨.

exit 명령으로 docker 컨테이너에서 빠져 나온 후 
http://localhost:8088/docs
브라우저를 통해 위 주소로 접속 후 테스트 한다.

# 설치방법
클론 후

가상환경 생성(python 3.12 버전)
```sh
python -m venv ./venv
```
가상환경 활성화
```sh
source ./venv/bin/activate
```
윈도우면
```sh
venv\Scripts\Activate.bat
```
> 스펠링 정확도를 확신할 수 없습니다. 웹 정보를 확인하세요.

필요한 패키지 설치
```sh
pip install -r ./requirements.txt
```

# 실행방법
윈도우인 경우
chroma.db 디렉토리(폴더)를 삭제 후 아래 명령으로 재생성함.
```sh
python make_chroma_db.py
```
chroma.db 디렉토리가 생성되고, 정상적으로 종료되면 아래명령으로
서버를 기동 시킴
```sh
python main.py
```

# API 확인
localhost:8088/docs 주소로 접속하여 확인합니다.