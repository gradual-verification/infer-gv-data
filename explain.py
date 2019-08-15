import sys

from common import *

def others(checker):
    cloned_checkers = list(checkers)
    cloned_checkers.remove(checker)
    return cloned_checkers

def explain(repo):
    sets = {}
    for name, issuetype in checkers.items():
        sets[name] = lines('{}/{}.txt'.format(repo, name), issuetype)
    for name in checkers.keys():
        other1, other2 = others(name)
        present = sets[name] - (sets[other1] | sets[other2])
        if present:
            print('Only present in {}:'.format(name))
            for line in sorted(present):
                print(line)
            print()
        missing = (sets[other1] & sets[other2]) - sets[name]
        if missing:
            print('Only missing in {}:'.format(name))
            for line in sorted(missing):
                print(line)
            print()

if len(sys.argv) < 2:
    print('Please specify a repository.')
else:
    choice = sys.argv[1]
    if choice not in repos:
        print('Your choice is not one of the choices.')
    else:
        explain(choice)
