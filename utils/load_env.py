import os
from dotenv import load_dotenv

load_dotenv()


# Langchain Models
LANGCHAIN_API_KEY = os.environ.get('LANGCHAIN_API_KEY')
LANGCHAIN_TRACING_V2 = os.environ.get('LANGCHAIN_TRACING_V2')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
