from utils import *
from Tools import tools

if __name__=="__main__":
    accounts = {
        "001":{"name":"Ini", "balance":200000},
        "002":{"name":"Bolu", "balance":420000},
        "003":{"name":"Ebuks", "balance":3000000},
        "004":{"name":"Daniel", "balance":250000}
    }

    llm = azure_llm()
    

    prompt_agent = '''
    You are a banking assistant. You MUST follow these steps:
    1. First, ALWAYS use the intentclassifier tool to understand the user's intent.
    2. Then, based on the classified intent, use the appropriate tool.
    User query: {input}
    Let's think step by step.
    If the user does not provide sufficient information, ask for it.
    '''

    agent = ZeroShotAgent.from_llm_and_tools(
        llm=llm,
        tools=tools,
        prefix=prompt_agent
    )

    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )

    result = agent_executor.invoke({"How much does it cost to procure a tesla?"})

    print(result["output"])