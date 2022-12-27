import sys

from logger import loggerFactory
from maper import MaperXml
from exception import InvalidXmlTree
from validator import BusinessLogicValidator
from tools import CSVWriter, PreliminaryCheck, FileMover


def main(path: str):
    loggerFactory.logger_strat(path)
    if PreliminaryCheck.chek(path):
        file = MaperXml(path).get_xml_file()
        file = BusinessLogicValidator().validate(file)
        CSVWriter().write(file)
        FileMover.good(path)
        print('Процесс завершен')
    else:
        raise FileNotFoundError


def main_exception_hendler():
    path = sys.argv[1]
    try:
        main(path)
    except InvalidXmlTree as e:
        print("Не удалось обработать дерево")
        FileMover.bad(path)
    except FileNotFoundError as e:
        print("Не удалось найти xml файл")
    except Exception as e:
        print("В процессе работы произошла ошибка")
        FileMover.bad(path)


if __name__ == "__main__":
    main_exception_hendler()
