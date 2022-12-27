import os


class PreliminaryCheck:

    @classmethod
    def chek(cls, path: str) -> bool:
        if os.path.exists(path):
            return path.endswith('.xml')
        return False
