#two.py

import one

print("TOP LEVEL TWO.PY!")

one.func()

if __name__ == '__main__' :
    print("TWO.PY runs Directly !")
else:
    print("TWO.PY")