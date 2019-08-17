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

appraisals = {}

for repo, groups in data.items():
    for type, checks in groups.items():
        for checker, messages in checks.items():
            for line, appraisal in messages.items():
                if not appraisal:
                    if type == 'present':
                        message = indices[repo][checker][line]
                        if checker == 'eradicate':
                            if 'test' in line.lower():
                                appraisals[line] = 'eradicate test'
                            elif 'ERADICATE_PARAMETER_NOT_NULLABLE' in message[0]:
                                appraisals[line] = 'eradicate parameter'
                            elif 'ERADICATE_INCONSISTENT_SUBCLASS_PARAMETER_ANNOTATION' in message[0]:
                                appraisals[line] = 'eradicate override'
                            elif 'ERADICATE_FIELD_NOT_INITIALIZED' in message[0]:
                                appraisals[line] = 'unstrict field'
                        elif checker == 'nullsafe' and 'NULLSAFE_FIELD_NOT_NULLABLE' in message[0]:
                            appraisals[line] = 'missing annotation'

with open('disagreement.json') as input:
    for line in input:
        if '""' in line:
            first_quote = find_nth(line, '"', 1)
            second_quote = find_nth(line, '"', 2)
            key = line[first_quote+1:second_quote]
            if key in appraisals:
                print(line.replace('""', '"'+appraisals[key]+'"'),end='')
                continue
        print(line, end='')
