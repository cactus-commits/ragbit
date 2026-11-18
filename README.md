# ragbit

### Setup folder structure and ddependencies 

Add separate frontend and backend packages. this is neeeded when we dockerize later 

packages in backend and frontend need to be added manualy in the pyproject file instead of uv add 

""
requires-python = ">=3.13"
dependencies = ["pydantic-ai", "lancedb", "fastapi", ]


Install all dependencies
uv sync --all-packages


### Extract the data (text from pdf)
- Add the data in backend
- install pypdf in root
uv sync all packages
- add the script to extract the text [[pdf_to_text.py]] since i want to reuse it make it a function
- add the PATH in constants and import it to the script
- finish the script and export the text to the data folder as txt


### Ingestion to database
- add ingestion.py in backend 
- add the path to the db in constance (VECTOR_DATABASE_PATH = Path(__file__).parents[1] / "knowledge_base" )
- add the functions for creating table, reading data and adding it
- add the data models in data_models.py - created Article
- in the ingestion script import the Article

