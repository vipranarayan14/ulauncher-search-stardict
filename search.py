from pystardict import Dictionary


def initDictionary(dict_path):
    return Dictionary(dict_path)


def search(dictionary, query):
    return dictionary.dict[query]


# _dict = initDictionary(
#     dic_path="/home/prasanna/App Files/data/dictdata/shabda-sAgara/shabda-sAgara"
# )

# result = search(_dict, "गुरु")

# print(result)
