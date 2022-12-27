import re


class PeriodValidator:

    def __init__(self, period: str):
        self.reg = r"[0,1]\d[1,2][0,9]\d{2}"
        self.period = period
        self.is_valid = False
        self._validate_period()

    def _validate_period(self) -> None:
        match = re.fullmatch(self.reg, self.period)
        if match:
            self.is_valid = self._range_validate()

    def _range_validate(self) -> bool:
        month = int(self.period[0:2])
        if month < 13:
            return True
        return False

    def validate(self) -> bool:
        return self.is_valid
