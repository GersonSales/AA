#https://www.urionlinejudge.com.br/judge/en/problems/view/1556


def powerset(s):
    x = len(s)
    result = []
    for i in range(1 << x):
        result.append([s[j] for j in range(x) if (i & (1 << j))])
    return result

string = raw_input()
combinationss = list(map(''.join, powerset(string)))

result = set()

for comb in  combinationss:
    if (comb != ""):
        result.add(comb)

result = list(result)
result.sort()

for comb in result:
    print comb




