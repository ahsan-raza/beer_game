import matplotlib.pyplot as plt

Y = []

with open('demand.txt', 'r') as demand:
    for row in demand:
        row = row.split('/n')
        Y.append(int(row[0]))

plt.plot(Y)
plt.title('Beer game demand', fontsize=12)
plt.xlabel('Number of Week', fontsize=12)
plt.xticks(range(0, 20))
plt.yticks(range(30, 45))
# plt.xlim([0,20])
plt.ylabel('Demand', fontsize=12)
plt.show()