from agents.planner_agent import planner_agent
from agents.researcher_agent import researcher_agent
from agents.executor_agent import executor_agent
from agents.critic_agent import critic_agent

def run_workflow(task: str):

    print("\n🧠 Planning...")
    plan = planner_agent(task)

    print("\n🔎 Researching...")
    research = researcher_agent(task)

    print("\n⚙️ Executing...")
    result = executor_agent(task, research)

    print("\n🧪 Critic Review...")
    review = critic_agent(result)

    return {
        "plan": plan,
        "research": research,
        "result": result,
        "review": review
    }
