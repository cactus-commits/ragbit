from fastapi import FastAPI
from backend.rag import rag_agent
from backend.data_models import Prompt
import logfire


app = FastAPI()

# add logfire monitoring
logfire.configure()
logfire.instrument_pydantic_ai()
logfire.instrument_fastapi(app)



@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_agent.run(query.prompt)

    return result.output

# uv run uvicorn api:app --reload
# add /docs in the url