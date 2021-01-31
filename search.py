from pystardict import Dictionary


class WordNotInDictionary(Exception):
    pass


def initDictionary(dict_path):
    return Dictionary(dict_path)


def search(dictionary, query):
    try:
        return dictionary.dict[query]
    except KeyError:
        raise WordNotInDictionary(query)

