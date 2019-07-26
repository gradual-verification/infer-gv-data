import common

def bar(sets):
    all = len(sets['dereferences'] - (sets['limit'] | sets['unannotated']))
    unannotated = len(sets['unannotated'] - sets['limit'])
    limit = len(sets['limit'])
    total = len(sets['dereferences'] | sets['unannotated'] | sets['limit'])
    if limit > 0 and unannotated > 0 and all > 0:
        return {
            'limit': limit/total,
            'unannotated': unannotated/total,
            'all': all/total,
        }
    else:
        return None

bars = {}
for repo in common.repos:
    this_bar = bar(common.dynamic_sets(repo))
    if this_bar:
        bars[repo] = this_bar
for k in ['limit', 'unannotated', 'all']:
    print('\\addplot+ [ybar] coordinates {')
    for repo, this_bar in bars.items():
        if repo == 'FloatingActionButtonSpeedDial':
            repo = 'FABSD'
        if repo == 'skaffold-tools-for-java':
            repo = 'skaffold-tools'
        print('  ({},{})'.format(repo, this_bar[k]))
    print('};')
