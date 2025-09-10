# Uploading Pipeline Application

This project implements an uploading pipeline that allows users to upload files, create embeddings using Daft, store them in LanceDB vector storage, and retrieve them based on queries. 

## Project Structure

```
uploading-pipeline-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── pipeline              # Contains the uploading pipeline logic
│   │   ├── __init__.py       # Marks the pipeline directory as a package
│   │   ├── uploader.py        # Handles file uploads to S3
│   │   ├── embedding.py       # Creates embeddings from uploaded files
│   │   ├── storage.py         # Manages storage of embeddings in LanceDB
│   │   └── retrieval.py       # Handles retrieval of embeddings based on queries
│   ├── config                # Contains configuration settings
│   │   └── settings.py        # AWS S3 credentials, LanceDB connection details, etc.
│   └── types                 # Contains data types and interfaces
│       └── index.py          # Exports data types used throughout the application
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd uploading-pipeline-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure settings:**
   Update the `src/config/settings.py` file with your AWS S3 credentials and LanceDB connection details.

4. **Run the application:**
   Execute the main script to start the uploading pipeline:
   ```
   python src/main.py
   ```

## Usage

- Upload files through the designated endpoint (to be implemented).
- The application will automatically create embeddings for the uploaded files and store them in LanceDB.
- You can query the stored embeddings based on your requirements.

## Overview of the Uploading Pipeline

- **Uploader:** Handles the file upload process to S3.
- **Embedding Creator:** Uses Daft to generate embeddings from the uploaded files.
- **Storage:** Manages the storage of embeddings in LanceDB vector storage.
- **Retrieval:** Handles the retrieval of embeddings based on user queries.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.