# this is a python image
FROM python:3.13-slim 
# this is where the code I want to run is.- ths is what the directory will be
WORKDIR /app

# this will copy backend to /app/backend since the line before puts us in /app
COPY backend backend

# instead of installing a package -> keep structure as it is for the imports
ENV PYTHONPATH=/app/backend

# install uv and removes cache
RUN pip install --no-cache-dir uv

# chose the directore we want to go to (where the api.py is)
WORKDIR /app/backend/src/backend

# install packages
RUN cd /app/backend && uv sync --no-dev

# runs the api
CMD ["uv", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]