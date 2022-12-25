import os
import logging
from logging import Logger


class LoggerFactory:

    def logger_strat(self, path:str) -> None:
        self.workdir = self._get_path_workdir(path)
        self._create_dir()
        self._init_logger()

    def _get_path_workdir(self, path: str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError
        return os.path.dirname(path)

    def _create_dir(self) -> None:
        if not os.path.exists(os.path.join(self.workdir, "log")):
            os.makedirs(os.path.join(self.workdir, "log"))

    def _init_logger(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            filename=os.path.join(self.workdir, "log", "python.log"),
            filemode="a",
            format="%(name)s - %(levelname)s  \n" +
            "Исключение -  %(module)s Время - %(asctime)s \n" +
            "%(message)s"
        )
        self.logger: Logger = logging.getLogger("main_logger")

    def get_loger(self) -> Logger:
        return self.logger
