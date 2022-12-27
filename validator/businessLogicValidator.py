from collections import Counter

from ODT import XmlFile
from exception import FailedValidation


class BusinessLogicValidator:

    def validate(self, file: XmlFile) -> XmlFile:
        self.file = file
        self._total_validator()
        self._repeat_validator()
        return self.file

    def _total_validator(self):
        for payer in self.file.payers:
            if payer.total < 0:
                self.file.payers.remove(payer)
                msg = f"ЛицСч - {payer.personal_account} Период - {payer.period} \n" + \
                      f"Поле Сумма имеет значение {payer.total}. Ожидалось положительное значение \n" +\
                      f"Обрабока записи остановленна"
                FailedValidation(
                    module_name=__name__, func_name=self._total_validator.__qualname__, msg=msg)

    def _repeat_validator(self):
        counter = Counter(self.file.payers)
        for payer, count in counter.items():
            if count > 1:
                self._del_by_hash(hash(payer))
                msg = f"ЛицСч - {payer.personal_account} Период - {payer.period} \n" + \
                      f"Запись встретилась {count} раз. \n" +\
                      f"Обрабока записи остановленна"
                FailedValidation(
                    module_name=__name__, func_name=self._repeat_validator.__qualname__, msg=msg)

    def _del_by_hash(self, hs: int):
        for payer in self.file.payers:
            if hash(payer) == hs:
                self.file.payers.remove(payer)
