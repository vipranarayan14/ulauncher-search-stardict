import os
import sys

from Dictionary import Dictionary

print(sys.argv)

if len(sys.argv) != 2:
    raise ValueError('Provide abs. path to the dictionary file')

dict_path = sys.argv[1]

dict_file_path = f'{dict_path}.dict'

if not os.path.exists(dict_file_path):
    raise FileNotFoundError(f"StarDict file not found in path '{dict_path}'")

dictionary = Dictionary(dict_path)

try:
    result = dictionary.lookup('गुरु')
except dictionary.WordNotFound:
    result = 'Word not found in dictionary.'

print(result)
