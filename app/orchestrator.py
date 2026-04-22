import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_agent(user_input: str):
    try:
        prompt = f"""
You are an execution planning assistant.

Convert the user's intent into a structured execution plan.

User Input:
{user_input}

Return JSON in this format:
{{
  "mode": "sales | work | learning | general",
  "summary": "Short actionable summary",
  "plan": [
    {{
      "task": "Clear task",
      "time": "e.g. 9:00 AM",
      "type": "Deep Work | Execution | Review",
      "priority": 1
    }}
  ]
}}
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        content = response.choices[0].message.content.strip()

        # ✅ SAFE JSON PARSE (prevents crash)
        try:
            return json.loads(content)
        except:
            return {
                "input": user_input,
                "mode": "general",
                "summary": content,
                "plan": []
            }

    except Exception as e:
        return {
            "input": user_input,
            "mode": "error",
            "summary": f"AI error: {str(e)}",
            "plan": []
        }