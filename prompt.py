from langchain_core.messages import BaseMessage
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate

DEFAULT_BASE_PROMPT = """
Extract information regarding cultural heritage crime from the following text.

In particular, please provide the following information:
- A list of triplets, where each triplet consists of two entities and the relation between them. Only use the predefined relations listed below and provide detailed descriptions for each entity.

The predefined relations are:
- 'is_the_owner_of': Denotes a business relationship where an actor controls, or is the legal owner of, a business, gallery, auction house, or other for-profit organization.
- 'works_with': Denotes a business relationship between actors who are dealers, organizations, looters, or collectors.
- 'works_for': Describes an employment or contractual relationship between actors who are dealers, organizations, businesses, museums, government agencies, looters, or collectors.
- 'has_possession_of': Describes a situation where a dealer, organization, collector, or auction house controls an artefact whether through ownership or other means.
- 'purchases': Describes a situation where a dealer, organization, collector, or auction house buys an artefact.
- 'buys_from': Describes a situation where a dealer, organization, collector, or auction house buys an artefact from a named actor.
- 'sells': Describes a situation where a dealer, organization, collector, or auction house sells an artefact.
- 'donates_to': Describes a situation where a dealer, organization, collector, or auction house donates an artefact to another entity.
- 'obtains_from': Describes a situation where a dealer, organization, collector, or auction house obtains an artefact from another entity under unclear circumstances.
- 'comes_from': Describes a situation where the provenance of an artefact is attributed.
- 'has_immediate_family_member': Describes a direct familial relationship between two individuals.
- 'legal_status_change': Describes when an organization, business, person, etc., has come to the attention of law enforcement.
- 'has_role': Describes the role or roles an actor or organization can have.

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
