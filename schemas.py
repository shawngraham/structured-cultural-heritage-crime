
"""`cultural_heritage` schema module"""

from pydantic import BaseModel, Field
from typing import List

class Entity(BaseModel):
    """Entity schema"""
    name: str = Field(
        description="The name of the entity, representing various aspects or participants in the cultural heritage and art crime domain.",
        examples=["actor", "collection", "policy", "place", "artefact", "organization", "museum", "government_agency", "business", "auction_house", "culture_group"]
    )
    description: str = Field(
        description=("'actor' A PERSON who plays a role in the cultural heritage or art crime domain. Actors ARE ALWAYS referred by their Forename Surname, e.g, 'Doe' becomes 'John Doe'. ALL PERSONS ARE ACTORS FIRST AND FOREMOST."
"'collection' A named collection of antiquities. Collections ARE ALWAYS referred to by their formal name."
"'policy' A government or organizational scheme to set a framework around aspects of the art or cultural heritage domain."
"'place' A geographic locale where an event occurs or an object comes from or an organization etc is located."
"'artefact' Objects and artworks that come from a particular culture and are bought, sold, donated, stolen, looted, traded, by dealers, museums, agencies, and other organizations."
"'organization' Non-profits and other associations. Organizations ARE ALWAYS referred to with their full formal name, e.g, 'RCMP' becomes 'Royal Canadian Mounted Police'"
"'museum' Institutions for the preservation, curation, and display of objects, museums ARE ALWAYS referred to with their full formal name, e.g., 'the MET' becomes 'The Metropolitan Museum of Art'."
"'government_agency' Government agencies ARE ALWAYS referred to with their full formal name, eg, 'IRS' becomes 'Internal Revenue Service'."
"'business' In this context they are enterprises for making money that are not auction houses or galleries. Businesses ARE ALWAYS referred to with their full formal name."
"'auction_house' An organization or gallery that facilitates the sale of artefacts between dealers and between collectors and between dealers and collectors and museums. Organizations ARE ALWAYS referred to with their full formal names."
"'culture_group' The people or cultural group to whom an artefact may be attributed, e.g., a 5th century kantharos comes from CLASSICAL GREECE."
"'place' A location where some event occurred."
"'scholar' A role subordinate to ACTOR, describing a PERSON who conducts academic or field research related to cultural heritage."
"'dealer' A role subordinate to ACTOR or ORGANIZATION, describing a PERSON or ENTITY involved in the buying and selling of artefacts."
"'collector' A role subordinate to ACTOR or ORGANIZATION, describing a PERSON or ENTITY that acquires artefacts for personal or institutional collections."
"'looter' A role subordinate to ACTOR, describing a PERSON who illegally excavates or steals cultural heritage artefacts."
"'officer' A role subordinate to ACTOR, describing a PERSON who enforces laws or regulations related to cultural heritage, such as police officers or customs agents, or holds a managerial role in a museum.'"),
    )

