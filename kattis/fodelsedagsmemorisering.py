import sys
import pandas as pd

# Parse input
# data = [['Sanna', '1', '16/03'], ['Simon', '2', '16/03'], ['Saga', '3', '14/10']]
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    info = sys.stdin.readline().split()
    data.append(info)

# Create a dataframe
df = pd.DataFrame(data, columns = ['name', 'score', 'bday'])
df['score'] = df['score'].astype(int)
df['bday'] = pd.to_datetime(df['bday'], format='%d/%m')
df = df.sort_values(['bday','score'])

# Group friends by bday, create a max score boolean, and filter
max_idx = df.groupby('bday')['score'].transform(max) == df['score']
grouped_df = df[max_idx].sort_values('name')

print(len(grouped_df))
chosen_friends = grouped_df['name'].values.tolist()
for friend in chosen_friends:
    print(friend)
