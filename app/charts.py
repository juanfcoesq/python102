import matplotlib.pyplot as plt
import random

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    values = [random.randint(1, 500) for _ in range(10)]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)