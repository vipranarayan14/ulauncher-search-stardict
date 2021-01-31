from pystardict import Dictionary as _Dictionary


class Dictionary:
    def __init__(self, dict_path: str):
        self._dict_path = dict_path
        self._dict_data = _Dictionary(dict_path)

    class WordNotFound(Exception):
        pass

    def lookup(self, query: str) -> str:
        try:
            return self._dict_data.dict[query]
        except KeyError:
            raise self.WordNotFound(query)
