import uuid
import asyncio

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi import Depends

from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import SessionLocal

from models import User
from schemas import UserCreate
from schemas import Command

from websocket_manager import manager
from tasks import background_agent
from tasks import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/command")
async def command(data: Command):

    task_id = str(uuid.uuid4())

    asyncio.create_task(
        background_agent(task_id, manager)
    )

    return {
        "task_id": task_id
    }


@app.get("/status/{task_id}")
def status(task_id: str):

    return {
        "task_id": task_id,
        "status": tasks.get(task_id, "Not Found")
    }


@app.post("/user/profile")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        address=user.address,
        resume_text=user.resume_text
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Saved"}


@app.get("/user/profile")
def get_users(db: Session = Depends(get_db)):

    return db.query(User).all()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)