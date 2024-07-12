#findS

import pandas as pd

# Load dataset
df = pd.read_csv('enjoysport.csv')

# Separate positive and negative examples
hp = df[df['enjoysport'] != 'no'].values.tolist()
hn = df[df['enjoysport'] == 'no'].values.tolist()

# Initialize hypothesis
h = ['0'] * (df.shape[1] - 1)

# Find maximally specific hypothesis
for example in hp:
    for i, value in enumerate(example[:-1]):
        if h[i] == '0':
            h[i] = value
        elif h[i] != value:
            h[i] = '?'

# Print results
print(f'Positive examples:\n{hp}')
print(f'Negative examples:\n{hn}')
print(f'Maximally specific hypothesis:\n{h}')
