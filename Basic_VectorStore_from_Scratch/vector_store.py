import numpy as np

class  VectorStore:
    def __init__(self):
        self.vector_data = {} # Dictionary to store vectors
        self.vector_index = {} # Dictionary to store index


    def _update_index(self, vector_id, vector):
        """
        Update the given index with the new vector

        :param vector_id: (str or int) This will act as an unique identifier or say index
        :param vector: (numpy array) Vector data to be added/updated at given index
        """

        # In this simple example, we use brute-force cosine similarity for indexing.
        # In simple words, here I am calculating similarity score
        # between input sentence with all other sentence present in the vector store.
        for existing_id, existing_vector in self.vector_data.items():
            similarity = np.dot(vector, existing_vector) / (np.linalg.norm(vector) * np.linalg.norm(existing_vector))
            if existing_id not in self.vector_index:
                self.vector_index[existing_id] = {}
            self.vector_index[existing_id][vector_id] = similarity

    def add_vector(self, vector_id, vector):
        """
        Add vector to the vector store.
        """
        self.vector_data[vector_id] = vector
        self._update_index(vector_id, vector)


    def get_similar_vectors(self, query_vector, num_results: 5):
        """
        Returns vectors similar to the query vector applying brute-force search
        :param query_vector: (numpy array) Input query vector
        :param num_results: (int) Number of similar results to be retunred
        :return: A list of tuples containing vector_id and similarity score
        """

        results = []
        for vector_id, vector in self.vector_data.items():
            similarity = np.dot(vector, query_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            results.append((vector_id, similarity))

        results.sort(key=lambda x: x[1], reverse=True) # Sorting based on similarity in descending order
        return results[:num_results]
