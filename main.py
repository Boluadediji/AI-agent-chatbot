from utils import *
from Tools import tools

from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.agents import ZeroShotAgent, AgentExecutor

if __name__=="__main__":

    accounts = {
        "001":{"name":"Ini", "balance":200000},
        "002":{"name":"Bolu", "balance":420000},
        "003":{"name":"Ebuks", "balance":3000000},
        "004":{"name":"Daniel", "balance":250000}
    }

    llm = azure_llm()

    # Add memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    prompt_agent = '''
    You are a banking assistant.

    You MUST follow these rules:

    1. ALWAYS classify intent *only for the very first user message in a topic*.
    2. If the user message is a follow-up (e.g., account ID, amount, card number, name, clarification):
    → DO NOT call intent classifier.
    → Continue the previous intent based on chat history.

    3. Use chat history to understand what the user is trying to complete.
    If the last user query was missing info, treat new input as that missing info.

    3b. If the user is providing info that was already given (e.g., account ID, amount):
    → Acknowledge it.

    3c. If a tool returns a failure like "Invalid account number":
    - Tell the user the account number is invalid

    4. Only call tools when:
    - You have ALL the required slots (account_id, amount, etc.)
    - The user explicitly asks for something that requires a tool

    5. If required info is missing → ask ONLY that question.
    Do not call any tool.

    6. NEVER call unsupported tool to ask a question.

    Chat history:
    {chat_history}

    Current user query: {input}

    Before responding:
    - Identify if this is the continuation of an earlier intent.
    - If yes, DO NOT classify intent again.
    - Fill the missing information and proceed.

    Respond as the agent.
    '''


    agent = ZeroShotAgent.from_llm_and_tools(
        llm=llm,
        tools=tools,
        prefix=prompt_agent,
        input_variables=["input", "chat_history", "agent_scratchpad"]
    )

    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )

    print("Chatbot is running... type 'q' to quit")

    # Continuous chat loop

    trial = 0

    while trial < 3:

        username = input("Enter your user ID: ")
        password = input("Enter your password: ")

        login_response = login(username, password)

        if login_response["status"] == "success":
            print(f"Welcome {login_response['name']}!")
            state = True
            break
        else:
            state = False
            print(login_response["message"])
            print("\nPlease try again.")
            trial += 1

    if not state:
        print("Maximum login attempts exceeded. Exiting...")

    while state:

        user_input = input("You: ")

        if user_input.lower() in ["q", "quit", "exit"]:
            print("Exiting chat...")
            break

        # Important: `input` must match the variable name in the prompt
        result = agent_executor.invoke({"input": user_input})

        print("Bot:", result["output"])
