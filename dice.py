
import random
import matplotlib.pyplot as plt
plt.rc('axes', linewidth=3)


N = random.randrange(1,7)  # 1 through 6, inclusive
print(N)


# funky dice plot
fig,ax=plt.subplots(dpi=300, figsize=[3,3], linewidth=3)
for i in range(N):
    x = random.random()
    y = random.random()
    ax.plot(x,y, 'bo', markersize=20, markerfacecolor='None', markeredgewidth=2)

dx = 0.1
ax.set_xlim(-dx,1+dx)
ax.set_ylim(-dx,1+dx)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title(N, fontsize=14)
plt.show()


