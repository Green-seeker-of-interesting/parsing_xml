from exception import BaseExceprion
from logger import loggerFactory


class MisingField(BaseExceprion):

    def _loging(self) -> None:
        loggerFactory.get_loger().warning(str(self))
