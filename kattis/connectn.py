import sys

X, Y, N = map(int, sys.stdin.readline().split())
data = []
for _ in range(X):
    line = sys.stdin.readline().split()
    data.append(line)
msg = ''

#X, Y, N = 3, 6, 3
#data = [['B', 'O', 'O', 'O', 'O', 'O'], ['B', 'O', 'O', 'O', 'O', 'O'], ['B', 'R', 'R', 'O', 'O', 'O']]

#X, Y, N = 4, 4, 4
#data = [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['B', 'B', 'B', 'O'], ['R', 'R', 'R', 'R']]
#data = [['B', 'O', 'O', 'O'], ['O', 'B', 'O', 'O'], ['B', 'B', 'B', 'O'], ['R', 'R', 'B', 'B']]

# 3 ways of winning: horizonal sum, vertical sum, diagnoal sum

# Horizontal: If an N-length slice of line equals
# either "B..B" or "R..R", then that color wins

for line in data:
    for start_idx in range(N):
        check = ''.join(line[start_idx : start_idx + N])
        if check == 'B' * N:
            msg = "BLUE WINS"
        elif check == 'R' * N:
            msg = "RED WINS"

# Vertical: If an N-length concatenation of ith index (ix) equals
# either "B..B" or "R..R", then that color wins

for column in range(Y):
    check = ''
    for line in data:
        check += line[column]
    if check == 'B' * N:
        msg = "BLUE WINS"
    elif check == 'R' * N:
        msg = "RED WINS"

# Diagnoal: If an N-length concatenation of diagnoals
# (top-left to bottom-right or top-right to bottom-left)
# equals either "B..B" or "R..R", then that color wins

# top-left to bottom-right
for start_idx in range(Y - N + 1):
    check = ''
    for row, line in enumerate(data):
        check += line[row + start_idx]
    if check == 'B' * N:
        msg = "BLUE WINS"
    elif check == 'R' * N:
        msg = "RED WINS"

# top-right to bottom-left
for start_idx in range(-1, N - Y - 2, -1):
    check = ''
    for row, line in enumerate(data, start=1):
        check += line[-row + start_idx + 1]
    if check == 'B' * N:
        msg = "BLUE WINS"
    elif check == 'R' * N:
        msg = "RED WINS"

# No winner
if msg == '':
    print("NONE")
else:
    print(msg)
