from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import run_agent

app = FastAPI(
    title="Multi-Agent Productivity API",
    description="AI system to manage tasks, schedules, and workflows using multiple agents",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str

class TaskItem(BaseModel):
    task: str
    time: str

class QueryResponse(BaseModel):
    input: str
    plan: list[TaskItem]

@app.get("/")
def home():
    return {"message": "Multi-Agent Productivity Assistant Running"}

@app.post("/run", response_model=QueryResponse)
def run(req: QueryRequest):
    result = run_agent(req.query)
    return result
