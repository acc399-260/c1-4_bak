'''\
mod2.py
A short program to show the result of the mod % operator.
The mod % operator returns the remainder of division.
NOTE: // is the operator for integer division.

This program also illustrates a deterministic loop a.k.a.* "for loop"
which is repeated a set number of times.

*a.k.a. = also known as
'''
print(" integer quotient remainder")
for iseq in range(0, 11):
    print(f"{iseq:5d} \t {iseq // 2:5d} \t {iseq % 2:5d}")
