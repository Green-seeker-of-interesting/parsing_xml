from logger import loggerFactory
from maper import MaperXml
from exception import InvalidXmlTree

def main():
    path = "./data/task.xml"
    # path = "./data/tooMany.xml"
    # path = "./data/bad.xml"
    loggerFactory.logger_strat(path)

    maper: MaperXml = MaperXml(path)
    file =  maper.get_xml_file()
    print(file)


if __name__ == "__main__":
    try:
        main()
    except InvalidXmlTree as e:
        print("Что то не так с деревом")
    except Exception as e:
        print(type(e))
