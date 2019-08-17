import json
import pprint

from common import *

prefix = '/home/sam/sandbox/NullSafetyJava-master/nullaway-eval/repos/'

def index(repo, checker):
    mapping = {}
    with open('{}/{}.txt'.format(repo, checker)) as file:
        current = None
        span = []
        for line in file:
            if line.isspace():
                if current:
                    mapping[current] = span
                current = None
                span = []
            if line.startswith(prefix):
                span = []
                colon = find_nth(line, ':', 2)
                current = line[len(prefix)+len(repo)+1:colon]
            span.append(line)
    return mapping

indices = {}
for repo in repos:
    indices[repo] = {}
    for checker in checkers.keys():
        indices[repo][checker] = index(repo, checker)

with open('disagreement.json') as file:
    data = json.load(file)

for repo, groups in data.items():
    for type, checks in groups.items():
        for messages in checks.values():
            for line, appraisal in messages.items():
                if not appraisal:
                    print([(len(indices[repo][checker][line]) if line in indices[repo][checker] else 0) for checker in checkers.keys()])
