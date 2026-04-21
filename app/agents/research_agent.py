def enrich_task(task):
    # Handle both dict and string
    if isinstance(task, dict):
        task_text = task.get("task", "")
    else:
        task_text = str(task)

    task_text_lower = task_text.lower()

    if "call" in task_text_lower:
        context = "Focus on decision-makers and clear value proposition"

    elif "follow up" in task_text_lower:
        context = "Personalize message based on last interaction"

    elif "proposal" in task_text_lower:
        context = "Highlight ROI and client-specific benefits"

    elif "crm" in task_text_lower:
        context = "Ensure all deal stages are accurately updated"

    elif "clarify" in task_text_lower:
        context = "Define clear outcome and success criteria"

    elif "identify" in task_text_lower:
        context = "List specific activities needed to move forward"

    elif "prioritize" in task_text_lower:
        context = "Focus on high-impact actions first"

    elif "execute" in task_text_lower:
        context = "Take immediate action on top priority"

    elif "review" in task_text_lower:
        context = "Evaluate results and refine approach"

    else:
        context = "Maintain focus and execution discipline"

    return {
        "task": f"{task_text} → {context}"
    }