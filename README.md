# Jabora: AI Travel Orchestrator

Jabora is an intelligent travel assistant that uses a multi-agent orchestration framework to help users plan their perfect trip. It combines an interactive intake chatbot with a specialized research crew to provide comprehensive travel itineraries, including flights and hotels.

## 🚀 Features

*   **Intelligent Intake Agent:** A conversational interface that identifies and extracts trip requirements (origin, destination, dates, budget, etc.) using structured output.
*   **Multi-Agent Research Crew:** Powered by **CrewAI**, the system employs specialized agents to research:
    *   **Flight Specialist:** Finds the best flight options.
    *   **Hotel Expert:** Identifies top-rated accommodations within budget.
    *   **Travel Planner:** Synthesizes all information into a cohesive Markdown itinerary.
*   **Structured Data Extraction:** Uses Pydantic and LangChain to ensure all necessary information is collected before starting the research phase.
*   **Local LLM Support:** Configured to run locally using **Ollama** and **Llama 3.1**.

## 🛠️ Tech Stack

*   **Language:** Python
*   **Orchestration:** [CrewAI](https://www.crewai.com/)
*   **LLM Framework:** [LangChain](https://www.langchain.com/)
*   **Model Provider:** [Ollama](https://ollama.com/) (Llama 3.1)
*   **Data Validation:** [Pydantic](https://docs.pydantic.dev/)

## ⚙️ Installation

### Prerequisites

*   Python 3.10+
*   [Ollama](https://ollama.com/) installed and running.
*   Llama 3.1 model downloaded: `ollama pull llama3.1`

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/jabora.git
    cd jabora
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # Linux/Mac
    source .venv/bin/activate
    # Windows
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add any necessary configurations (if applicable).

## 🚀 Usage

To start the interactive travel assistant, run:

```bash
python src/jabora/chat.py
```

1.  Chat with the assistant to provide your trip details.
2.  Once all information is collected, the assistant will automatically trigger the research crew.
3.  Wait for the crew to synthesize your personalized itinerary.

## 📁 Project Structure

```text
jabora/
├── src/
│   └── jabora/
│       ├── crew/               # Agent definitions
│       │   ├── flight.py
│       │   └── hotel.py
│       ├── chat.py             # Main entry point (Chatbot)
│       ├── config.py           # Configuration and logging
│       └── travel_orchestrator.py # CrewAI orchestration logic
├── docs/                       # Documentation and planning
├── tests/                      # Unit and integration tests
└── requirements.txt            # Project dependencies
```

## 📄 License

This project is licensed under the MIT License.
