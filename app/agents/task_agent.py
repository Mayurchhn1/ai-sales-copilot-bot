from app.db.database import add_task

def create_tasks(user_input):
    query = user_input.lower()

    tasks = []

    # Step 1: Light intent detection (NOT hardcoded behavior)
    if any(word in query for word in ["plan", "day", "schedule"]):
        tasks = [
            {"task": f"Clarify objective: {user_input}"},
            {"task": "Identify key activities required"},
            {"task": "Prioritize tasks based on impact"},
            {"task": "Allocate time for execution"},
            {"task": "Review and adjust plan"}
        ]

    elif any(word in query for word in ["learn", "study"]):
        tasks = [
            {"task": f"Define learning goal: {user_input}"},
            {"task": "Break topic into sub-topics"},
            {"task": "Study core concepts"},
            {"task": "Practice and apply knowledge"},
            {"task": "Review and summarize learnings"}
        ]

    else:
        tasks = [
            {"task": f"Analyze request: {user_input}"},
            {"task": "Break into actionable steps"},
            {"task": "Execute priority tasks"},
            {"task": "Monitor progress"},
            {"task": "Review outcomes"}
        ]

    # Step 2: Save to DB
    for t in tasks:
        add_task(t["task"], "Not Scheduled")

    return tasks