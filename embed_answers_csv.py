
from sentence_transformers import SentenceTransformer, util
import csv
import read_data as rd
questions, answers, q_ids = rd.get_all_questions_answers()
import numpy

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
header = ['QID']


embeddings = model.encode(answers, convert_to_tensor=True)

cosine_scores = util.cos_sim(embeddings[0], embeddings)

embed_headers = ['QID', 'embeddings']
embed_data = []

for t in range(len(q_ids)):
    embed_data.append([q_ids[t], embeddings[t].cpu().numpy()])

with open('embedding_database.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(embed_headers)

    # write multiple rows
    writer.writerows(embed_data)