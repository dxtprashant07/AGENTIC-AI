# LangGraph Agentic Workflow

## Overview
This project is an agentic workflow system designed to handle a variety of tasks, including weather queries, math calculations, creative writing, travel planning, and more. It uses a modular approach with tools and agents to process and execute tasks dynamically.

## Features

### 1. Weather Queries
- **What:** Get current weather and temperature for any city.
- **How:** Uses the OpenWeatherMap API via the `WeatherTool`.
- **Example Query:** "temperature in Tokyo"

### 2. Math Calculations
- **What:** Perform basic math calculations.
- **How:** Evaluates math expressions using Python’s `eval()`.
- **Example Query:** "1234567/5678"

### 3. News Summaries
- **What:** Get the latest news headlines.
- **How:** Uses the NewsAPI (if configured) to fetch and summarize top news.
- **Example Query:** "summarize the news"

### 4. General Knowledge & Search
- **What:** Answer factual questions.
- **How:** Uses the `SearchTool` (DuckDuckGo API) to fetch web results. Falls back to the LLM if no relevant results are found.
- **Example Query:** "Who is Alan Turing?"

### 5. Creative Writing & LLM Tasks
- **What:** Write poems, stories, essays, or answer open-ended questions.
- **How:** Routes creative tasks to the LLM (HuggingFace’s flan-t5-large).
- **Example Query:** "Write a 4-line poem about artificial intelligence."

### 6. Python Code Execution
- **What:** Execute simple Python code snippets or functions.
- **How:** Uses the `PythonREPLTool` to run code and return the output.
- **Example Query:** "python print('Hello World')"

### 7. Travel Planning
- **What:** Plan trips, suggest hotels, create itineraries, and estimate costs.
- **How:** Uses the `TravelPlannerTool` to generate itineraries, suggest hotels, and calculate costs dynamically.
- **Example Query:** "Plan a 3-day trip to Goa, suggest budget hotels, and calculate total cost under ₹15,000."

### 8. Typo Correction
- **What:** Dynamically corrects typos in queries.
- **How:** Uses `pyspellchecker` to identify and correct misspelled words.
- **Example Query:** "tokyo temprateture" → "tokyo temperature"

### 9. Reflection, Logging, and Error Handling
- **What:** Logs feedback, errors, and performance metrics.
- **How:** Uses utility functions in `utils/reflection.py` to log and print relevant information for debugging and improvement.

## How It Works
1. **Input:** Enter a query (single or multiple tasks separated by commas).
2. **Planning:** The `PlanAgent` splits the query into sub-tasks.
3. **Reflection:** The system corrects typos and refines tasks.
4. **Execution:** Each task is routed to the appropriate tool (weather, search, LLM, etc.).
5. **Output:** Results for each task are displayed.

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd langgraph-agentic-workflow
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys in `.env`:
   ```plaintext
   OPENWEATHER_API_KEY=your_openweathermap_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```

4. Run the workflow:
   ```bash
   python src/langgraph_workflow.py
   ```

## Future Enhancements
- Integrate advanced APIs like Google Places or Amadeus for travel planning.
- Add support for real-time news and stock market updates.
- Improve typo correction with context-aware models.

## Contributing
Feel free to submit issues or pull requests to improve the project!