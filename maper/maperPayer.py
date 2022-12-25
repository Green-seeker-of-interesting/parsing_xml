from xml.etree.ElementTree import Element
from typing import List

from ODT import Payer


class MaperPayer:

    def __init__(self, element: Element) -> None:
        self.element = element

    def get_ODT(self) -> list[Payer]:
        pass