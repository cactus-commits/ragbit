FROM python:3.13-slim 

# this is where the code I want to run is.- ths is what the directory will be
WORKDIR /app

# this will copy frontend to /app/frontend since the line before puts us in /app
COPY frontend frontend

# instead of installing a package -> keep structure as it is for the imports
ENV PYTHONPATH=/app/frontend

# install uv and removes cache
RUN pip install --no-cache-dir uv

# chose the directore we want to go to (where the api.py is)
WORKDIR /app/frontend/src/frontend

# install packages
RUN cd /app/frontend && uv sync --no-dev

# runs the api
CMD [ "uv" , "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]