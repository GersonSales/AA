#https://www.urionlinejudge.com.br/judge/en/problems/view/1556
from itertools import chain, combinations



def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


string = raw_input()
combinations = list(map(''.join, powerset(string)))

result = []#set()

for comb in  combinations:
    if (comb in string and comb != ""):
        result.append(comb)

result = list(result)
result.sort()

for comb in result:
    print comb




