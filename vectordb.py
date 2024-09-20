import chromadb

client = chromadb.PersistentClient('./chroma.db')
db = client.get_or_create_collection(
    name='facedb',
    metadata={
        "hnsw:space": 'cosine',
    },
)