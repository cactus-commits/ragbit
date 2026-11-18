import lancedb # the database
from backend.constants import DATA_PATH, VECTOR_DATABASE_PATH # data path to the database
from pathlib import Path
import time
from backend.data_models import Article



# Creates a folder in the vector database and connects
def setup_vector_db(path):
    Path(path).mkdir(exist_ok=True)
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("articles", schema=Article, exist_ok=True) # create an empty  tabel called Article 

    return vector_db # Returns the vector database

# Ingest the data
def ingest_docs_to_vector_db(table):
    for file in DATA_PATH.glob("*.txt"):
        with open(file, "r") as f: # open and read the file
            content = f.read()

        doc_id = file.stem

        # idempotent - prevents that we add the same data multiple times?
        table.delete(f"doc_id = '{doc_id}'")

        table.add(
            [
                {
                    "doc_id": doc_id,
                    "filepath": str(file),
                    "filename": file.stem,
                    "content": content,
                }
            ]
        )

        print(table.to_pandas().shape)
        print(table.to_pandas()["filename"])
        time.sleep(10)



if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DATABASE_PATH)
    ingest_docs_to_vector_db(vector_db["articles"])