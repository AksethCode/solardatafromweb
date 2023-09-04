import re
from googlesearch import search

s = search("microsoft", num_results=5)

for i in s:

    print(i)

