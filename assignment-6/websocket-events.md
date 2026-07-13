# WebSocket Event Format

## task_started
{
  "type": "task_started",
  "task_id": "123",
  "message": "Task execution started"
}

## step_completed
{
  "type": "step_completed",
  "task_id": "123",
  "step": "navigate",
  "message": "Browser opened"
}

## tool_used
{
  "type": "tool_used",
  "task_id": "123",
  "tool": "browser",
  "message": "Clicked submit"
}

## task_finished
{
  "type": "task_finished",
  "task_id": "123",
  "message": "Task completed"
}

## error
{
  "type": "error",
  "task_id": "123",
  "message": "Something went wrong"
}