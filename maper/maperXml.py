import os
from xml.etree import ElementTree

from ODT import XmlFile
from exception import InvalidXmlTree
from maper import MaperInfo, maperPayer

class MaperXml:

    def __init__(self, path: str) -> None:
        self.path = path

    def get_xml_file(self) -> XmlFile:
        self._init_mapers()
        return XmlFile(
            name=os.path.basename(self.path),
            path=self.path,
            general_info=self.maper_info.get_ODT(),
            payers=self.maper_payer.get_ODT(),
            encoding=""
        )

    def _init_mapers(self) -> None:
        try:
            root = ElementTree.parse(self.path).getroot()
            info_part, payers_part = list(root)
            self.maper_info = MaperInfo(info_part)
            self.maper_payer = maperPayer(payers_part) # type:ignore
        except ValueError as e:
            msg = "В корневом элементе {} потомка а ожидалось 2".format(
                len(list(ElementTree.parse(self.path).getroot())))
            raise InvalidXmlTree(module_name=__name__,
                                 func_name=self._init_mapers.__name__, msg=msg)
