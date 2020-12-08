import sys
import math
from matplotlib import pyplot as plt


class Bubble:

    def __init__(self):
        self.lst = []

    def sort(self, to_sort):
        done = False
        no_change = True
        element = 0
        while not done:
            if element < len(to_sort)-1:
                if to_sort[element][1] > to_sort[element+1][1]:
                    self.lst.append(to_sort[element])
                    to_sort[element] = to_sort[element+1]
                    to_sort[element + 1] = self.lst.pop()
                    no_change = False
                element += 1
            elif no_change:
                done = True
            else:
                element = 0
                no_change = True


class Merge:

    def sort(self, to_sort):
        if len(to_sort) > 1:
            mid = len(to_sort) // 2
            left = to_sort[:mid]
            right = to_sort[mid:]

            self.sort(left)
            self.sort(right)

            to_sort.clear()

            while len(left) > 0 and len(right) > 0:
                if left[0][1] < right[0][1]:
                    to_sort.append(left.pop(0))
                else:
                    to_sort.append(right.pop(0))
            # Appending any leftover elements from both the left and right lists
            while len(left) > 0:
                to_sort.append(left.pop(0))

            while len(right) > 0:
                to_sort.append(right.pop(0))


def print_complexity():
    print("\n              COMPLEXITY COMPARISON")
    print("-"*48)
    print("n", " "*8, n_list[0], " "*6, n_list[1], " "*6, n_list[2])
    print("nlog(n)", " "*2, round(Onlogn[0], 3), " "*2, round(Onlogn[1], 3), " ",  round(Onlogn[2], 3))
    print("n^2", " "*6, On2[0], " "*4, On2[1], " "*2, On2[2])


def ascii_score_table(scores, method):
    descending_scores = []
    counter = 0
    for i in scores:
        counter -= 1
        descending_scores.append(scores[counter])

    place = 0
    print(f"\nHigh scores sorted using {method}")
    print("No. Player", " "*30, "Score")
    print("-"*47)
    for i in descending_scores:
        place += 1
        print(place, " "*(2-len(str(place))), i[0], " " * (37-len(i[0])), i[1])


if __name__ == '__main__':
    n_list = [10 ** ((i+1)*2) for i in range(3)]
    score_list = [
        ["Napaladin", 73],
        ["Cocowboy", 20],
        ["Oysterminate", 15],
        ["RadioactiveYak", 67],
        ["RudeFlamingo", 65],
        ["RadioactiveRose", 93],
        ["Rerunner", 90],
        ["Gerbilbo", 85],
        ["Lobsteroid", 37],
        ["GiantChimera", 18],
        ["DapperFledgling", 26],
        ["ClassicRoach", 83],
        ["Patriode", 24],
        ["BalanceBot", 71],
        ["NurNNNN", 3],
        ["SmartGull", 49],
        ["MeanKoala", 90],
        ["Cloverlord", 55],
        ["Warthawk", 90],
        ["StrongFlike", 52],
    ]

    Onlogn = [(n * math.log2(n)) for n in n_list]
    On2 = [n ** 2 for n in n_list]

    print_complexity()

    plt.plot(n_list, Onlogn, label='O(nlog(n))', linewidth=1)
    plt.plot(n_list, On2, label='O(n^2)', linewidth=1)

    plt.title('Complexity Plots')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    bubble = Bubble()
    merge = Merge()

    score_list_2 = score_list

    bubble.sort(score_list)
    merge.sort(score_list_2)
    ascii_score_table(score_list, "bubble sort")
    ascii_score_table(score_list_2, "merge sort")
    sys.exit(0)
