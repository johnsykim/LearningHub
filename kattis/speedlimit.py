import sys

n = 0

while n != -1:
    n = int(input())
    if n == -1: break
    
    arr_speed = []
    arr_stopwatch = []

    for _ in range(n):
        speed, time = tuple(map(int, sys.stdin.readline().split()))
        arr_speed.append(speed)
        arr_stopwatch.append(time)

    arr_time = [y - x for x, y in zip(arr_stopwatch, arr_stopwatch[1:])]
    arr_time.insert(0, arr_stopwatch[0])

    distance_driven = sum([speed * time for speed, time
                           in zip(arr_speed, arr_time)])

    print(distance_driven, "miles")
