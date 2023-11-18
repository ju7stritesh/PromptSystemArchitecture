# This file embeds the answers and saved it in a csv file which acts as a vector database (one can use Pinecone, chromadb etc.)

import read_data as rd
import chromadb
from chromadb.utils import embedding_functions

questions, answers, q_ids = rd.get_all_questions_answers()

# It is important to have persistent client for future retrievals
chroma_client = chromadb.PersistentClient('q_a')

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = chroma_client.create_collection(name="embed_data_new")
q_ids = list(map(str, q_ids))

collection.add(
  documents = answers,
  embeddings = sentence_transformer_ef(answers),
  ids = q_ids
)



