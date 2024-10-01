#......................
api_key = "YOUR_OPENAI_API_KEY"
#......................

from autogen import ConversableAgent, UserProxyAgent

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": api_key
}

agent_with_animal = ConversableAgent(
    "agent_with_animal",
    system_message="You are thinking of an animal. You ahve the animla 'elephant in your mind, and I will try to guess it."
    "If I guess incorrectly, give me a hint.",
    llm_config=llm_config,
    is_termination_msg=lambda msg: "elephant" in msg["content"],
    human_input_mode="NEVER"
)

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM is used for human proxy.
    human_input_mode="ALWAYS"
)

result = human_proxy.initiate_chat(
    agent_with_animal,
    message="parrot"
)
