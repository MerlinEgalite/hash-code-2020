import numpy as np
import matplotlib.pyplot as plt
import pickle


import parser


data = parser.configConstructor('./datasets/e_so_many_books.txt')


def plot_signup_time(data):
    libraries = data['libraries']
    x = []
    y = []
    for lib in libraries:
        x.append(len(lib['books']))
        y.append(lib['signup_time'])
    plt.plot(x, y, 'o')
    plt.show()


def plot_velocity(data):
    libraries = data['libraries']
    x = []
    y = []
    for lib in libraries:
        x.append(len(lib['books']))
        y.append(lib['velocity'])
    plt.plot(x, y, 'o')
    plt.show()


plot_signup_time(data)

plot_velocity(data)

# c entre 10 et 20 books

l1 = [0, 10 , 6]
l2 = sorted(l1)


print(l1)
print(l2)
