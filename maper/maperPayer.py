from xml.etree.ElementTree import Element
from typing import List, Union

from ODT import Payer
from exception import MisingField, MissingKeyField
from validator import PeriodValidator


class MaperPayer:

    def __init__(self, element: Element) -> None:
        self.element = element

    def get_ODT(self) -> List[Payer]:
        out = []
        for i, el in enumerate(self._tag_filter()):
            new_payer = self._parse_payer(i, el)
            if new_payer:
                out.append(new_payer)
        return out

    def _tag_filter(self) -> List[Element]:
        out = []
        for payer in self.element:
            if payer.tag == "Плательщик":
                out.append(payer)
        return out

    def _parse_payer(self, index: int, element: Element) -> Union[Payer, None]:
        try:
            return Payer(
                personal_account=self._get_personal_account(index, element),
                full_name=self._get_full_name(index, element),
                address=self._get_adress(index, element),
                period=self._get_period(index, element),
                total=self._get_total(index, element),
            )
        except MissingKeyField as e:
            return None

    def _get_personal_account(self, index: int, element: Element) -> str:
        try:
            p_accout = element.find("ЛицСч")
            out = p_accout.text  # type: ignore
        except AttributeError as at:
            msg = f"В записи № {index} отсутствует ключевое поле <ЛицСч>" +\
                " Обработка записи остановленна"
            raise MissingKeyField(module_name=__name__,
                                  func_name=self._get_personal_account.__qualname__,
                                  msg=msg)
        return out  # type: ignore

    def _get_full_name(self, index: int, element: Element) -> str:
        try:
            full_name = element.find("ФИО")
            out = full_name.text  # type: ignore
            return out  # type: ignore
        except AttributeError as at:
            msg = f"В записи № {index} отсутствует не ключевое поле <ФИО>"
            MisingField(module_name=__name__,
                        func_name=self._get_full_name.__qualname__, msg=msg)
        return ""

    def _get_adress(self, index: int, element: Element) -> str:
        try:
            adress = element.find("Адрес")
            out = adress.text  # type: ignore
            return out  # type: ignore
        except AttributeError as at:
            msg = f"В записи № {index} отсутствует не ключевое поле <Адрес>"
            MisingField(module_name=__name__,
                        func_name=self._get_adress.__qualname__, msg=msg)
        return ""

    def _get_period(self, index: int, element: Element) -> str:
        try:
            period = element.find("Период")
            period = period.text  # type: ignore
        except AttributeError as ae:
            msg = f"В записи № {index} отсутствует ключевое поле <Период>" +\
                " Обработка записи остановленна"
            raise MissingKeyField(module_name=__name__,
                                  func_name=self._get_period.__qualname__,
                                  msg=msg)

        if period and PeriodValidator(period).validate():
            return period
        else:
            msg = f"В записи № {index} поле <Период> не прошло валидацию" +\
                f" Значение {period} Ожидаемый формат MMYYYY \nОбработка записи остановленна"
            raise MissingKeyField(module_name=__name__,
                                  func_name=self._get_period.__qualname__,
                                  msg=msg)

    def _get_total(self, index: int, element: Element) -> float:
        out = ""
        try:
            total = element.find("Сумма")
            out = total.text  # type: ignore
            return float(out)  # type: ignore
        except AttributeError as at:
            msg = f"В записи № {index} отсутствует не ключевое поле <Сумма>"
            MisingField(module_name=__name__,
                        func_name=self._get_full_name.__qualname__, msg=msg)
        except ValueError as ve:
            msg = f"В записи № {index} поле <Сумма> имеет некоректное значение [{out}] " +\
                "Ожидалось чисто типа float \nУстановленно значение по умолчанию 0.0"
            MisingField(module_name=__name__,
                        func_name=self._get_full_name.__qualname__, msg=msg)
        return 0.0
