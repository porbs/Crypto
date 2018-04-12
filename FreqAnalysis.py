from collections import OrderedDict
import matplotlib.pylab as plt


def calculate_frequency(data: str):
    alphabet = [chr(upper) for upper in range(ord('A'), ord('Z') + 1)]
    data = list(filter(lambda x: x in alphabet, str.upper(data)))
    freqs = dict()
    for c in data:
        if c not in freqs:
            freqs[c] = 0
        else:
            freqs[c] += 1
    return {k: (freqs[k] * 100 / len(data)) for k in sorted(freqs, key=freqs.get, reverse=True)}
    # return OrderedDict(sorted({k: v*100/len(data) for k, v in freqs.items()}.items()))


def plot_frequencies(*args):
    plt.figure(1)
    i = 1
    for data in args:
        plt.subplot(int(str(len(args)) + "1" + str(i)))
        i += 1
        plt.bar(list(data.keys()), data.values())
        plt.xlabel("Value")
        plt.ylabel("Frequency")
    plt.show()
