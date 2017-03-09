#http://codeforces.com/problemset/problem/570/B

n, m = map(int, raw_input().split())

if (n == 1):
    print 1
else:
    if (m > n / 2):
        print m - 1
    else:
        print m + 1

