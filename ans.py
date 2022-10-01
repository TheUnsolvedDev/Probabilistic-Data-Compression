import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random
import math

table_log = 5
table_size = 1 << table_log


def first_set_index(val):
    counter = 0
    while val > 1:
        counter += 1
        val >>= 1
    return counter


if __name__ == '__main__':

    print(first_set_index(34))
    print(bin(34))

    # Define how often a symbol is seen, total should equal the
    # table size.
    symbol_occurrences = {"0": 10, "1": 10, "2": 12}

    ####
    # Define the Initial Positions of States in StateList.
    ####
    symbol_list = [symbol for symbol,
                   occcurences in symbol_occurrences.items()]
    cumulative = [0 for _ in range(len(symbol_list)+2)]
    for u in range(1, len(symbol_occurrences.items()) + 1):
        cumulative[u] = cumulative[u - 1] + \
            list(symbol_occurrences.items())[u-1][1]
    cumulative[-1] = table_size + 1
    print(symbol_list, cumulative)

    #####
    # Spread Symbols to Create the States Table
    #####

    high_thresh = table_size - 1
    states_table = [0 for _ in range(table_size)]
    table_mask = table_size - 1
    step = ((table_size >> 1)+(table_size >> 3) + 3)
    pos = 0
    for symbol, occcurences in symbol_occurrences.items():
        for i in range(occcurences):
            states_table[pos] = symbol
            pos = (pos + step) & table_mask
    print(states_table)

    #####
    # Build Coding Table from State Table
    #####

    output_bits = [0 for _ in range(table_size)]
    coding_table = [0 for _ in range(table_size)]
    cumulative_cp = cumulative.copy()

    for i in range(table_size):
        s = states_table[i]
        index = symbol_list.index(s)
        coding_table[cumulative_cp[index]] = table_size + i
        cumulative_cp[index] += 1
        output_bits[i] = table_log - first_set_index(table_size + i)

    print(output_bits, coding_table)
