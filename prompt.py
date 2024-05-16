"""`prompt.py`"""
from langchain_core.messages import BaseMessage
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from schema import CulturalHeritageSchema, Entity, Relation, Pattern

DEFAULT_BASE_PROMPT = """
Extract information regarding cultural heritage crime from the following text. 

In particular, please provide the following information:
- A list of entities involved in the text, including their types and detailed descriptions.
- A list of relations that define how these entities interact with one another.
- A set of patterns that describe specific relational configurations between these entities, providing detailed contextual explanations.

Entities should be formatted as follows:
    {
        "name": "string",
        "description": "string"
    }

Relations should be formatted as follows:
    {
        "name": "string",
        "description": "string"
    }

Patterns should be formatted as follows:
    {
        "head": "string",
        "relation": "string",
        "tail": "string",
        "description": "string"
    }

{format_instructions}

Make sure to provide a valid and well-formatted JSON adhering to the given schema.
"""

def create_prompt(
        base_prompt: str,
        output_format: PydanticOutputParser,
        text: str
) -> list[BaseMessage]:
    """Create a prompt for the model."""

    prompt_template = HumanMessagePromptTemplate.from_template(template=base_prompt)
    chat_prompt_template = ChatPromptTemplate.from_messages(messages=[prompt_template])
    format_instructions = output_format.get_format_instructions()

    chat_prompt = chat_prompt_template.format_prompt(
        text=text,
        format_instructions=format_instructions,
    )
    
    return chat_prompt.to_messages()
