from xml.etree.ElementTree import Element
import re

from ODT import GeneralInfo
from exception import MisingField, MissingKeyField


class DataValidator:

    def __init__(self, date: str) -> None:
        self.reg = r"[0-3]\d.[0,1]\d.[1,2][0,9]\d{2}"
        self.date = date
        self.is_valid = False
        self._validate_date()

    def _validate_date(self) -> None:
        match = re.fullmatch(self.reg, self.date)
        if match:
            self.is_valid = self._range_validate()

    def _range_validate(self) -> bool:
        day, month, year = self.date.split(".")
        if int(day) < 32 and int(month) < 13:
            return True
        return False

    def validate(self) -> bool:
        return self.is_valid


class MaperInfo:

    def __init__(self, element: Element) -> None:
        self.element = element

    def get_ODT(self) -> GeneralInfo:
        gai = self._get_general_account_info()
        return GeneralInfo(
            date_file=gai["date_file"],
            file_number=gai["file_number"],
            type_info=gai["type_info"],
            recipient_id=self._get_resipient_id(),
            sender_id=self._get_sender_id(),
        )

    def _get_general_account_info(self) -> dict:
        return {
            "file_number": self._get_file_number(),
            "date_file": self._get_date_file(),
            "type_info": self._get_type_info(),
        }

    def _get_file_number(self) -> str:
        try:
            # ignore уместен поскольку иначе будет исключение и вернёт ""
            number = self.element.find('ОбщСвСч').find(  # type: ignore
                'ИдФайл').find('НомФайл')  # type: ignore
            out: str = number.text  # type: ignore
        except AttributeError as ae:
            msg = "В файле отсутствует не ключевое поле <НомФайл>"
            MisingField(module_name=__name__,
                        func_name=self._get_file_number.__qualname__, msg=msg)
            return ""
        return out

    def _get_date_file(self) -> str:
        try:
            date_file = self.element.find(
                'ОбщСвСч').find('ИдФайл').find('ДатаФайл')  # type: ignore
            date_file = date_file.text  # type: ignore
        except AttributeError as ae:
            msg = "В файле отсутствует ключевое поле <ДатаФайл>"
            raise MissingKeyField(
                module_name=__name__, msg=msg, func_name=self._get_date_file.__qualname__)

        if date_file and DataValidator(date_file).validate():
            return date_file
        else:
            msg = f"Поле <ДатаФайл> не прошло валидацию Значение {date_file}" +\
                " Ожидаемый формат DD.MM.YYYY"
            raise MissingKeyField(
                module_name=__name__, msg=msg, func_name=self._get_date_file.__qualname__)

    def _get_type_info(self) -> str:
        try:
            t_info = self.element.find('ОбщСвСч').find(  # type: ignore
                'ТипИнф')  # type: ignore
            out: str = t_info.text  # type: ignore
        except AttributeError as ae:
            msg = "В файле отсутствует не ключевое поле <ТипИнф>"
            MisingField(module_name=__name__,
                        func_name=self._get_type_info.__qualname__, msg=msg)
            return ""
        return out

    def _get_resipient_id(self) -> str:
        try:
            rec_id = self.element.find('ИдПолуч').find(  # type: ignore
                'Наименование')  # type: ignore
            out: str = rec_id.text  # type: ignore
        except AttributeError as ae:
            msg = "В файле отсутствует не ключевое поле <ИдПолуч>"
            MisingField(module_name=__name__,
                        func_name=self._get_resipient_id.__qualname__, msg=msg)
            return ""
        return out

    def _get_sender_id(self) -> str:
        try:
            rec_id = self.element.find('ИдОтправ').find(  # type: ignore
                'Наименование')  # type: ignore
            out: str = rec_id.text  # type: ignore
        except AttributeError as ae:
            msg = "В файле отсутствует не ключевое поле <ИдОтправ>"
            MisingField(module_name=__name__,
                        func_name=self._get_sender_id.__qualname__, msg=msg)
            return ""
        return out
