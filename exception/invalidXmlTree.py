from logger import loggerFactory


class InvalidXmlTree(Exception):

    def __init__(self, module_name: str, func_name: str, msg: str) -> None:
        self.module_name = module_name
        self.func_name = func_name
        self.message = msg
        self._loging()

    def __str__(self) -> str:
        return f"Модуль: {self.module_name} Функция: {self.func_name} \n{self.message}"

    def _loging(self) -> None:
        loggerFactory.get_loger().error(str(self))
