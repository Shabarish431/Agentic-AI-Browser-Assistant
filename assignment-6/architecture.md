# UI Prototype + Architecture Document

## Goal
Build a working UI shell and a clean execution pipeline for the agent system.

## UI Plan
The frontend will be a React app with three major areas:
1. Command input bar for entering user instructions.
2. Live activity log panel showing every agent step in real time.
3. User profile/settings page for editing user preferences.

## Backend Plan
The backend will use FastAPI with WebSocket support to stream live execution updates to the UI.

## Architecture Flow
UI → FastAPI → AgentExecutor → [LLM, Browser Tools, Memory] → External APIs

## Component Responsibilities
- UI: Displays commands, logs, and settings.
- FastAPI: Serves REST and WebSocket endpoints.
- AgentExecutor: Coordinates execution of each task.
- LLM: Interprets user intent and generates actions.
- Browser Tools: Perform browser-based automation steps.
- Memory: Stores and retrieves user/task context.
- External APIs: Provide outside services as needed.

## WebSocket Events
- task_started
- step_completed
- tool_used
- task_finished
- error

## Data Contracts
Use Pydantic models for:
- UserProfile
- Task
- AgentAction

## Testing Plan
Create 5 pytest tests for the intent parser:
- navigate
- fill_form
- email
- summarize
- click