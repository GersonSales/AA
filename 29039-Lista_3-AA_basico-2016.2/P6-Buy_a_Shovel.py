k, r = map(int, raw_input().split())

n = 1
while ((k * n) % 10 != 0 and (k * n) % 10 != r):
    n += 1

print n
