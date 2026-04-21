from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.orchestrator import run_agent

app = FastAPI(
    title="Multi-Agent Productivity Assistant",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ✅ CORS (required for index.html to call your API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

class TaskItem(BaseModel):
    task: str
    time: str
    type: str
    priority: int

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