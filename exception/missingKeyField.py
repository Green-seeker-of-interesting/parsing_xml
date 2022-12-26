from exception import BaseExceprion
from logger import loggerFactory

class MissingKeyField(BaseExceprion):

    def _loging(self) -> None:
        loggerFactory.get_loger().error(str(self))


