import logging
from crewai import Agent, Task, Crew, Process, LLM

from .crew.flight import search_flights
from .crew.hotel import search_hotels

logger = logging.getLogger(__name__)

# Initialize LLM
# Ensure you have the model pulled locally: ollama pull llama3.1
MODEL = "ollama/llama3.1" 

llm = LLM(model=MODEL, base_url="http://localhost:11434")

# Define Agents
flight_agent = Agent(
    role="Flight Researcher",
    goal="Find optimal flights based on user criteria.",
    backstory="Expert travel agent specializing in airline networks and pricing.",
    llm=llm,
    tools=[search_flights],
    verbose=True
)

hotel_agent = Agent(
    role="Accommodation Specialist",
    goal="Find the best hotels in the destination city within the specified budget.",
    backstory="Hospitality expert with access to global hotel databases.",
    llm=llm,
    tools=[search_hotels],
    verbose=True
)

planner_agent = Agent(
    role="Itinerary Coordinator",
    goal="Compile flight and hotel options into a final travel itinerary.",
    backstory="Senior travel planner ensuring seamless trips and budget adherence.",
    llm=llm,
    verbose=True
)

# Define Tasks
flight_task = Task(
    description="Search for flights from {origin} to {destination} departing on {departure_date}.",
    expected_output="A list of flight options with prices and airlines.",
    agent=flight_agent
)

hotel_task = Task(
    description="Search for hotel options in {destination} for check-in on {departure_date} and check-out on {return_date}. Prioritize options within a budget of {budget}.",
    expected_output="A list of hotel options including their names and price per night, filtered by the specified budget.",
    agent=hotel_agent
)

planning_task = Task(
    description="Combine the flight and hotel options into a cohesive travel plan within the {budget}.",
    expected_output="A formatted travel itinerary in Markdown.",
    agent=planner_agent,
    context=[flight_task, hotel_task]
)

# Define the Crew
travel_crew = Crew(
    agents=[flight_agent, hotel_agent, planner_agent],
    tasks=[flight_task, hotel_task, planning_task],
    process=Process.sequential
)

def run_travel_crew(origin: str, destination: str, departure_date: str, return_date: str, budget: str) -> str:
    """
    Runs the travel planning CrewAI with the given inputs.
    """
    logger.info(f"Starting run_travel_crew with inputs: {origin=}, {destination=}, {departure_date=}, {return_date=}, {budget=}")
    inputs = {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "return_date": return_date,
        "budget": budget
    }
    result = travel_crew.kickoff(inputs=inputs)
    logger.info("CrewAI execution completed.")

    return result
