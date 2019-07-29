"""
"""

IMPORTS = """
import examplepackage.examplemodule01 as exmodule
from .examplemodule02 import myfunction02 as exfunct
from examplemodule02 import MyClassTwo as ExClass
"""

REGISTRY = {}
for i in IMPORTS.split('\n'):
    if i == '':
        continue
    i = i.rstrip('\n')
    REGISTRY[i.split(' ')[-1]] = i
del IMPORTS
del i


def __getattr__(name):
    """
    """
    try:
        exec(REGISTRY[name], globals(), globals())
        REGISTRY[name] = eval(name)
        return REGISTRY[name]
    except Exception:
        print(f'ERROR while attempting to dynamically load {name}:')
        raise


def __dir__():
    """
    """
    return REGISTRY.keys()
