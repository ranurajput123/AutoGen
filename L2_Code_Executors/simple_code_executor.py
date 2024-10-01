#......................
api_key = "YOUR_OPENAI_API_KEY"
#......................

from autogen import AssistantAgent, UserProxyAgent

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": api_key
}

assistant = AssistantAgent(
    "assistant",
    llm_config=llm_config
    )

user_proxy = UserProxyAgent(
    name='user',
    llm_config=llm_config,
    code_execution_config={
        "work_dir":"coding",
        "use_docker":False
        },
    human_input_mode="ALWAYS"
    )

user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of META and TESLA stock price change."
)
