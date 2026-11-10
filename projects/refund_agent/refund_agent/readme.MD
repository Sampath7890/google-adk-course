# 🎓 CampusX Refund Agent

An AI-powered Student Refund Management Agent built using **Google Agent Development Kit (ADK)** and Python. The agent helps students understand refund policies, check enrollment details, verify refund eligibility, submit refund requests, and track refund status through natural language conversations.

## 🚀 Project Overview

The CampusX Refund Agent is a conversational AI assistant designed to automate the student refund management process.

Instead of manually checking enrollment records and refund policies, students can interact with an AI agent that uses specialized tools to retrieve information and perform refund-related operations.

## ✨ Features

- **Refund Policy:** Retrieve and explain the refund policy.
- **Student Identification:** Identify students using their details.
- **Enrollment Details:** Retrieve a student's course enrollment information.
- **Refund Eligibility:** Check whether a student qualifies for a refund.
- **Refund Requests:** Submit refund requests through the agent.
- **Refund Tracking:** Check the current status of submitted refund requests.
- **Database Integration:** Store and retrieve student, course, and enrollment information using SQLite.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google ADK | AI agent development |
| Gemini API | LLM-powered conversations |
| SQLite | Database management |
| Python sqlite3 | Database connectivity |
| VS Code | Development environment |

## 📂 Project Structure

```text
refund_agent/
│
├── refund_agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── tools.py
│   ├── database.py
│   ├── campusx.db
│   └── .env
│
└── README.md
```

## 🧠 Agent Tools

The agent uses the following specialized tools:

| Tool | Description |
|---|---|
| `get_refund_policy()` | Retrieves refund policies |
| `identify_student()` | Identifies a student |
| `get_my_enrollments()` | Retrieves student enrollments |
| `check_refund_eligibility()` | Checks refund eligibility |
| `request_refund()` | Submits a refund request |
| `get_refund_status()` | Retrieves refund request status |

## 🗄️ Database

The project uses SQLite for storing student and course-related information.

**Database:** `campusx.db`

Main database tables:

- `students` – Student information.
- `courses` – Course information.
- `enrollments` – Enrollment details, payment information, completion percentage, and refund status.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install google-adk
```

Install any additional dependencies used by the project if required.

### 4. Configure environment variables

Create a `.env` file inside the `refund_agent` package directory.

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace the placeholder with your Gemini API key.

**Important:** Never commit API keys or other sensitive credentials to GitHub.

### 5. Run the agent

Navigate to the project directory containing the `refund_agent` package:

```bash
cd projects/refund_agent
```

Run the agent using Google ADK:

```bash
adk run refund_agent
```

## 💬 Example Interactions

**Student:** What is the refund policy?

**Agent:** I'll retrieve the refund policy and explain the applicable conditions.

**Student:** Show my enrollments.

**Agent:** I'll identify you and retrieve your enrolled courses.

**Student:** Am I eligible for a refund?

**Agent:** I'll check your enrollment details against the refund eligibility rules.

**Student:** What is my refund status?

**Agent:** I'll retrieve the current status of your refund request.

## 🎯 Learning Objectives

Through this mini project, I am exploring:

- Building AI agents using Google ADK.
- Integrating Gemini models with custom tools.
- Understanding tool calling and function execution.
- Connecting AI agents with SQLite databases.
- Implementing multi-step agent workflows.
- Building practical AI-powered applications.

## 👨‍💻 Author

**G Sampath Kumar**

B.Tech CSE (AI & ML) | Aspiring AI Engineer

- GitHub: [@Sampath7890](https://github.com/Sampath7890)

---

⭐ This project is part of my hands-on journey into Generative AI, AI Agents, and Agentic AI development.