from typing import TYPE_CHECKING, Tuple

from ...minimal_resources import MinimalResource
from ...utility.common_models import Description, Name, NamedResource

if TYPE_CHECKING:
    from . import Move


class MoveTarget(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    moves: Tuple[MinimalResource["Move"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = tuple(
            name_data["name"]
            for name_data in data["names"]
            if name_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.moves = tuple(MinimalResource(move_data) for move_data in data["moves"])

    def __repr__(self) -> str:
        return f"<MoveTarget description='{self.description}' descriptions={self.descriptions} id_={self.id_} moves={self.moves} name='{self.name}'>"
