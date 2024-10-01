from autogen import AssistantAgent

assistant = AssistantAgent(
    "coding_agent",
    llm_config={
        "cache_seed":None,
        "config_list":OAI_CONFIG_LIST,
        "max_tokens":1024
    }
)

#........................
# None = disable caching
# 41 = default
#........................