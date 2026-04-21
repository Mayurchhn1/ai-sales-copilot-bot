def enrich_task(task):
    task_text = task.get("task", "").lower()

    if "call" in task_text:
        context = "Focus on decision-makers and clear value proposition"

    elif "follow up" in task_text:
        context = "Personalize message based on last interaction"

    elif "proposal" in task_text:
        context = "Highlight ROI and client-specific benefits"

    elif "crm" in task_text:
        context = "Ensure all deal stages are accurately updated"

    elif "clarify" in task_text:
        context = "Define clear outcome and success criteria"

    elif "identify" in task_text:
        context = "List specific activities needed to move forward"

    elif "prioritize" in task_text:
        context = "Focus on high-impact actions first"

    elif "execute" in task_text:
        context = "Take immediate action on top priority"

    elif "review" in task_text:
        context = "Evaluate results and refine approach"

    else:
        context = "Maintain focus and execution discipline"

    return {
        "task": f"{task.get('task', '')} → {context}"
    }