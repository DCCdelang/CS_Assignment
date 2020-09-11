import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df =pd.read_csv('istherecorrelation.csv', delimiter=';',header=0)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (years)')
ax1.set_ylabel('WO x1000', color=color)
ax1.plot(df['Year'], df['WO [x1000]'])
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('NL Beer consumption x1000 hL', color=color)  # we already handled the x-label with ax1
ax2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'])
ax2.tick_params(axis='y', labelcolor=color)

print("Is there correlation?")
print("Yes for:",np.corrcoef(df['Year'], df['NL Beer consumption [x1000 hectoliter]'])[0][1], "%")

fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()
fig.savefig('myplot.jpeg', dpi=300)
