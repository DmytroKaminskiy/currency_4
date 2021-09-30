class TXTWriter:
    def __init__(self, filename=None):

        if not filename:
            filename = 'results.txt'

        self._file = open(filename, 'w')

    def write(self, item: dict):
        # sort dict by key and transform to string
        item = str(dict(sorted(item.items())))

        self._file.write(item)
        self._file.write('\n')

    def destruct(self):
        self._file.close()
