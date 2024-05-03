import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Metric': ['MSE', 'RMSE', 'R2', 'MAE'],
    'Ridge Regression': [0.428, 0.654, 0.532, 0.506],
    'kNN': [0.3283932607084337, 0.5730560711731739, 0.5328715761570901, 0.42921551940931985],
    'Random Forest': [0.40085, 0.63313, 0.56188, 0.476]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))
bars = df.plot(kind='bar', ax=ax, color=['skyblue', 'lightgreen', 'salmon'])
ax.set_title('Model Comparison on Different Metrics')
ax.set_xlabel('Metric')
ax.set_ylabel('Value')
ax.set_xticks(range(len(df['Metric'])))
ax.set_xticklabels(df['Metric'])
ax.legend(title='Model')
ax.grid(True)

for bar in bars.containers:
    ax.bar_label(bar, fmt='%.3f', label_type='edge', padding=3)
plt.tight_layout()
plt.show()
