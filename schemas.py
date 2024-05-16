"""`cultural_heritage` schema module"""

from pydantic import BaseModel, Field
from typing import List
from enum import Enum


# Define RelationType Enum
class RelationType(str, Enum):
    is_the_owner_of = 'is_the_owner_of'
    works_with = 'works_with'
    works_for = 'works_for'
    has_possession_of = 'has_possession_of'
    purchases = 'purchases'
    buys_from = 'buys_from'
    sells = 'sells'
    makes_sale_to = "makes_sale_to"
    donates_to = 'donates_to'
    obtains_from = 'obtains_from'
    comes_from = 'comes_from'
    has_immediate_family_member = 'has_immediate_family_member'
    legal_status_change = 'legal_status_change'
    has_role = 'has_role'


class Entity(BaseModel):
    """Entity schema"""
    name: str = Field(
        description="The name of the entity, representing various participants in the cultural heritage and art crime domain.",
        examples=[
            "John Doe -- an actor",
            "Ancient Greek Vase -- an artefact",
            "The Metropolitan Museum of Art -- a museum",
            "Royal Canadian Mounted Police -- an organization",
            "Internal Revenue Service -- a government agency"
        ]
    )


class Relation(BaseModel):
    """Relation schema"""
    name: RelationType = Field(description="The specific name of the relationship that can exist between entities in the domain.")


class Triplet(BaseModel):
    """Triplet schema to represent entity-relation-entity structure"""
    entity1: Entity = Field(description="The first entity in the triplet.")
    relation: Relation = Field(description="The relation connecting the first and second entities.")
    entity2: Entity = Field(description="The second entity in the triplet.")


class CulturalHeritageSchema(BaseModel):
    """Cultural Heritage Schema"""
    triplets: List[Triplet] = Field(
        description=("A list of triplets, where each triplet consists of two entities and the relation between them. "
                     "Triplets capture the structured relationships within the cultural heritage domain.")
    )
