# WHOAMI project
이미지를 입력받아 보유한 얼굴 데이터와 비교하여 이름과 정보를 알려주는 RESTful API 서비스

# 설치방법
클론 후

가상환경 생성
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