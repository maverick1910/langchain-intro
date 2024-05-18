from utils.load_env import ANTHROPIC_API_KEY
from langchain_anthropic import ChatAnthropic


class ClaudeModel(object):
    @classmethod
    def claude_init(cls):
        llm = ChatAnthropic(model='claude-3-opus-20240229', api_key=ANTHROPIC_API_KEY)
        return llm
