from langchain_core.messages import HumanMessage # high level framework to build LLM applications
from langchain_openai import ChatOpenAI # allows to use OpenAI's LLMs within LangChain & langgraph
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent # complex framework to build AI agents
from dotenv import load_dotenv 

# Ai agent has a access to a set of tools

load_dotenv()

@tool
def  addition(a: float,b: float) -> str:
    """Useful for performing addition."""
    return f"The sum of {a} and {b} is {a + b}." 

@tool
def subtraction(a: float, b: float) -> str:
    """Useful for performing subtraction."""
    return f"The difference between {a} and {b} is {a - b}."

@tool
def multiplication(a: float, b: float) -> str:
    """Useful for performing multiplication."""
    return f"The product of {a} and {b} is {a * b}."

@tool
def division(a: float, b: float) -> str:
    """Useful for performing division."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return f"The quotient of {a} and {b} is {a / b}."

def main():
    model = ChatOpenAI(temperature=0)

    tools = [addition, subtraction, multiplication, division]
    agent_executor = create_react_agent(model, tools)

    print("Welcome to the AI agent. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        
        print()

if __name__ == "__main__":
    main()

