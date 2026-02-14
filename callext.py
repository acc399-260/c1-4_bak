'''\
callext.py
ACC 399 c1-4
February 14, 2026

This program illustrates calling functions from another file.
'''

import linear as lin

strName = lin.greet()
iRes = lin.numericalInputs()

print(f"Aloha e {strName} (the sum was {iRes}.)")
