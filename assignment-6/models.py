from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any, Literal
from datetime import datetime

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: EmailStr
    timezone: Optional[str] = "Asia/Kolkata"
    preferences: Dict[str, Any] = Field(default_factory=dict)

class Task(BaseModel):
    task_id: str
    user_id: str
    prompt: str
    status: Literal["queued", "running", "completed", "failed"] = "queued"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class AgentAction(BaseModel):
    action_type: Literal["navigate", "fill_form", "email", "summarize", "click"]
    target: Optional[str] = None
    value: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)