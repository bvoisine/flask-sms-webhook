# File: run_frogstack_breach_monitor.py

from crewai import Crew
from crewai_tools import tool
from langchain_community.llms import ChatOpenAI
from yaml import safe_load
import os

# Set this if you're using OpenAI-compatible models
os.environ["OPENAI_API_KEY"] = "your-key-here"

# Step 1: Load the YAML configuration
def load_crew_from_yaml(file_path: str):
    with open(file_path, "r") as f:
        data = safe_load(f)

    crew = Crew.from_yaml(data)
    return crew

# Step 2: Run the process
if __name__ == "__main__":
    yaml_path = "frogstack_breach_monitor.yaml"
    crew = load_crew_from_yaml(yaml_path)

    print(f"✅ Crew loaded: {crew.name}")
    print(f"🧠 Agents: {[agent.role for agent in crew.agents]}")

    result = crew.run()
    print("\n📣 Final Output:\n")
    print(result)
