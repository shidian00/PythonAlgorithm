"""
Convert a string of characters to a sequence of numbers
corresponding to the character's position in the English alphabet.
https://www.dcode.fr/letter-number-cipher
http://bestcodes.weebly.com/a1z26.html
"""
from __future__ import annotations


def encode(plain: str) -> list[int]:
    """
    >>> encode("myname")
    [13, 25, 14, 1, 13, 5]
    >>> encode("testing")
    [20, 5, 19, 20, 9, 14, 7]
    >>> encode("demo 123")
    [4, 5, 13, 15, -64, -47, -46, -45]
    """
    return [ord(elem) - 96 for elem in plain]


def decode(encoded: list[int]) -> str:
    """
    >>> decode([13, 25, 14, 1, 13, 5])
    'myname'
    >>> decode([20, 5, 19, 20, 9, 14, 7])
    'testing'
    >>> decode([4, 5, 13, 15, -64, -47, -46, -45])
    'demo 123'
    """
    return "".join(chr(elem + 96) for elem in encoded)


def main() -> None: # pragma: no cover
    encoded = encode(input("-> ").strip().lower())
    print("Encoded: ", encoded)
    print("Decoded:", decode(encoded))

if __name__ == "__main__": # pragma: no cover
    main()
