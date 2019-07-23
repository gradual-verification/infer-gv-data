import os

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# https://stackoverflow.com/a/1884277/5044950
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

# https://stackoverflow.com/a/3277515/5044950
def lines(filename, issuetype):
    with open(filename) as file:
        strings = [line.rstrip() for line in file if issuetype in line]
        strings = [s for s in strings if s.lstrip() == s]
        return {s[:find_nth(s, ':', 2)] for s in strings}

repos = [
    'okbuck',
    'caffeine',
    'butterknife',
]

checkers = {
    'eradicate': 'ERADICATE',
    'gradual': 'GRADUAL_STATIC',
    'nullsafe': 'NULLSAFE',
}

for repo in repos:
    sets = {}
    for name, issuetype in checkers.items():
        sets[name] = lines('{}/{}.txt'.format(repo, name), issuetype)
    keys = sets.keys()
    venn3([sets[k] for k in keys], set_labels=keys)
    plt.title(repo)
    dir = 'venn'
    os.makedirs(dir, exist_ok=True)
    plt.savefig('{}/{}.png'.format(dir, repo))
    plt.clf()
