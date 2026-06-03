# Apigee MCP - COVID-19 Project

This project demonstrates the use of a Model Context Protocol (MCP) server to provide COVID-19 data to an AI agent.

## Project Structure

- **`covid_agent/`**: The core application. A Python-based agent developed with the Google ADK (Agent Development Kit).
- **`disease_spec.yaml` / `disease.json`**: OpenAPI specifications for the [disease.sh](https://disease.sh/) API, which provides the underlying data for the MCP server.
- **`covid-19.zip`**: Project artifacts and resources.

## Getting Started

### Prerequisites

- Python 3.12+
- A Google API Key (for the Gemini model)

### Setup

1. **Clone the repository.**
2. **Configure the agent:**
   Navigate to the `covid_agent` directory and create a `.env` file with your credentials:
   ```bash
   cd covid_agent
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```
3. **Run the agent:**
   Refer to the [covid_agent/README.md](covid_agent/README.md) for detailed instructions on how to run the agent using the ADK.

## Agent Capabilities

The COVID-19 agent is designed to:
- Retrieve real-time COVID-19 statistics (cases, deaths, recoveries).
- Provide data at global, continental, country, and US state levels.
- Support queries in Spanish.
- Use a remote MCP server to access the data tools.

## MCP Server
<
The agent connects to an MCP server at: `https://<your-host>/mcp/covid-19`

This server translates the OpenAPI definitions in `disease_spec.yaml` into tools that the LLM can use.
