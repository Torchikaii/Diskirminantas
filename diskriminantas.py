from math import *

while True:
    try:
        def main():
            a = float(input("a: ").strip())
            b = float(input("b: ").strip())
            c = float(input("c: ").strip())
            d = pow(b, 2) - 4 * a * c
            if d < 0:
                return "sprendinių nėra"
            else:
                x1 = (-1 * b + sqrt(d)) / (2 * a)
                x2 = (-1 * b - sqrt(d)) / (2 * a)
                return x1, x2

        print(" ")
        print(main())

    except ValueError:
        print(ValueError)
        continue
    except ZeroDivisionError:
        print(ZeroDivisionError)
        continue
