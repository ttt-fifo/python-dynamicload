"""
"""

IMPORTS = """
"""

IMP = {}
for i in IMPORTS.split('\n'):
    if i == '':
        continue
    i = i.rstrip('\n')
    IMP[i.split(' ')[-1]] = i
del IMPORTS
del i


def __getattr__(name):
    """
    """
    try:
        exec(IMP[name], globals(), globals())
        IMP[name] = eval(name)
        return IMP[name]
    except Exception:
        print(f'ERROR while attempting to dynamically load {name}:')
        raise


def __dir__():
    """
    """
    return IMP.keys()
