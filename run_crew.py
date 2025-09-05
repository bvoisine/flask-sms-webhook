# run_crew.py

from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
import random
from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()


# === Tool: Breach Check ===
class BreachCheckTool(BaseTool):
    name: str = "SPY Breach Checker"
    description: str = "Checks SPY Iron Condor for breach."

    def _run(self, query: str) -> str:
        # For now, use mock data
        mock_price = 623  # Simulated SPY price
        short_call = 610
        short_put = 590

        if mock_price > short_call:
            return f"SPY is at {mock_price}, which is ABOVE the short call strike ({short_call}). ⚠️ High breach risk on call side!"
        elif mock_price < short_put:
            return f"SPY is at {mock_price}, which is BELOW the short put strike ({short_put}). ⚠️ High breach risk on put side!"
        else:
            return f"SPY is at {mock_price}, within safe bounds of 590–610. ✅ No breach detected."


# === Tool: Send SMS Stub ===
class SendSmsTool(BaseTool):
    name: str = "SendSMSAlert"
    description: str = "Sends an SMS alert (stub only for now)"

    def _run(self, message: str) -> str:
        print(f"📬 [SMS STUB]: {message}")
        return "SMS sent (stubbed)"


# === Agent ===
breach_monitor = Agent(
    role="Breach Monitor",
    goal="Detect breach risk and alert the user",
    backstory="This agent monitors spreads like SPY 590/610 for signs of breach using real or simulated data.",
    verbose=True,
    allow_delegation=False,
    tools=[BreachCheckTool(), SendSmsTool()]
)

# === Task ===
breach_check_task = Task(
    description=dedent("""
        Evaluate whether the SPY Iron Condor spread (590P/610C) is at risk of breach.
        Use the CheckSpreadRisk tool to assess price levels.
        If breach is likely, use the SendSMSAlert tool to notify the user.
        Your final output should summarize the risk status and confirm whether an alert was sent.
    """),
    agent=breach_monitor,
    expected_output="Risk summary and alert status"
)

# === Crew ===
crew = Crew(
    agents=[breach_monitor],
    tasks=[breach_check_task],
    verbose=True,
    full_output=True
)

# === Kickoff ===
if __name__ == "__main__":
    print("🐸 Launching FrogStack Breach Monitor...\n")
    result = crew.kickoff()
    print("\n🎯 Final Result:")
    print(result)