class Relation(BaseModel):
    """Relation schema"""
    name: str = Field(
        description="The specific name of the relationship that can exist between entities in the domain.",
        examples=["is_the_owner_of", "works_with", "works_for", "has_possession_of", "purchases", "buys_from", "sells", "donates_to", "obtains_from", "comes_from", "has_immediate_family_member", "legal_status_change", "has_role"]
    )
    description: str = Field(
        description=("'is_the_owner_of' Denotes a business relationship where an ACTOR controls, or is the legal owner of, a business, gallery, auction house, or other for-profit organization.'"
"'works_with'  Denotes a business relationship between ACTORS who are dealers, organizations, looters, or collectors.'"
"'works_for' Describes an employment or contractual relationship between ACTORS who are dealers, organizations, businesses, museums, government agencies, looters, or collectors.'"
"'has_possession_of' Describes a situation where a dealer, organization, collector, or auction house controls an artefact whether through ownership or other means.'"
"'purchases' Describes a situation where a dealer, organization, collector, or auction house buys AN ARTEFACT. e.g., John Smith purchases the Elgin Vase.'"
"'buys_from' Describes a situation where a dealer, organization, collector, or auction house buys an artefact from a NAMED ACTOR. e.g, John Smith bought from Jane Doe the Elgin Vase.'"
"'sells' Describes a situation where a dealer, organization, collector, or auction house sells AN ARTEFACT. e.g. Jane Doe sells the Elgin Vase.'"
"'donates_to' Describes a situation where a dealer, organization, collector, or auction house donates an artefact to another entity.'"
"'obtains_from' Describes a situation where a dealer, organization, collector, or auction house obtains an artefact from another entity UNDER UNCLEAR CIRCUMSTANCES.'"
"'comes_from' Describes a situation where the provenance of an artefact is attributed, e.g., a 5th century black-figure vase comes from classical Greece.'"
"'has_immediate_family_member' Describes a direct familial relationship between two individuals, including relationships by blood (e.g., parent, child, sibling) and by legal commitments such as marriage (e.g., spouse). Excludes more distant blood relationships and informal relationships like common-law partnerships UNLESS that relationship is explicitly mentioned.'"
"'legal_status_change' Describes when an organization, business, person, or so on, has come to the attention of law enforcement as when e.g., a person is charged with theft, an organization is sanctioned, an arrest warrant is issued.'"
"'has_role' Describes the role or roles an actor or organization can have, such as SCHOLAR, DEALER, COLLECTOR, LOOTER, or OFFICER.' "),
    )

class Pattern(BaseModel):
    """Pattern schema"""
    head: str = Field(
        description=("Specifies the entity type that constitutes the subject or starting point of the relationship pattern. "
                     "Examples include 'actor', 'organization', or 'artefact'. Each pattern begins with this entity."),
        examples=["actor", "organization", "artefact", "auction_house", "government_agency"]
    )
    relation: str = Field(
        description=("Defines the type of relationship that connects the head entity to the tail entity. "
                     "This field identifies the interaction or connection between entities, such as 'works_with', "
                     "'has_immediate_family_member', or 'owns'."),
        examples=["works_with", "has_immediate_family_member", "is_the_owner_of", "has_possession_of", "comes_from", "sells", "purchases", "buys_from", "legal_status_change", "has_role"]
    )
    tail: str = Field(
        description=("Specifies the entity type that constitutes the object or endpoint of the relationship pattern. "
                     "Examples include entities such as 'actor', 'business', 'artefact', or 'role'. This completes the "
                     "relationship pattern by defining what or who the head entity is connected to."),
        examples=["actor", "business", "artefact", "culture_group", "auction_house", "role"]
    )
    description: str = Field(
        description=("A detailed explanation of the specific pattern of relationships between entities. This field elaborates on "
                     "how the head and tail entities are connected through the defined relationship, providing context and examples "
                     "to illustrate typical scenarios in the cultural heritage domain."),
    )

class CulturalHeritageSchema(BaseModel):
    """Cultural Heritage Schema"""
    entities: List[Entity] = Field(
        description=("An extensive list of all entities relevant to the cultural heritage domain. "
                     "Each entity type is characterized by its unique role or representation within the domain, "
                     "from actors like individuals and organizations to artefacts, collections, and more."),
    )
    relations: List[Relation] = Field(
        description=("An exhaustive list of all possible relations that can exist amongst the different entities. "
                     "Relations define the various ways in which entities within the cultural heritage domain can interact "
                     "or be connected to one another, such as ownership, collaboration, or provenance."),
    )
    patterns: List[Pattern] = Field(
        description=("A detailed collection of patterns that describe specific relational configurations between entities. "
                     "These patterns help in understanding complex interactions and connections within the cultural heritage domain, "
                     "providing clear examples and scenarios for better comprehension."),
    )
