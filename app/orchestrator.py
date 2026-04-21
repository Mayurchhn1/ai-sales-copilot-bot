from app.agents.task_agent import create_tasks
from app.agents.calendar_agent import schedule_tasks
from app.agents.research_agent import enrich_task

def run_agent(user_input):
    query = user_input.lower()

    # 🔥 Mode detection
    if "sales" in query or "client" in query or "deal" in query:
        mode = "sales"

        tasks = [
            {"task": "Call top 5 warm leads"},
            {"task": "Follow up with previous prospects"},
            {"task": "Prepare proposal for active client"},
            {"task": "Update CRM and pipeline status"}
        ]

        summary = "Focus on high-impact sales actions: outreach, follow-ups, and deal progression."

    else:
        mode = "generic"

        tasks = create_tasks(user_input)

        summary = "Structured plan generated to organize and execute your day effectively."

    # Enrich tasks
    enriched_tasks = [enrich_task(t) for t in tasks]

    # Schedule tasks
    schedule = schedule_tasks(enriched_tasks)

    return {
        "input": user_input,
        "mode": mode,
        "summary": summary,
        "plan": schedule
    }