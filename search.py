from pystardict import Dictionary


class WordNotInDictionary(Exception):
    pass


def initDictionary(dict_path):
    return Dictionary(dict_path)


def search(dictionary, query):
    try:
        dictionary.dict[query]
    except KeyError:
        raise WordNotInDictionary(query)


_dict = initDictionary(
    dict_path="/home/prasanna/App Files/data/dictdata/shabda-sAgara/shabda-sAgara"
)

result = search(_dict, "fdsf")

print(result)
