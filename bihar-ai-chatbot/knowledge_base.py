import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

class BiharKnowledgeBase:
    def __init__(self):
        self.data = pd.read_csv('data/bihar_knowledge.csv')
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.index = self._create_faiss_index()
        
    def _create_faiss_index(self):
        embeddings = self.model.encode(self.data['question'].tolist())
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings).astype('float32'))
        return index
        
    def search(self, query, k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding).astype('float32'), k)
        return self.data.iloc[indices[0]].to_dict('records')