import sys
import math
from matplotlib import pyplot as plt

if __name__ == '__main__':
    nList = [1 << i for i in range(8)]

    O1 = [1 for n in nList]
    Ologn = [math.log2(n) for n in nList]
    On = [n for n in nList]
    Onlogn = [(n * math.log2(n)) for n in nList]
    On2 = [n ** 2 for n in nList]
    O2n = [2 ** n for n in nList]

    print("\nComplexity of O(1):")
    print(O1)
    print("\nComplexity of O(log(n)):")
    print(Ologn)
    print("\nComplexity of O(n):")
    print(On)
    print("\nComplexity of O(nlog(n)):")
    print(Onlogn)
    print("\nComplexity of O(n^2):")
    print(On2)
    print("\nComplexity of O(2^n):")
    print(O2n)

    plt.plot(nList, O1, label='O(1)', linewidth=1)
    plt.plot(nList, Ologn, label='O(log(n))', linewidth=1)
    plt.plot(nList, On, label='O(n)', linewidth=1)
    plt.plot(nList, Onlogn, label='O(nlog(n))', linewidth=1)
    plt.plot(nList, On2, label='O(n^2)', linewidth=1)
    plt.plot(nList, O2n, label='O(2^n)', linewidth=1)  # Can't be clearly shown together with all other data

    plt.title('Complexity Plots')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    sys.exit(0)
