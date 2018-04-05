# -*- coding: utf-8 -*-
"""Show CSV header info"""

import csv
import sys
from tabulate import tabulate
import header

if __name__ == '__main__':

    with open(sys.argv[0]) as input_stream:
        READER = csv.reader(sys.stdin)

        INPUT_HEADERS = next(READER, None)
        if INPUT_HEADERS:
            COLUMNS = header.stats(INPUT_HEADERS)

            OUTPUT_HEADER = ["Column", "Position", "Index"]
            print(tabulate(COLUMNS, OUTPUT_HEADER, tablefmt="grid"))
