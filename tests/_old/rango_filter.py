class RangoFilter(object):
    def __init__(self):
        self._criteria = []

    @property
    def criteria(self):
        return self._criteria

    @criteria.setter
    def criteria(self, value):
        self._criteria = value

    def search(self, *searchargs):
        for arg in searchargs:
            self._criteria.append(arg)