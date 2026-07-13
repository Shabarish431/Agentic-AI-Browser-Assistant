# Backend API Server

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

## Endpoints

POST /command

Returns a task_id.

GET /status/{task_id}

Returns task status.

POST /user/profile

Stores user profile in SQLite.

GET /user/profile

Returns all user profiles.

WebSocket

/ws

Streams live updates while task is executing.