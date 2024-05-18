from fastapi import APIRouter
from models.gemini_model import GeminiModel
from models.anthropic_model import ClaudeModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

router = APIRouter()
gemini_llm = GeminiModel.gemini_init()
claude_llm = ClaudeModel.claude_init()

parser = StrOutputParser()


@router.post("/message")
def get_message(user_input: dict):
    template = f"""
    What is the ideal weight for the certain individual profile with clear explanation
        Age : {user_input['age']}
        Gender : {user_input['gender']}
    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | claude_llm | parser

    result = chain.invoke(user_input)
    return {
        'status': "200",
        'data': result
    }
