
from vector_store import VectorStore

import numpy as np

vector_store = VectorStore() # Creating an instance

# Sample strings
str_data = [
    "India is a beautiful country.",
    "This is a generation of AI.",
    "Spiritual Capital of India is Varanasi. ",
    "Generative AI (GenAI) is a broad term for artificial intelligence (AI) that can create new content."
    ]

# Tokenization and creating Vocabulary
vocabulary = set()
for sentence in str_data:
    tokens = sentence.lower().split()
    vocabulary.update(tokens)

# Assigning indices to each words
word_to_index = {word: i for i, word in enumerate(vocabulary)}

# Vectorization (Count Vectorization)
sentence_vectors = {}
for sentence in str_data:
    tokens = sentence.lower().split()
    vector = np.zeros(len(vocabulary))

    for token in tokens:
        vector[word_to_index[token]] += 1
    sentence_vectors[sentence] = vector

# Adding vector to vector store
for sentence, vector in sentence_vectors.items():
    vector_store.add_vector(sentence, vector)

# Similarity search

def similarity_search(query_sentences):
    for query_sentence in query_sentences:
        query_vector = np.zeros(len(vocabulary))
        query_tokens = query_sentence.lower().split()
        for token in query_tokens:
            if token in word_to_index:
                query_vector[word_to_index[token]] += 1

        similar_sentences = vector_store.get_similar_vectors(query_vector, num_results=3)

        print("\nQuestion: ", query_sentence)
        print("Similar sentences are: ")
        for sentence, similarity in similar_sentences:
            print(f"{sentence}: Similarity = {similarity:.4f}")



similarity_search(["What is the capital of India?", "Is Generative AI (GenAI) and AI are same?"])
