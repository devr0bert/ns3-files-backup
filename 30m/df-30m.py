#%%
from matplotlib.ticker import MultipleLocator
import pandas as pd
import matplotlib.pyplot as plt
# %%
data = pd.read_csv('RxPacketTrace-100Ghz.txt', sep='\s+')
df = pd.DataFrame(data)
df
#%%
Time = df['time']
Time
#%%
db = df['SINR(dB)']
db.describe()
# %%
## criando o gráfico

fig, ax = plt.subplots()
ax.plot(Time, db)
plt.plot(Time, db, linewidth=1, linestyle='-',
          label='Sinr',
          markersize=2,marker='o', color = 'blue'
          )
plt.title('Signal rate (30m)')

plt.xlabel('Time')
plt.xticks(range(0, 101, 10))
ax.set_xlim(0,101)
ax.set_ylim(51, 52.2)
ax.yaxis.set_major_locator(MultipleLocator(0.2))
plt.ylabel('db')
plt.legend()
plt.show()

# %%
