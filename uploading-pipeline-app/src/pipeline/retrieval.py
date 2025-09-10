class Retrieval:
    def __init__(self, storage):
        self.storage = storage

    def query_embeddings(self, query):
        """
        Retrieve embeddings from storage based on a user query.
        """
        results = self.storage.retrieve_embedding(query)
        return results