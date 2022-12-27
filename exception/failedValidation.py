from exception import BaseExceprion
from logger import loggerFactory


class FailedValidation(BaseExceprion):

    def _loging(self) -> None:
        loggerFactory.get_loger().error(str(self))
