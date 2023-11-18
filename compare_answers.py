import numpy as np

import chromadb
from chromadb.utils import embedding_functions
import csv
import read_data as rd
import ast
from sentence_transformers import SentenceTransformer, util
import torch


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def get_chroma_score(answer):
    chroma_client = chromadb.PersistentClient('q_a')
    # l2 squared error as default
    collection = chroma_client.get_collection(name='embed_data_new',
        embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2"))
    results = collection.query(
        query_texts=[answer],
        n_results=4
    )
    return results['distances'][0][0]

def get_cosine_score(answer):
    user_embedding = model.encode(answer, device='cpu')
    embeddings, e_ids = rd.get_embeddings()
    res_dict = {}
    res_list = []
    for t in range(len(embeddings)):
        embedding = (embeddings[t].strip('][').split(' '))
        res = [float(x) for x in embedding if len(x) > 0]
        res_dict[e_ids[t]] = res
        res_list.append(res)
    cosine_scores = util.cos_sim(user_embedding, res_list)
    return cosine_scores[0][0]

if __name__ == '__main__':
    answer = 'Anybody, anywhere, at any age, can participate in human rights education to learn about their own rights, as well as the rights of others, and how to assert them. It gives people the tools they need to cultivate the attitudes and abilities that will advance respect, equality, and dignity both locally and globally.'
    # answer = 'Human rights education is a process that anyone, anywhere can undertake at any age to learn about their own human rights -- and the rights of others -- and how to claim them. It empowers people to develop the skills and attitudes to promote equality, dignity and respect in their own communities, societies and worldwide.'
    chroma_score = get_chroma_score(answer)
    cos_score = get_cosine_score(answer)
    print (cos_score, chroma_score)

