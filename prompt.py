from langchain_core.messages import BaseMessage
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate

DEFAULT_BASE_PROMPT = """
Extract information regarding cultural heritage crime from the following text.

In particular, please provide the following information:
- A list of triplets, where each triplet consists of two entities and the relation between them. Be sure to use only the predefined relations listed below and provide detailed descriptions for each entity.

The predefined relations are:
- 'is_the_owner_of'
- 'works_with'
- 'works_for'
- 'has_possession_of'
- 'purchases'
- 'buys_from'
- 'sells'
- 'donates_to'
- 'obtains_from'
- 'comes_from'
- 'has_immediate_family_member'
- 'legal_status_change'
- 'has_role'

{format_instructions}

Make sure to provide a valid and well-formatted JSON adhering to the given schema.

Content:
{content}

"""

def create_prompt(
        base_prompt: str,
        output_format: PydanticOutputParser,
        content: str,
)->list[BaseMessage]:
    """Create a prompt for the model."""

    prompt_template = HumanMessagePromptTemplate.from_template(template=base_prompt)
    chat_prompt_template = ChatPromptTemplate.from_messages(messages=[prompt_template])
    format_instructions = output_format.get_format_instructions()


    chat_prompt = chat_prompt_template.format_prompt(
        content=content, 
        format_instructions=format_instructions,
        )
    
    return chat_prompt.to_messages()
