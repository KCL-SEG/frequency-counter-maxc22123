"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    s_items = [str(i) for i in items]

    for i in s_items:
        frequencies[i] = s_items.count(i)

    return frequencies
