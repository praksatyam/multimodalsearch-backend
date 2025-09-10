from pipeline.uploader import Uploader
from pipeline.embedding import EmbeddingCreator
from pipeline.storage import LanceDBStorage
from pipeline.retrieval import Retrieval

def main():
    # Initialize components
    uploader = Uploader()
    embedding_creator = EmbeddingCreator()
    storage = LanceDBStorage()
    retrieval = Retrieval()

    # Example usage
    file_path = "path/to/your/file"  # Replace with actual file path
    if uploader.validate_file(file_path):
        s3_url = uploader.upload_file(file_path)
        embedding = embedding_creator.create_embedding(s3_url)
        storage.store_embedding(embedding)
        print("File uploaded and embedding stored successfully.")
    else:
        print("File validation failed.")

    # Example retrieval
    query = "example query"  # Replace with actual query
    results = retrieval.query_embeddings(query)
    print("Retrieved embeddings:", results)

if __name__ == "__main__":
    main()