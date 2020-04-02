''' Order Braille dots:
     1 4       01 08
     2 5  -->  02 16
     3 6       04 32
'''

T2B = {'a': 1, 'b': 3, 'c': 9, 'd': 25, 'e': 17, 'f': 11, 'g': 27, 'h': 19, 'i': 10, 'j': 26, \
       'k': 5, 'l': 7, 'm': 13, 'n': 29, 'o': 21, 'p': 15, 'q': 31, 'r': 23, 's': 14, 't': 30, \
       'u': 37, 'v': 39, 'x': 45, 'y': 61, 'z': 53, 'w': 58, \
       'and': 47, 'of': 55, 'the': 46, 'with': 62, 'for': 63, \
       'capital symbol': 32, 'comma': 2, 'apostrophe': 4, 'colon': 18, 'exclamation mark': 22, 'question mark': 38, \
       'semicolon': 6, 'superscript indicator': 20, 'subscript indicator': 36}

B2T = {}

for sym in T2B:
    B2T[T2B[sym]] = sym
