from typing import List
from dataclasses import dataclass

from ODT import Payer, GeneralInfo


@dataclass
class XmlFile:
    name: str
    path: str
    general_info: GeneralInfo
    payers: List[Payer]
    encoding: str
