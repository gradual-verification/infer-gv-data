import os

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from common import *

plt.figure(figsize=(10,10))
venn3(subsets=(4, 4, 2, 4, 2, 2, 1),
    set_labels=['', '', ''],
    subset_label_formatter=lambda l: ''
)
dir = 'venn'
os.makedirs(dir, exist_ok=True)
plt.savefig('{}/{}.png'.format(dir, 'all'), transparent=True)
plt.clf()

exit()

for repo in repos:
    sets = {}
    for name, issuetype in checkers.items():
        sets[name] = lines('{}/{}.txt'.format(repo, name), issuetype)
    keys = sets.keys()
    plt.figure(figsize=(10,10))
    venn3([sets[k] for k in keys],
        set_labels=['' for k in keys],
        subset_label_formatter=lambda l: ''
    )
    dir = 'venn/static'
    os.makedirs(dir, exist_ok=True)
    plt.savefig('{}/{}.png'.format(dir, repo))
    plt.clf()

for repo in repos:
    try:
        sets = dynamic_sets(repo)
        keys = sets.keys()
        venn3([sets[k] for k in keys], set_labels=keys)
        plt.title(repo)
        dir = 'venn/dynamic'
        os.makedirs(dir, exist_ok=True)
        plt.savefig('{}/{}.png'.format(dir, repo))
        plt.clf()
    except:
        pass
