"""
count - itertools
"""

from itertools import count

contador = count(start=5, step=0.1)

for x in contador:
    print(round(x, 2))

    if x >= 10:
        break