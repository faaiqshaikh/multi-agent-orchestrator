from orchestrator.workflow_engine import run_workflow

if __name__ == "__main__":
    task = input("Enter your task: ")

    output = run_workflow(task)

    print("\n\n===== FINAL OUTPUT =====\n")
    print(output["result"])

    print("\n===== REVIEW =====\n")
    print(output["review"])
