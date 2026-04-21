from app.mcp.mcp_client import fetch_data

def enrich_task(task):
    task_text = task.get("task", "")
    task_lower = task_text.lower()

    try:
        info = fetch_data(task_text)

        # ✅ If MCP gives meaningful data → use it
        if info and len(info.strip()) > 20:
            context = info[:80]

        # 🔥 Sales-specific intelligence
        elif "call" in task_lower:
            context = "Focus on decision-makers and clear value proposition"

        elif "follow up" in task_lower:
            context = "Personalize message based on last interaction"

        elif "proposal" in task_lower:
            context = "Highlight ROI and client-specific benefits"

        elif "crm" in task_lower or "pipeline" in task_lower:
            context = "Ensure all deal stages are accurately updated"

        # 🧠 Generic intelligence (non-sales)
        elif "clarify" in task_lower:
            context = "Define clear outcome and success criteria"

        elif "identify" in task_lower:
            context = "List specific activities needed to move forward"

        elif "prioritize" in task_lower:
            context = "Focus on high-impact actions first"

        elif "execute" in task_lower:
            context = "Take immediate action on top priority"

        elif "review" in task_lower:
            context = "Evaluate results and refine approach"

        # ⚡ Final fallback
        else:
            context = "Maintain execution discipline"

    except Exception:
        context = "Proceed with best judgment"

    return {
        "task": f"{task_text} → {context}"
    }