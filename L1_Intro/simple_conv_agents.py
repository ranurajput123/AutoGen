#......................
api_key = "YOUR_OPENAI_API_KEY"
#......................

import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": api_key
}

agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER"
)

response = agent.generate_reply(messages=[{"role":"system", "content":"Tell me a funny joke."}])
print(response)