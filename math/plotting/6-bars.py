#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    generates a stacked bar graph showing the number of different fruits
    (apples, bananas, oranges, peaches) that Farrah, Fred, and Felicia have

    -apples are colored red
    -bananas are colored yellow
    -oranges are colored orange (#ff8000)
    -peaches are colored peach (#ffe5b4)

    bars are stacked in the order of the fruit matrix
    (from bottom to top)
    the graph includes a legend, y-axis label,
    tick marks every 10 units (0 to 80),
    and a title
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ['Farrah', 'Fred', 'Felicia']
    fruit_labels = ['apples', 'bananas', 'oranges', 'peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    bar_width = 0.5
    x = np.arange(fruit.shape[1])

    bottom = np.zeros(fruit.shape[1])

    for i in range(fruit.shape[0]):
        plt.bar(x, fruit[i], width=bar_width, bottom=bottom,
                color=colors[i], label=fruit_labels[i])
        bottom += fruit[i]

    plt.xticks(x, people)
    plt.yticks(np.arange(0, 81, 10))
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.legend()
    plt.ylim(0, 80)
    plt.show()
