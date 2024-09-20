from numpy import ndarray
from deepface import DeepFace
from vectordb import db

THRESHOLD = 0.3

async def search_face(image: str | ndarray): 
    embedding = DeepFace.represent(img_path=image, detector_backend='retinaface', model_name='Facenet512')
    results = db.query(
        query_embeddings=[embedding[0]['embedding']],
        n_results=1
    )

    # id = results['ids'][0][0]
    distance = results['distances'][0][0]
    metadata = results['metadatas'][0][0]

    bFound = distance < THRESHOLD

    if bFound:
        # 아는 얼굴
        return { 'found': True, 'distance': distance, 'name': metadata['name'], 'img_path': metadata['img_path'] }
    else:
        # 모르는 얼굴
        return { 'found': False,'distance': distance, 'name': '', 'img_path': '' }