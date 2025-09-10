from typing import TypedDict, Any

class FileMetadata(TypedDict):
    title: str
    description: str
    author: str
    file_path: str
    upload_date: str

class Embedding(TypedDict):
    id: str
    vector: Any
    metadata: FileMetadata