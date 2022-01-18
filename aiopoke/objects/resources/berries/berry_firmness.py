from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import Berry


class BerryFirmness(NamedResource):
    berries: List[MinimalResource["Berry"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berries = [
            MinimalResource(berry_data) for berry_data in data["berries"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
