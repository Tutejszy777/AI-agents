# AI agents
using OpenAI API Key


### Commands for uv

DOWNLOAD PYTHON VERSION
uv python install version
INITIALIZE PROJECT
uv init .

CREATE & ACTIVATE ENV
uv venv --python 3.13
.venv\Scripts\activate 

MANAGE DEPENDENCIES
uv add langgraph langchain python-dotenv langchain-openai
uv remove
uv sync (if added manually)

RUN THE PROGRAM
uv run main.py