import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

# Load environment variables from .env file
load_dotenv()

# Configure MCP Toolset for COVID-19
covid_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://34.8.26.2.nip.io/mcp/covid-19"
    )
)

root_agent = Agent(
    model='gemini-3.5-flash',
    tools=[covid_toolset],
    name='covid_agent',
    description="An agent that retrieves COVID-19 data using an MCP server.",
    instruction=(
        "Eres un experto en datos de COVID-19. Tu objetivo es ayudar a los usuarios a obtener información sobre la pandemia. "
        "Debes responder a las consultas de los usuarios en español. "
        "Utiliza las herramientas proporcionadas por el servidor MCP para recuperar los datos necesarios. "
        "Si el usuario pregunta en español, tradúcelo internamente para llamar a las herramientas si es necesario, pero responde siempre en español. "
        "Asegúrate de proporcionar información precisa y actualizada basada en los datos recuperados."
    ),
)

if __name__ == "__main__":
    print(f"Agent '{root_agent.name}' initialized and ready.")
    print(f"Model configured: {root_agent.model}")
