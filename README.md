![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Deployment](https://img.shields.io/badge/Deployed-Render-blue)

# 🚀 Multi-Agent Productivity Assistant

🌐 Live Demo: https://multi-agent-productivity-assistant-y8sv.onrender.com  
📄 API Docs: https://multi-agent-productivity-assistant-y8sv.onrender.com/docs  
 
---

## 🚀 What This Project Solves

Sales and business professionals lose time managing follow-ups, planning workdays, and organizing tasks.

This AI-powered multi-agent system automates:
- Workday planning
- Sales follow-ups
- Task prioritization

It acts like a virtual assistant that thinks, plans, and executes workflows.

💡 Designed to scale with real-world integrations like CRM, WhatsApp, and Calendar using MCP-style architecture.
---

## 💼 Real Use Cases

### 1. Sales Follow-up Planning
Input: "Plan my follow-up calls"

Output:
- Call warm leads (10 AM)
- Send proposals (2 PM)
- Check pending replies (5 PM)

---

### 2. Daily Productivity Planning
Input: "Plan my workday"

Output:
- Emails (9 AM)
- Meetings (1 PM)
- Deep Work (6 PM)

---

## 🔷 Problem Statement

Build a system that:
- Manages tasks and schedules  
- Uses multiple tools and data sources  
- Executes multi-step workflows  
- Provides API-based interaction  

---

## 🔷 Solution Overview

A modular **multi-agent architecture**:

- 🧠 Orchestrator Agent – controls workflow  
- 📋 Task Agent – generates tasks  
- 📅 Calendar Agent – schedules tasks  
- 🔎 Research Agent – enriches tasks  

---

## 🔷 Architecture

User → API (/run) → Orchestrator → Agents → Structured Output

---

## 🔷 Tech Stack

- Python  
- FastAPI  
- SQLite  
- Requests  
- Multi-Agent Architecture  

---

## 🔷 API Endpoint

### POST /run

#### Input:
```json
{
  "query": "Plan my workday"
}
```

#### Output:
```json
{
  "input": "Plan my workday",
  "plan": [
    {"task": "Emails", "time": "9:00 AM"},
    {"task": "Meetings", "time": "1:00 PM"},
    {"task": "Deep Work", "time": "6:00 PM"}
  ]
}
```
