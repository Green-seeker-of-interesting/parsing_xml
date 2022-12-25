from xml.etree.ElementTree import Element

from ODT import GeneralInfo


class MaperInfo:

    def __init__(self, element: Element) -> None:
        self.element = element

    def get_ODT(self) -> GeneralInfo:
        pass