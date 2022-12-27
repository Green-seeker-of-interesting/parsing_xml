import os
import shutil


class FileMover:

    @classmethod
    def good(cls, path: str):
        workdir = cls._get_path_workdir(path)
        if not os.path.exists(os.path.join(workdir, "arh")):
            os.makedirs(os.path.join(workdir, "arh"))
        shutil.move(path, os.path.join(workdir, "arh"))

    @classmethod
    def bad(cls, path: str):
        workdir = cls._get_path_workdir(path)
        if not os.path.exists(os.path.join(workdir, "bad")):
            os.makedirs(os.path.join(workdir, "bad"))
        shutil.move(path, os.path.join(workdir, "bad"))

    @classmethod
    def _get_path_workdir(cls, path: str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError
        return os.path.dirname(path)
