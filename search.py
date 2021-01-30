# import stargaze

# dict = stargaze.Dictionary("/home/prasanna/App Files/data/dictdata/apte-1890")

# result = dict.lookup("गुरु")

# print(result)

from pystardict import Dictionary

dict = Dictionary(
    "/home/prasanna/App Files/data/dictdata/shabda-sAgara/shabda-sAgara",
    in_memory=False,
)

result = dict.dict["प्रश्न"]

print(result)
