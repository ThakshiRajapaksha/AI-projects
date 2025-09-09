from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    model = ChatOpenAI(
    model="openai/gpt-4o-mini", 
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

    tools = []
    agent_executor = create_react_agent(model, tools)
    print("Welcome I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform caculation or chat with me")
   
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        print(f"Assistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(f"\n{message.content}", end="")

    print()  # For a new line after the response


if __name__ == "__main__":
        main()