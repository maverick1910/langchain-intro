import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get('ANTHROPIC_API_KEY'))
# Langchain Models
LANGCHAIN_API_KEY = os.environ.get('LANGCHAIN_API_KEY')
LANGCHAIN_TRACING_V2 = os.environ.get('LANGCHAIN_TRACING_V2')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')
OPEN_AI_ORG_ID = os.environ.get('OPEN_AI_ORG_ID')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
