from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.orchestrator import run_agent
import logging

# ✅ Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Multi-Agent Productivity Assistant",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ✅ CORS (required for UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class QueryRequest(BaseModel):
    query: str

# ✅ Response models
class TaskItem(BaseModel):
    task: str
    time: str
    type: str
    priority: int

class QueryResponse(BaseModel):
    input: str
    mode: str
    summary: str
    plan: list[TaskItem]

# ✅ Root endpoint (health + info)
@app.get("/")
def home():
    return {
        "status": "running",
        "app": "FlowPlan AI",
        "version": "2.0.0",
        "message": "AI execution planning API is live 🚀",
        "endpoints": {
            "docs": "/docs",
            "run": "/run"
        }
    }

# ✅ Main AI endpoint (WITH logging)
@app.post("/run", response_model=QueryResponse)
def run(req: QueryRequest):
    try:
        return run_agent(req.query)

    except Exception as e:
        # 🔴 Logs visible in Render logs
        logger.error(f"Error in /run: {str(e)}")

        # 🟢 Safe response to user
        return {
            "input": req.query,
            "mode": "error",
            "summary": "Something went wrong. Please try again.",
            "plan": []
        }