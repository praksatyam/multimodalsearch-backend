from daft import Daft
import numpy as np

class EmbeddingCreator:
    def __init__(self):
        self.model = Daft.load_model("path/to/your/model")  # Load your Daft model here

    def create_embedding(self, file_content):
        # Assuming file_content is a string or text data
        embedding = self.model.embed(file_content)
        return embedding.tolist()  # Convert to list for easier storage
