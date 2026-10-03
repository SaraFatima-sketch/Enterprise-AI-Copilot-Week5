import os
from openai import OpenAI

# Initialize client (Use your preferred key/provider, e.g., Groq, OpenAI, or Local LLM)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
def run_agent(agent_role, system_prompt, task_input):
    print(f"\n🤖 [{agent_role.upper()}] Processing task...")
    
    # Pre-defined outputs for local testing without paid API
    responses = {
        "CEO": "Strategy Brief: Build an Autonomous Business Operations Platform leveraging multi-agent decision pipelines.",
        "Project Manager": "Sprint Plan: 1. Architecture Setup 2. Core Modules 3. Testing 4. Deployment Docs.",
        "Research Agent": "Tech Stack Recommendation: Python 3.10+, FastAPI backend, SQLite DB, CrewAI/OpenAI orchestrator.",
        "Software Engineer": "# Core execution module\ndef process_task(task):\n    return f'Executing {task}'\n\nif __name__ == '__main__':\n    print('Engine initialized.')",
        "QA Engineer": "# Unit Tests\ndef test_process():\n    assert process_task('test') == 'Executing test'\nprint('All tests passed.')",
        "Technical Writer": "# Project Documentation\n\n## Overview\nAutonomous Business Operations Platform with multi-agent architecture.\n\n## Agents\n- CEO\n- PM\n- Researcher\n- Engineer\n- QA\n- Technical Writer"
    }
    
    output = responses.get(agent_role, f"Execution completed for {agent_role}.")
    print(f"✅ [{agent_role.upper()}] Done!\n")
    return output

def main():
    print("🚀 Starting Autonomous Business Operations Multi-Agent Workflow...")
    
    # Task 1: CEO Agent
    ceo_out = run_agent(
        "CEO", 
        "Provide strategic direction and high-level requirements.",
        "Create strategic goals for an Autonomous Business Operations Platform."
    )

    # Task 2: Project Manager Agent
    pm_out = run_agent(
        "Project Manager", 
        "Break down strategic briefs into sprint tasks.",
        f"Create a task breakdown based on this strategy:\n{ceo_out}"
    )

    # Task 3: Research Agent
    research_out = run_agent(
        "Research Agent", 
        "Provide technical library recommendations.",
        f"Research best technologies to build this system:\n{pm_out}"
    )

    # Task 4: Software Engineer Agent
    dev_out = run_agent(
        "Software Engineer", 
        "Generate clean Python code implementation.",
        f"Write core Python code based on these specs:\n{research_out}"
    )

    # Task 5: QA Agent
    qa_out = run_agent(
        "QA Engineer", 
        "Write unit tests and conduct code review.",
        f"Review and generate tests for this code:\n{dev_out}"
    )

    # Task 6: Technical Writer Agent
    writer_out = run_agent(
        "Technical Writer", 
        "Create complete project documentation.",
        f"Write a full README based on all previous outputs."
    )

    print("\n================ FINAL SYSTEM DOCUMENTATION ================\n")
    print(writer_out)

if __name__ == "__main__":
    main()