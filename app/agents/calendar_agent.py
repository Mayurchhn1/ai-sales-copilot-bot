def schedule_tasks(tasks):
    time_blocks = [
        ("9:00 AM", "Deep Work"),
        ("10:30 AM", "High Priority"),
        ("12:00 PM", "Light Work"),
        ("2:00 PM", "Execution"),
        ("4:00 PM", "Review")
    ]

    scheduled = []

    for i, task in enumerate(tasks):
        task_text = task.get("task", "")
        text = task_text.lower()

        # 🔥 Smart priority logic (sales + generic)
        if "call" in text or "follow up" in text:
            priority = 3

        elif "proposal" in text:
            priority = 2

        elif "crm" in text or "pipeline" in text:
            priority = 1

        elif "clarify" in text or "analyze" in text:
            priority = 2

        elif "prioritize" in text or "execute" in text:
            priority = 3

        elif "review" in text:
            priority = 1

        else:
            priority = 1

        # ⏰ Smart time assignment (based on task type)
        if "call" in text:
            time_slot = "9:00 AM"
            block_type = "Deep Work"

        elif "follow up" in text:
            time_slot = "10:30 AM"
            block_type = "High Priority"

        elif "proposal" in text:
            time_slot = "12:00 PM"
            block_type = "Light Work"

        elif "crm" in text or "pipeline" in text:
            time_slot = "2:00 PM"
            block_type = "Execution"

        elif "review" in text:
            time_slot = "4:00 PM"
            block_type = "Review"

        else:
            # fallback rotation
            time_slot, block_type = time_blocks[i % len(time_blocks)]

        scheduled.append({
            "task": task_text,
            "time": time_slot,
            "type": block_type,
            "priority": priority
        })

    return scheduled