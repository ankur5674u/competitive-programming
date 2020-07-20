class Multiset(object):
    def __init__(self):
        self._element = list()

    def add(self, val):
        self._element.append(val)

    def remove(self, val):
        self._element.remove(val)

    def __len__(self):
        return len(self._element)

    def __contains__(self, item):
        return item in self._element
