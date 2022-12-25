from logger import loggerFactory
from ODT import Payer
from maper import MaperXml
from exception import InvalidXmlTree

def main():
    path = "./data/task.xml"
    # path = "./data/tooMany.xml"
    loggerFactory.logger_strat(path)

    maper: MaperXml = MaperXml(path)
    maper.get_xml_file()


if __name__ == "__main__":
    try:
        main()
    except InvalidXmlTree as e:
        pass
    except Exception as e:
        print(e)
