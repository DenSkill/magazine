class InstantiateCSVError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message