import numpy as np
import matplotlib.pyplot as plt
import pickle

pickle_in = open("dict.pickle","rb")




def plot_signup_time(data):
    libraries = data['config']['libraries']
    x = []
    y = []
    for lib in libraries:
        x.append(len(lib['books']))
        y.append(lib['signup_time'])
    plt.plot(x, y)
    plt.show()


def plot_velocity(data):
    libraries = data['config']['libraries']
    x = []
    y = []
    for lib in libraries:
        x.append(len(lib['books']))
        y.append(lib['velocity'])
    plt.plot(x, y)
    plt.show()



