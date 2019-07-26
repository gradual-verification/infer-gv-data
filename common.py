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
    'jib',
    'skaffold-tools-for-java',
    'AutoDispose',
    'ReactiveNetwork',
    'keyvaluestore',
    'filesystem-generator',
    'butterknife',
    'picasso',
    'RIBs',
    'FloatingActionButtonSpeedDial',
    'uLeak',
    'QRContact',
    'test-ribs',
    'ColdSnap',
    'OANDAFX',
    'meal-planner',
]

checkers = {
    'eradicate': 'ERADICATE',
    'gradual': 'GRADUAL_STATIC',
    'nullsafe': 'NULLSAFE',
}

modes = {
    'dereferences': ['GRADUAL_DEREFERENCE'],
    'unannotated': ['GRADUAL_CHECK'],
    'limit': ['GRADUAL_CHECK'],
}

def dynamic_sets(repo):
    sets = {}
    for name, issuetypes in modes.items():
        the_set = set()
        filename = '{}/{}.txt'.format(repo, name)
        for issuetype in issuetypes:
            the_set |= lines(filename, issuetype)
        sets[name] = the_set
    return sets
