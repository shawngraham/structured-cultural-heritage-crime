"""`prompt.py`"""

from langchain_core.messages import BaseMessage
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate


DEFAULT_BASE_PROMPT = """
Who are the actors, organizations, and artefacts involved in the antiquities trade?

Make sure to provide a valid and well-formatted JSON.

"""

def create_prompt(
        base_prompt: str,
        output_format: PydanticOutputParser,
        ingredients: str,
        steps: str | None = None
)->list[BaseMessage]:
    """Create a prompt for the model."""

    prompt_template = HumanMessagePromptTemplate.from_template(template=base_prompt)
    chat_prompt_template = ChatPromptTemplate.from_messages(messages=[prompt_template])
    format_instructions = output_format.get_format_instructions()


    chat_prompt = chat_prompt_template.format_prompt(
        ingredients=ingredients, 
        steps=steps, 
        format_instructions=format_instructions,
        )
    
    return chat_prompt.to_messages()
