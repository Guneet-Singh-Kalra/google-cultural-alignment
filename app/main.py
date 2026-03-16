import uuid
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from .database import db
from .ai_engine import GCA_Agent
import google.generativeai as genai

app = FastAPI()
agent = GCA_Agent()
sessions = {}

class CandidateCreate(BaseModel):
    name: str
    email: str
    role: str

@app.post("/hr/create-candidate")
async def create_candidate(candidate: CandidateCreate):
    magic_id = str(uuid.uuid4())
    db.collection("candidates").document(magic_id).set({
        "name": candidate.name,
        "email": candidate.email,
        "role": candidate.role,
        "status": "Profile Building Initiated",
        "isHiPo": False
    })
    return {"magic_link": f"http://localhost:8000/start?id={magic_id}"}

@app.post("/chat/{magic_id}")
async def chat_with_coach(magic_id: str, message: str = Body(..., embed=True)):
    doc_ref = db.collection("candidates").document(magic_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Invalid Session")

    if magic_id not in sessions:
        sessions[magic_id] = agent.model.start_chat(history=[])
        sessions[magic_id].send_message(agent.system_instructions)

    response_text = agent.get_chat_response(sessions[magic_id], message)
    
    # Update status to In-Progress
    doc_ref.update({"status": "Profile Building In-Progress"})
    
    return {"response": response_text}