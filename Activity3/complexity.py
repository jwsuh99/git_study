from binarysearchtree import BinarySearchTree
from linkedlist import LinkedList
import random
import time
import matplotlib.pyplot as plt
import math
# random.seed(90)

X = [x for x in range(5,101,5)] # global variable
Y = []
Y2 = []
Y3 = []
Y4 = []

def random_tree(n):
    if 1<= n <= 1000:
        tree = BinarySearchTree(limit_size=float('inf'))
        for _ in range(n):
            value = random.randint(1,1000)
            tree.insert(value)
        return tree

def gen_y():
    for s in X:
        perf_time = 0
        for _ in range(1000):
            tree = random_tree(s)
            start_time = time.time()
            tree.search_val(42)
            end_time = time.time()
            perf_time += end_time - start_time
        avg_time = perf_time / 1000
        Y.append(avg_time)

def gen_y2():
    n = [5,10]
    y = []

    for s in n:
        perf_time = 0
        for _ in range(1000):
            tree = random_tree(s)
            start_time = time.time()
            tree.search_val(42)
            end_time = time.time()
            perf_time += end_time - start_time
        avg_time = perf_time / 1000
        y.append(avg_time)

    c = (y[1] - y[0]) / (n[1] - n[0])    #t-b/n = c from t = c*n + b
    b = y[0] - c*n[0] # t - c*n = b from t = c*n + b

    if c < 0:
        c = abs(c)

    for n in X:
        t = c*n + b
        Y2.append(t)

def gen_y3():
    n = [5, 10]
    y = []

    for s in n:
        perf_time = 0
        for _ in range(1000):
            tree = random_tree(s)
            start_time = time.time()
            tree.search_val(42)
            end_time = time.time()
            perf_time += end_time - start_time
        avg_time = perf_time / 1000
        y.append(avg_time)

    log_n0 = math.log2(n[0])
    log_n1 = math.log2(n[1])
    c = (y[0] - y[1])/ log_n0 - log_n1
    b = y[0] - c*log_n0

    if c < 0:
        c = abs(c)

    for n in X:
        log_n = math.log2(n)
        t = c*log_n + b
        Y3.append(t)

def random_list(n):
    if 1 <= n <= 1000:
        linked_list = LinkedList(limit_size=float('inf'))
        for _ in range(n):
            value = random.randint(1, 1000)
            linked_list.insert(value)

        return linked_list

def gen_y4():
    for s in X:
        perf_time = 0
        for _ in range(1000):
            linked_list = random_list(s)
            start_time = time.time()
            linked_list.search(42)
            end_time = time.time()
            perf_time += end_time - start_time
        avg_time = perf_time / 1000
        Y4.append(avg_time)


def plot_x_y(): # ref: https://matplotlib.org/stable/users/explain/quick_start.html
    plt.plot(X,Y)
    plt.xlabel('Size of tree')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis = 'both', style='sci',scilimits=(0,0))
    plt.show()

def plot_three(): # Complexity analysis X vs Y, Y2 and Y3 depend on
    # result Y and Y2's result are in the order of e-06 and Y3 is normally 15~30
    scaled_Y3 = [num * 1e-06 for num in Y3]
    plt.plot(X,Y)
    plt.plot(X, Y2)
    plt.plot(X, scaled_Y3)
    plt.legend(['BST', 'Linear', 'Logarithmic'])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    plt.show()

def plot_four(): #Complexity analysis X vs Y, Y2, Y3 and Y4, depend on
    # result Y and Y2's result are in the order of e-06 and Y3 is normally 15~30
    # and Y4's result is in the order of e -05. So i intentionally adjust it for plot
    scaled_Y3 = [num * 1e-06 for num in Y3]
    scaled_Y4= [num * 1e-01 for num in Y4]
    plt.plot(X, Y)
    plt.plot(X, Y2)
    plt.plot(X, scaled_Y3)
    plt.plot(X, scaled_Y4)
    plt.legend(['BST', 'Linear', 'Logarithmic', 'LL'])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    plt.show()

def main():
    gen_y()
    gen_y2()
    gen_y3()
    gen_y4()
    plot_x_y() #Complexity analysis X vs Y seems like O(log(n))
    plot_three()
    plot_four()


if __name__ == '__main__':
    main()
