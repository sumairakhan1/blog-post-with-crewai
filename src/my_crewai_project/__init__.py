# def main() -> None:
#     print("Hello from crewai!")
from my_crewai_project.flow1 import TopicOutlineFlow

if __name__ == "__main__":
    flow = TopicOutlineFlow()
    final_outline = flow.kickoff()
    print("Final Output:")
    print(final_outline)
