import os
from xml.etree import ElementTree

from ODT import XmlFile
from exception import InvalidXmlTree
from maper import MaperInfo, MaperPayer


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
            encoding=self._get_encoding(),
        )

    def _init_mapers(self) -> None:
        try:
            root = ElementTree.parse(self.path).getroot()
            info_part, payers_part = list(root)
            self.maper_info = MaperInfo(info_part)
            self.maper_payer = MaperPayer(payers_part)
        except ValueError as e:
            msg = "В корневом элементе {} потомка а ожидалось 2".format(
                len(list(ElementTree.parse(self.path).getroot())))
            raise InvalidXmlTree(module_name=__name__,
                                 func_name=self._init_mapers.__name__, msg=msg)

    def _get_encoding(self) -> str:
        # reg = r'encoding="(.+)"'
        with open(self.path, 'rb') as f:
            text = f.readline().decode("utf-8")
        return text.split("=")[-1].split('"')[1]
