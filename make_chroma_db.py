import os
import cv2
from deepface import DeepFace
from vectordb import db

# 디렉토리에서 이미지 파일명을 읽어 리스트로 만들기
image_dir = 'data/'
image_files = []
def search_files(dir):
    for file in os.listdir(dir):
        full_path = os.path.join(dir, file)
        if not file.startswith('.'):
            if os.path.isdir(dir + file):
                search_files(dir + file + '/')
            else:
                image_files.append(full_path)
search_files(image_dir)

# 이미지 파일을 읽어서 얼굴을 추출하고 임베딩을 계산하여 DB에 저장
index = 0
for image_file in image_files:
    print(image_file)
    label = image_file.split('/')[1]
    img = cv2.imread(image_file)
    result = DeepFace.represent(img_path=img, detector_backend='retinaface', model_name='Facenet512')
    print(result[0]['embedding'])
    index = index + 1
    db.add(
        ids=[str(index)],
        embeddings=[result[0]['embedding']],  # Replace with your embeddings
        metadatas=[{'name': label, 'img_path': image_file}],
    )
    
print('Done')