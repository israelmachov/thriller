import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    # Basic crew with two agents using the model configured in .env.
    researcher = Agent(
        role="Researcher",
        goal="Gather concise facts about a topic.",
        backstory="You are a meticulous researcher who verifies sources quickly.",
        verbose=True,
    )

    writer = Agent(
        role="Writer",
        goal="Turn research into a short, friendly summary.",
        backstory="You write clear, engaging summaries for busy readers.",
        verbose=True,
    )

    topic = os.getenv("TOPIC", "CrewAI")

    research_task = Task(
        description=(
            "Find 3-5 bullet points about {topic}. Focus on what it is, "
            "what it is used for, and one key benefit."
        ),
        expected_output="A bullet list of 3-5 factual points.",
        agent=researcher,
    )

    writing_task = Task(
        description=(
            "Write a 3-4 sentence summary about {topic} based on the research."
        ),
        expected_output="A concise paragraph suitable for a README.",
        agent=writer,
        context=[research_task],
    )

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff(inputs={"topic": topic})
    print("\nFinal Summary:\n")
    print(result)


if __name__ == "__main__":
    main()
