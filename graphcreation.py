import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def creategraphs(kps, time):
    fig = plt.figure()
    fig, ax = plt.subplots()
    return ax.plot(time, kps)

if __name__ == "__main__":
    graph = creategraphs([1,2,3,4,5], range(5))
    plt.show()

