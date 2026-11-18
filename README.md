# ragbit



Add separate frontend and backend packages. this is neeeded when we dockerize later 

packages in backend and frontend need to be added manualy in the pyproject file instead of uv add 

""
requires-python = ">=3.13"
dependencies = ["pydantic-ai", "lancedb", "fastapi", ]


Install all dependencies
uv sync --all-packages