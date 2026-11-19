# ragbit

![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/alex/Downloads/image.webp?version%3D1795077787120)

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


### Database
- add ingestion.py in backend 
- add the path to the db in constance (VECTOR_DATABASE_PATH = Path(__file__).parents[1] / "knowledge_base" )
- add the functions for creating table, reading data and adding it
- add the data models in data_models.py - created Article
- in the ingestion script import the Article
- run the script -> knowledbase is created 
- try to search in the database


### Create the RAG model 
Create a tool for LLM to search and fins context in the database

- import BaseModel from pydantic in data_models
- create Prompt and Response using basemodel
- create rag.py (can also be called agent) - this is both the agent and the tool it uses. The tool could also be in the mcp server
- create model.py and set the model
- imort model in rag
- create the tool - @rag_agent.tool_plain
    the tool findes the closest match and return the name, path and content of the closest document from the search. the result is sent back to the agent and is being used for the agent to draft a response to the question.


### API - serv the prompt to backend and answers to the user
- create api.py
- run api - uv run uvicorn api:app --reload
- add logfire monitoring 
    - create new logfire project
    - create a new write token and add to .env LOGFIRE_TOKEN


### Frontend
- add streamlit layout in app.py
- add assets
- try it out and check what happends in logfire

### Dockerize fronted and backend in two different containers
- create a folder fo dockerfiles and add a dockerfile for frontend and one for backend
    both files pretty similar
- create docker-compose.yaml in root - the orchestrator of both the docker containers
    - build the compose file






