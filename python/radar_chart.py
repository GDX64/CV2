# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import pdb

# Set data
df = pd.DataFrame({
'group': ['A','B','C','D'],
'Str': [23, 1.5, 30, 4],
'Speed': [33, 10, 9, 34],
'Dribbling': [32, 39, 1000, 24],
'Pass': [35, 31, 33, 14],
'Shooting': [25, 15, 32, 14]
})

# number of variable
categories=list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
plt.figure(figsize=(10,10))
ax = plt.subplot(111, polar=True)
#breakpoint()
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid', color='r')

# Fill area
ax.fill(angles, values, 'red', alpha=0.2)

plt.show()
