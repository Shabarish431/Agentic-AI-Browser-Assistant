import asyncio

tasks = {}

async def background_agent(task_id, manager):

    tasks[task_id] = "Running"

    for step in range(1,6):
        await asyncio.sleep(2)
        await manager.send(f"Task {task_id}: Step {step}/5 completed")

    tasks[task_id] = "Completed"

    await manager.send(f"Task {task_id} Finished")