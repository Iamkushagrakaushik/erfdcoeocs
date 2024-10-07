n, k = map(int, input().split())
m = 240 - k  # Total time available after accounting for other activities
i = 0
time_spent = 0

while i < n and time_spent + 5 * (i + 1) <= m:
    i += 1
    time_spent += 5 * i

print(i)
