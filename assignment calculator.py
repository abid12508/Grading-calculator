#assignment calculator

from cProfile import label
from turtle import color
from xml.dom.expatbuilder import theDOMImplementation
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

set_1 = []
set_2 = []

i = 1
ax = plt.figure().gca()

ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

num_Sets = 1

while i < 500:

    set1_Input = int(input("Enter grade (set 1) >>"))

    if set1_Input != 000:

        set_1.append(set1_Input)
        i += 1

    elif set1_Input == 000:

        print(f'avg: {[sum(set_1) / len(set_1)]}')
        print(f'list: {set_1}')

        plt.plot([x+1 for x in range(0, len(set_1))], set_1, label = "set 1", color = "green", marker = 'o', markerfacecolor = 'r')
        break

    else:
        print("Error")

x = 1

while x < 500:

    set2_Input = int(input("Enter grade (set 2) >>"))

    if set2_Input != 000:

        set_2.append(set2_Input)
        x += 1

    elif set2_Input == 000 and len(set_2) > 0:

        print(f'avg: {[sum(set_2) / len(set_2)]}')
        print(f'list: {set_2}')

        plt.plot([x+1 for x in range(0, len(set_2))], set_2, label = "set 2", color = "blue", marker = 'o', markerfacecolor = 'r')
        print("x axis is indexed (0 is 1 and 1 is 2....)")
        break
    elif set2_Input == 000 and len(set_2) == 0:
        print("x axis is indexed (0 is 1 and 1 is 2....)") 
        break

    else:
        print("Error")

plt.xlabel('Number of assignments')
plt.ylabel('Grade')

plt.title('grade calculator')

plt.legend()
plt.show()