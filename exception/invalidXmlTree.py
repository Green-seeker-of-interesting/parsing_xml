from exception import BaseExceprion
from logger import loggerFactory


class InvalidXmlTree(BaseExceprion):

    def _loging(self) -> None:
        loggerFactory.get_loger().error(str(self))
