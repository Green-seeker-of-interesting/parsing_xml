from loggerFactory import loggerFactory

class missingKeyField(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Отсутствует ключевой параметр"

    def __str__(self):
        pass
