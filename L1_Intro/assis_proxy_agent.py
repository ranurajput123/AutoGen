#......................
api_key = "YOUR_OPENAI_API_KEY"
#......................

import os
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
    "user_proxy",
    llm_config=llm_config,
    code_execution_config={
        "work_dir":"code_execution",
        "use_docker":False
        },
    human_input_mode="NEVER"
    )


### Start the agents chat..............
res = user_proxy.initiate_chat(
    assistant,
    message="What is the capital of France?"
)

print(res)