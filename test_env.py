import yaml
from crewai import Agent, Task, Crew

from dotenv import load_dotenv
load_dotenv()


# === LOAD YAML ===
with open("frogstack_breach_monitor.yaml", "r") as f:
    config = yaml.safe_load(f)
    print("CONFIG LOADED:")
    print(config)


# === BUILD AGENTS ===
agents = {}
for a in config.get("agents", []):
    agent = Agent(
        role=a["role"],
        goal=a["goal"],
        backstory=a["backstory"],
        verbose=a.get("verbose", False),
        allow_delegation=a.get("allow_delegation", False)
    )
    agents[a["role"]] = agent

# === BUILD TASKS ===
tasks = []
for t in config.get("tasks", []):
    task = Task(
        description=t["description"],
        expected_output=t.get("expected_output"),
        agent=agents[t["agent"]]
    )
    tasks.append(task)

# === BUILD CREW ===
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    verbose=True,
    name=config.get("crew", {}).get("name", "Unnamed Crew"),
    description=config.get("crew", {}).get("description", "")
)

# === RUN ===
result = crew.kickoff()
print(result)
