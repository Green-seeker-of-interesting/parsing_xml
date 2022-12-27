import re


class DateValidator:

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
